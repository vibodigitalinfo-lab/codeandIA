/* codeandIA: comportamiento compartido (menú y tema). */
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

  function init() {
    initNav();
    initTheme();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
