"""Auditor de reviews: la ficha de prueba tiene que estar completa y respaldar
las afirmaciones de tiempo de uso.

Por que existe esto: la pagina /como-trabajamos/ promete que cada review abre
con una ficha de prueba (version, fecha, tiempo de uso, proyecto, limites), y
que lo que se prueba se prueba "durante semanas". Eso es lo mas convincente
del sitio, y nada lo hacia obligatorio: un review nuevo sin ficha se publicaba
igual. Este script convierte la promesa en una comprobacion.

Uso:
    python scripts/auditar_reviews.py          # informa y sale con codigo 1 si falla
    python scripts/auditar_reviews.py --aviso  # solo avisa, nunca falla la CI

Que comprueba:
  1. Cada articulo con category "Review" tiene los 4 campos que exige la ficha:
     version, tiempo, proyecto y limites. Sin los cuatro, el include
     _includes/test-card.html no pinta la ficha y la promesa se rompe.
  2. Si el texto afirma un tiempo de uso concreto ("tres semanas", "un mes",
     "durante semanas", "dos meses"), el campo `tiempo:` del frontmatter tiene
     que corroborarlo. Es el caso que mas se ha dado: un cuerpo que dice un
     plazo y una ficha que no lo menciona.
  3. Aviso (no fallo) si una review no lleva `updated:`: es contenido que
     envejece con los precios y los planes.
"""
import datetime
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ART = os.path.join(RAIZ, 'articulos')
FICHA = ('version', 'tiempo', 'proyecto', 'limites')

# Frases que prometen duracion. El numero va aparte para no depender de como
# se escriba ("3 semanas", "tres semanas", "un mes").
DURACION = re.compile(
    r'(durante\s+semanas|varias\s+semanas|'
    r'(tres|cuatro|cinco|seis|siete|ocho|nueve|diez)\s+semanas?|'
    r'\d+\s+semanas?|'
    r'(un|dos|tres|cuatro|cinco)\s+(mes|meses|semana|semanas)|'
    r'\d+\s+(mes|meses))',
    re.I,
)

# Palabras que hacen que un plazo no sea una promesa de uso propio. Importa
# "hace": "un comando que use hace tres semanas" habla del comando, no de
# cuanto llevo con la herramienta.
EXCEPCION = re.compile(
    # 'hac...' seguido de un plazo: habla de cuando se hizo algo, no de
    # cuanto tiempo llevo con la herramienta. Se escribe con escapes \\u
    # El tramo intermedio admite "tres", "20" o nada: el texto dice
    # "hace tres semanas", no "hace 3 semanas".
    r'hac\w*\s+(\w+\s+)?(a[n\u00f1]os?|semanas?|meses?|d[i\u00ed]as?)|'
    r'\d{4}|precio|plan|memoria',
    re.I,
)

# Un plazo solo cuenta si la frase habla de lo que HIZO el autor. Si es una
# recomendacion al lector ("prueba Trae 2 semanas", "activa un mes de Plus"),
# no hay nada que respaldar. Sin esto el auditor marca lo contrario de lo que
# busca: los 3 fallos que dio la primera vez eran recomendaciones, no claims.
PRIMERA_PERSONA = re.compile(
    r'\b(yo|me|mí|conmigo|usé|usaba|he estado|estuve|probé|probé|'
    r'trabajé|llevo|llevaba|conviví|convivo)\b',
    re.I,
)


def articulos():
    """Rutas de los .md publicados con category Review."""
    for root, dirs, files in os.walk(ART):
        dirs[:] = [d for d in dirs if d not in ('_entrada', 'redirects')]
        for f in sorted(files):
            if not f.endswith('.md'):
                continue
            p = os.path.join(root, f)
            t = io.open(p, encoding='utf-8').read()
            m = re.match(r'^---\n(.*?)\n---\n', t, re.S)
            if not m:
                continue
            fm = m.group(1)
            if not re.search(r'^category:\s*"?Review"?\s*$', fm, re.M):
                continue
            yield p, fm, t[m.end():]


def valor(fm, clave):
    m = re.search(r'^%s:\s*(.+)$' % clave, fm, re.M)
    return m.group(1).strip().strip('"\'') if m else ''


def frases_de_duracion(cuerpo):
    """Frases del cuerpo que Besides un plazo de uso propio del autor.

    Descarta el codigo, los inline y dos cosas mas: los plazos que son
    contexto (fechas, precios) y los que van dirigidos al lector en vez de
    describir lo que hizo el autor.
    """
    fuera = re.sub(r'```.*?```', '', cuerpo, flags=re.S)  # el codigo no cuenta
    fuera = re.sub(r'`[^`]*`', '', fuera)
    salida = []
    for frase in DURACION.finditer(fuera):
        ctx = fuera[max(0, frase.start() - 70):frase.end() + 70]
        if EXCEPCION.search(ctx):
            continue
        # Lo que decide es la oracion completa: si en ella no hay primera
        # persona, el plazo es consejo al lector y no hay nada que respaldar.
        if not PRIMERA_PERSONA.search(_oracion(fuera, frase.start())):
            continue
        salida.append((frase.group(0).strip(), ctx.replace('\n', ' ').strip()))
    return salida


def _oracion(texto, indice):
    """La oracion (o celda de tabla / elemento de lista) que contiene indice."""
    ini = max(
        texto.rfind('\n', 0, indice),
        texto.rfind('. ', 0, indice),
        texto.rfind('| ', 0, indice),
        texto.rfind('**', 0, indice),
    )
    fin_candidates = [p for p in (texto.find('\n', indice),
                                  texto.find('. ', indice),
                                  texto.find('|', indice),
                                  texto.find('**', indice + 3)) if p != -1]
    fin = min(fin_candidates) if fin_candidates else len(texto)
    return texto[ini + 1:fin] if fin > ini + 1 else texto[max(0, indice - 120):indice + 120]


def main():
    solo_aviso = '--aviso' in sys.argv[1:]
    fallos, avisos = [], []
    total = 0

    for ruta, fm, cuerpo in articulos():
        total += 1
        rel = os.path.relpath(ruta, RAIZ).replace('\\', '/')

        faltan = [c for c in FICHA if not valor(fm, c)]
        if faltan:
            fallos.append('ficha incompleta (%s sin: %s) -> %s'
                          % (rel, ', '.join(faltan), os.path.basename(rel)))

        tiempo = valor(fm, 'tiempo')
        for plazo, ctx in frases_de_duracion(cuerpo):
            if tiempo and not DURACION.search(tiempo):
                fallos.append(
                    'el cuerpo dice "%s" pero tiempo: dice "%s" -> %s\n      contexto: %s'
                    % (plazo, tiempo, rel, ctx[:150]))

        if not re.search(r'^updated:', fm, re.M):
            avisos.append('%s no lleva updated: (los planes y precios envejecen)' % rel)

    print('%d reviews revisadas' % total)

    if avisos:
        print('\nAVISOS (%d):' % len(avisos))
        for a in avisos:
            print('  - %s' % a)

    if fallos:
        print('\nFALLOS (%d): la promesa de /como-trabajamos/ no se cumple' % len(fallos))
        for f in fallos:
            print('  - %s' % f)
        return 0 if solo_aviso else 1

    print('\nOK: todas las reviews tienen ficha de prueba completa y el tiempo de'
          ' uso del cuerpo esta respaldado por el frontmatter')
    return 0


if __name__ == '__main__':
    sys.exit(main())