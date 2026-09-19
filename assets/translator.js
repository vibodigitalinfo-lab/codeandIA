(function () {
  'use strict';

  var LS_LANG = 'lang';
  var CACHE_KEY = 'translations_cache_v1';

  function getLang() {
    try {
      var l = localStorage.getItem(LS_LANG);
      if (l === 'en' || l === 'es') return l;
    } catch (e) {}
    return 'es';
  }

  function setLang(l) {
    try { localStorage.setItem(LS_LANG, l); } catch (e) {}
  }

  var SKIP_TAGS = {
    SCRIPT: 1, STYLE: 1, NOSCRIPT: 1, CODE: 1, PRE: 1,
    KBD: 1, SAMP: 1, TEXTAREA: 1, SELECT: 1, OPTION: 1, SVG: 1, IFRAME: 1
  };

  var cache = {};
  try { cache = JSON.parse(localStorage.getItem(CACHE_KEY) || '{}') || {}; } catch (e) {}

  var originals = new WeakMap();
  var currentNodes = [];
  var map = {};
  var translating = false;
  var runId = 0;

  function wordCount(s) {
    var m = s.match(/[\u00C0-\u024F\u1E00-\u1FFFA-Za-zñç]+/g);
    return m ? m.length : 0;
  }

  function collect() {
    var nodes = [];
    var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        var p = n.parentElement;
        if (!p) return NodeFilter.FILTER_REJECT;
        if (SKIP_TAGS[p.tagName]) return NodeFilter.FILTER_REJECT;
        if (p.closest('.visually-hidden')) return NodeFilter.FILTER_REJECT;
        var t = n.nodeValue;
        if (!t || !t.trim()) return NodeFilter.FILTER_REJECT;
        if (wordCount(t) < 2) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    while (walker.nextNode()) nodes.push(walker.currentNode);
    return nodes;
  }

  function norm(t) {
    return t.replace(/\s+/g, ' ').trim();
  }

  function buildMap(nodes) {
    var m = {};
    for (var i = 0; i < nodes.length; i++) {
      var t = norm(nodes[i].nodeValue);
      if (!t) continue;
      if (!m[t]) m[t] = [];
      m[t].push(nodes[i]);
    }
    return m;
  }

  function translateBatch(texts) {
    var joined = texts.join('\n');
    var url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=es&tl=en&dt=t&q=' + encodeURIComponent(joined);
    return fetch(url)
      .then(function (r) { if (!r.ok) throw new Error('translate ' + r.status); return r.json(); })
      .then(function (data) {
        var tuples = data && data[0];
        if (!Array.isArray(tuples)) throw new Error('bad response');
        var full = '';
        for (var i = 0; i < tuples.length; i++) full += (tuples[i] && tuples[i][0]) || '';
        var lines = full.split('\n');
        if (lines.length !== texts.length) throw new Error('line mismatch ' + lines.length + ' vs ' + texts.length);
        return texts.map(function (_, i) { return lines[i]; });
      });
  }

  function applyToNodes(text, trans) {
    var list = map[text] || [];
    for (var i = 0; i < list.length; i++) {
      var n = list[i];
      if (!n.nodeValue) continue;
      if (!originals.has(n)) originals.set(n, n.nodeValue);
      n.nodeValue = trans;
    }
  }

  function saveCache() {
    try {
      var keys = Object.keys(cache);
      while (keys.length > 2500) delete cache[keys.shift()];
      localStorage.setItem(CACHE_KEY, JSON.stringify(cache));
    } catch (e) {}
  }

  function updateButtons(lang) {
    var switcher = document.querySelector('.lang-switch');
    if (!switcher) return;
    var btns = switcher.querySelectorAll('.lang-btn');
    for (var i = 0; i < btns.length; i++) {
      var on = btns[i].getAttribute('data-lang') === lang;
      btns[i].classList.toggle('is-active', on);
      btns[i].setAttribute('aria-pressed', on ? 'true' : 'false');
    }
  }

  function translatePage() {
    if (translating || getLang() === 'es') return;
    translating = true;
    var id = ++runId;
    function alive() { return id === runId && getLang() === 'en'; }

    currentNodes = collect();
    map = buildMap(currentNodes);
    var uniques = Object.keys(map);

    uniques.forEach(function (t) {
      if (t in cache && cache[t]) applyToNodes(t, cache[t]);
    });

    var remaining = uniques.filter(function (t) { return !(t in cache); });

    var BATCH = 22;
    var idx = 0;

    function finish() {
      if (!alive()) return;
      translating = false;
      saveCache();
      document.documentElement.setAttribute('lang', 'en');
      updateButtons('en');
    }

    function next() {
      if (!alive()) { translating = false; return; }
      if (idx >= remaining.length) { finish(); return; }
      var batch = remaining.slice(idx, idx + BATCH);
      idx += BATCH;
      translateBatch(batch).then(function (results) {
        if (!alive()) { translating = false; return; }
        for (var i = 0; i < results.length; i++) {
          var t = batch[i];
          var tr = results[i];
          if (tr && tr.trim() && tr !== t) {
            cache[t] = tr;
            applyToNodes(t, tr);
          } else {
            cache[t] = t;
          }
        }
        next();
      }).catch(function () {
        if (!alive()) { translating = false; return; }
        var i = 0;
        function one() {
          if (!alive()) return;
          if (i >= batch.length) { next(); return; }
          var t = batch[i++];
          fetch('https://translate.googleapis.com/translate_a/single?client=gtx&sl=es&tl=en&dt=t&q=' + encodeURIComponent(t))
            .then(function (r) { return r.json(); })
            .then(function (data) {
              if (!alive()) return;
              var tr = '';
              try {
                var g = data && data[0];
                if (Array.isArray(g)) for (var j = 0; j < g.length; j++) tr += (g[j] && g[j][0]) || '';
              } catch (e) {}
              if (tr && tr.trim() && tr !== t) { cache[t] = tr; applyToNodes(t, tr); }
              else { cache[t] = t; }
              one();
            }).catch(function () { cache[t] = t; one(); });
        }
        one();
      });
    }

    next();
  }

  function restorePage() {
    translating = false;
    runId++;
    for (var i = 0; i < currentNodes.length; i++) {
      var n = currentNodes[i];
      if (originals.has(n)) n.nodeValue = originals.get(n);
    }
    map = {};
    document.documentElement.setAttribute('lang', 'es');
    updateButtons('es');
  }

  window.__tr = {
    apply: function (lang) {
      setLang(lang);
      if (lang === 'en') translatePage();
      else restorePage();
    },
    boot: function () {
      var l = getLang();
      updateButtons(l);
      if (l === 'en') translatePage();
    }
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', window.__tr.boot);
  } else {
    window.__tr.boot();
  }
})();