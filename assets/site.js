/* codeandIA: utilidades compartidas (guardados, progreso y atajos). */
window.codeandia = (function () {
  var CLAVE_GUARDADOS = 'candaias:guardados';
  var CLAVE_PROGRESO = 'candaias:progreso';
  var MAX_GUARDADOS = 60;
  var MAX_HISTORIAL = 40;

  function leer(clave, pordefecto) {
    try {
      var bruto = localStorage.getItem(clave);
      if (!bruto) return pordefecto;
      var valor = JSON.parse(bruto);
      return valor === null || valor === undefined ? pordefecto : valor;
    } catch (e) {
      return pordefecto;
    }
  }

  function escribir(clave, valor) {
    try {
      localStorage.setItem(clave, JSON.stringify(valor));
      return true;
    } catch (e) {
      return false;
    }
  }

  function sinAcentos(texto) {
    return String(texto == null ? '' : texto)
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .toLowerCase();
  }

  var api = {
    sinAcentos: sinAcentos,

    obtenerGuardados: function () {
      var lista = leer(CLAVE_GUARDADOS, []);
      return Array.isArray(lista) ? lista : [];
    },

    estaGuardado: function (url) {
      return api.obtenerGuardados().some(function (g) { return g.url === url; });
    },

    guardarArticulo: function (datos) {
      var lista = api.obtenerGuardados();
      if (api.estaGuardado(datos.url)) {
        return api.quitarArticulo(datos.url);
      }
      lista.unshift({
        url: datos.url,
        title: datos.title,
        category: datos.category,
        date: datos.date
      });
      if (lista.length > MAX_GUARDADOS) lista = lista.slice(0, MAX_GUARDADOS);
      escribir(CLAVE_GUARDADOS, lista);
      return true;
    },

    quitarArticulo: function (url) {
      var lista = api.obtenerGuardados().filter(function (g) { return g.url !== url; });
      escribir(CLAVE_GUARDADOS, lista);
      return false;
    },

    vaciarGuardados: function () {
      escribir(CLAVE_GUARDADOS, []);
    },

    registrarProgreso: function (datos) {
      var actual = leer(CLAVE_PROGRESO, null);
      if (actual && actual.url === datos.url) {
        if (typeof actual.pct === 'number' && actual.pct >= datos.pct) return;
        actual.pct = datos.pct;
        actual.title = datos.title;
        actual.ts = Date.now();
        escribir(CLAVE_PROGRESO, actual);
        return;
      }
      escribir(CLAVE_PROGRESO, {
        url: datos.url,
        title: datos.title,
        pct: datos.pct,
        ts: Date.now()
      });
    },

    obtenerProgreso: function () {
      return leer(CLAVE_PROGRESO, null);
    },

    progresoDeUrl: function (url) {
      var actual = api.obtenerProgreso();
      return actual && actual.url === url && typeof actual.pct === 'number' ? actual.pct : 0;
    },

    /* Rutas de aprendizaje: pasos completados por ruta. */
    obtenerPasos: function (rutaId) {
      var mapa = leer('candaias:rutas', {});
      var ids = mapa && mapa[rutaId];
      return Array.isArray(ids) ? ids : [];
    },

    alternarPaso: function (rutaId, indice) {
      var mapa = leer('candaias:rutas', {});
      if (!mapa || typeof mapa !== 'object') mapa = {};
      var ids = Array.isArray(mapa[rutaId]) ? mapa[rutaId] : [];
      var pos = ids.indexOf(indice);
      if (pos === -1) ids.push(indice);
      else ids.splice(pos, 1);
      mapa[rutaId] = ids;
      escribir('candaias:rutas', mapa);
      return mapa[rutaId];
    }
  };

  /* Botón "Guardar" de cada artículo. */
  function initGuardar() {
    var btn = document.getElementById('save-article');
    if (!btn) return;
    var url = btn.getAttribute('data-url');
    var icono = btn.querySelector('.tool-btn-icon');
    var etiqueta = btn.querySelector('.tool-btn-label');

    function pintar() {
      var activo = api.estaGuardado(url);
      btn.setAttribute('aria-pressed', activo ? 'true' : 'false');
      btn.classList.toggle('is-active', activo);
      if (icono) icono.textContent = activo ? '★' : '☆';
      if (etiqueta) etiqueta.textContent = activo ? 'Guardado' : 'Guardar';
    }

    btn.addEventListener('click', function () {
      api.guardarArticulo({
        url: url,
        title: btn.getAttribute('data-title') || '',
        category: btn.getAttribute('data-category') || '',
        date: btn.getAttribute('data-date') || ''
      });
      pintar();
    });

    pintar();
  }

  /* Imprimir / PDF. */
  function initImprimir() {
    var btn = document.getElementById('print-article');
    if (!btn) return;
    btn.addEventListener('click', function () { window.print(); });
  }

  /* Guarda por dónde iba el lector para "Continúa leyendo". */
  function initProgreso() {
    var contenido = document.getElementById('article-content');
    var url = document.querySelector('link[rel="canonical"]');
    var titulo = document.querySelector('.article-title');
    if (!contenido || !url || !titulo) return;

    var destino = url.getAttribute('href');
    var texto = titulo.textContent.trim();
    var avisado = false;

    function medir() {
      if (avisado) return;
      var caja = contenido.getBoundingClientRect();
      var altoTotal = caja.height || 1;
      var visto = Math.min(Math.max(window.innerHeight - caja.top, 0), altoTotal);
      var pct = Math.round((visto / altoTotal) * 100);
      if (pct >= 70) {
        avisado = true;
        api.registrarProgreso({ url: destino, title: texto, pct: pct });
      }
    }

    window.addEventListener('scroll', medir, { passive: true });
    window.addEventListener('pagehide', medir);
    medir();
  }

  /* Atajo "/" para ir al buscador, como en la documentación. */
  function initAtajoBusqueda() {
    document.addEventListener('keydown', function (e) {
      if (e.key !== '/' || e.metaKey || e.ctrlKey || e.altKey) return;
      var el = document.activeElement;
      if (el) {
        var etiqueta = (el.tagName || '').toLowerCase();
        if (etiqueta === 'input' || etiqueta === 'textarea' || etiqueta === 'select' || el.isContentEditable) return;
      }
      e.preventDefault();
      window.location.href = '/buscar/';
    });
  }

  function init() {
    initGuardar();
    initImprimir();
    initProgreso();
    initAtajoBusqueda();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  return api;
})();
