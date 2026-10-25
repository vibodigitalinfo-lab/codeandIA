/* codeandIA: comportamiento compartido (menú, tema y botón de copiar). */
(function () {
  'use strict';

  /* Menú de navegación móvil */
  function initNav() {
    var toggle = document.getElementById('nav-toggle');
    var menu = document.getElementById('nav-menu');
    if (!toggle || !menu) return;

    function close() {
      menu.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    }

    toggle.addEventListener('click', function () {
      var open = !menu.classList.contains('open');
      menu.classList.toggle('open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });

    menu.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') close();
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') close();
    });
  }

  /* Toggle de tema claro/oscuro (recuerda la preferencia en localStorage) */
  function initTheme() {
    var toggle = document.getElementById('theme-toggle');
    if (!toggle) return;

    var metaTheme = document.querySelector('meta[name="theme-color"]');
    var LIGHT_BG = '#fbfcfe';
    var DARK_BG = '#0f1320';

    function isDark() {
      return document.documentElement.getAttribute('data-theme') === 'dark';
    }

    function applyTheme(dark) {
      if (dark) {
        document.documentElement.setAttribute('data-theme', 'dark');
      } else {
        document.documentElement.removeAttribute('data-theme');
      }
      if (metaTheme) {
        metaTheme.setAttribute('content', dark ? DARK_BG : LIGHT_BG);
      }
      var label = dark ? 'Cambiar a modo claro' : 'Cambiar a modo oscuro';
      toggle.setAttribute('aria-label', label);
      toggle.setAttribute('title', label);
    }

    toggle.addEventListener('click', function () {
      var next = !isDark();
      applyTheme(next);
      try {
        localStorage.setItem('theme', next ? 'dark' : 'light');
      } catch (e) {}
    });

    applyTheme(isDark());
  }

  /* Botón "Copiar" en cada bloque de código o texto preformateado
     (prompts, código, comandos) de artículos y páginas. El botón va fuera
     del <pre> para que no se desplace con el scroll horizontal. */
  function initCopy() {
    var blocks = document.querySelectorAll('.article-content pre, .page-content pre');
    if (!blocks.length) return;

    var status = document.createElement('p');
    status.className = 'visually-hidden';
    status.setAttribute('role', 'status');
    status.setAttribute('aria-live', 'polite');
    document.body.appendChild(status);

    function fallbackCopy(text) {
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.setAttribute('readonly', '');
      ta.style.position = 'fixed';
      ta.style.top = '-1000px';
      document.body.appendChild(ta);
      ta.select();
      var ok = false;
      try { ok = document.execCommand('copy'); } catch (e) {}
      document.body.removeChild(ta);
      return ok;
    }

    function copy(text) {
      if (navigator.clipboard && window.isSecureContext) {
        return navigator.clipboard.writeText(text).then(
          function () { return true; },
          function () { return fallbackCopy(text); }
        );
      }
      return Promise.resolve(fallbackCopy(text));
    }

    Array.prototype.forEach.call(blocks, function (pre) {
      var wrap = document.createElement('div');
      wrap.className = 'code-block';
      pre.parentNode.insertBefore(wrap, pre);
      wrap.appendChild(pre);

      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'copy-btn';
      btn.textContent = 'Copiar';
      btn.setAttribute('aria-label', 'Copiar al portapapeles');
      wrap.appendChild(btn);

      var timer;
      btn.addEventListener('click', function () {
        var code = pre.querySelector('code');
        var text = (code || pre).textContent.replace(/\n$/, '');
        copy(text).then(function (ok) {
          btn.textContent = ok ? 'Copiado' : 'Error';
          btn.classList.toggle('is-copied', ok);
          status.textContent = ok ? 'Copiado al portapapeles' : 'No se pudo copiar';
          clearTimeout(timer);
          timer = setTimeout(function () {
            btn.textContent = 'Copiar';
            btn.classList.remove('is-copied');
            status.textContent = '';
          }, 2000);
        });
      });
    });
  }

  function init() {
    initNav();
    initTheme();
    initCopy();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
