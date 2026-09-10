import os
import re
from datetime import datetime, timedelta

articles = [
    'articulos/comparativas/deepseek-vs-chatgpt-gratuitos-para-programar.md',
    'articulos/comparativas/claude-ai-vs-chatgpt-plus-para-programar.md',
    'articulos/comparativas/namecheap-vs-porkbun-dominio-es-estudiante.md',
    'articulos/comparativas/windsurf-vs-cursor-ai-aprender-programar.md',
    'articulos/reviews/hostinger-review-2026.md',
    'articulos/comparativas/github-copilot-business-vs-individual-programador-solo.md',
    'articulos/comparativas/cursor-ai-plan-pro-vs-free.md',
    'articulos/listas/5-proyectos-portfolio-desarrollador-ia-fin-de-semana.md',
    'articulos/guias/mejores-prompts-chatgpt-corregir-errores-codigo-junior.md',
    'articulos/guias/que-dominio-comprar-primer-proyecto-web.md',
    'articulos/listas/7-herramientas-ia-gratuitas-estudiantes-desarrollo-web-2026.md',
    'articulos/guias/como-usar-github-copilot-practicas-daw.md',
    'articulos/guias/como-configurar-cursor-ai-vscode-desde-cero.md',
    'articulos/guias/como-publicar-primera-web-internet-barato-ia.md',
    'articulos/guias/chatgpt-para-aprender-javascript-principiante.md',
    'articulos/guias/crear-portfolio-desarrollador-web-con-ia.md',
    'articulos/comparativas/chatgpt-vs-cursor-para-programar.md',
    'articulos/comparativas/hostinger-vs-namecheap-primer-dominio.md',
    'articulos/comparativas/cursor-vs-github-copilot-para-aprender.md',
    'articulos/reviews/chatgpt-plus-para-programadores.md',
    'articulos/reviews/cursor-ai-review-espanol.md',
    'articulos/reviews/github-copilot-gratis-estudiantes.md',
    'articulos/listas/mejores-teclados-mecanicos-programar.md',
    'articulos/comparativas/monitor-ultrawide-programar.md',
    'articulos/listas/raton-ergonomico-programadores.md',
    'articulos/listas/silla-ergonomica-barata-programar.md',
    'articulos/listas/webcam-programar-streaming.md',
]

base = datetime(2026, 9, 10)
base_path = 'C:/Users/ivanm/OneDrive/Documentos/codeandIA'

for i, rel in enumerate(articles):
    p = os.path.join(base_path, rel)
    if not os.path.exists(p):
        print('NOT FOUND:', rel)
        continue
    d = (base - timedelta(days=i)).strftime('%Y-%m-%d')
    with open(p, 'r', encoding='utf-8') as f: c = f.read()
    c = re.sub(r'^date:.*$', f'date: {d}', c, flags=re.MULTILINE)
    with open(p, 'w', encoding='utf-8') as f: f.write(c)
    print(f'{rel} -> {d}')
print('Done')