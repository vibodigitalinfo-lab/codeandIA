<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:atom="http://www.w3.org/2005/Atom">
<xsl:output method="html" encoding="UTF-8" indent="yes"/>

<xsl:template match="/">
  <html lang="es">
  <head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title><xsl:value-of select="rss/channel/title"/> — Feed RSS</title>
    <style>
      :root { --bg:#0b0d12; --fg:#e8e8ec; --muted:#8b909d; --accent:#6aa6ff; --card:#12151d; --border:#252a35; }
      * { box-sizing:border-box; margin:0; padding:0; }
      body { font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif; background:var(--bg); color:var(--fg); min-height:100vh; display:flex; flex-direction:column; align-items:center; padding:3rem 1rem; line-height:1.6; }
      .container { width:100%; max-width:720px; }
      .icon { width:64px; height:64px; margin-bottom:1.5rem; opacity:0.9; }
      h1 { font-size:clamp(1.75rem,4vw,2.5rem); font-weight:700; margin-bottom:0.5rem; }
      .subtitle { color:var(--muted); margin-bottom:2rem; font-size:1.05rem; }
      .card { background:var(--card); border:1px solid var(--border); border-radius:12px; padding:1.5rem; margin-bottom:1rem; }
      .card h2 { font-size:1.1rem; font-weight:600; margin-bottom:0.5rem; }
      .card p { color:var(--muted); font-size:0.95rem; }
      .feed-title { color:var(--accent); text-decoration:none; }
      .feed-title:hover { text-decoration:underline; }
      .meta { display:flex; flex-wrap:wrap; gap:1rem; margin-top:0.75rem; font-size:0.85rem; color:var(--muted); }
      .meta span { display:flex; align-items:center; gap:0.35rem; }
      .items { margin-top:2rem; }
      .item { background:var(--card); border:1px solid var(--border); border-radius:10px; padding:1.25rem; margin-bottom:1rem; transition:border-color 0.2s; }
      .item:hover { border-color:var(--accent); }
      .item-title { font-weight:600; margin-bottom:0.35rem; }
      .item-title a { color:var(--fg); text-decoration:none; }
      .item-title a:hover { color:var(--accent); }
      .item-desc { color:var(--muted); font-size:0.9rem; margin-bottom:0.5rem; }
      .item-meta { font-size:0.8rem; color:var(--muted); }
      .cta { margin-top:2rem; text-align:center; }
      .btn { display:inline-block; background:var(--accent); color:#0b0d12; font-weight:600; padding:0.85rem 1.75rem; border-radius:8px; text-decoration:none; transition:opacity 0.2s; }
      .btn:hover { opacity:0.9; }
      .footer { margin-top:3rem; text-align:center; font-size:0.8rem; color:var(--muted); }
      .footer a { color:var(--accent); text-decoration:none; }
    </style>
  </head>
  <body>
    <div class="container">
      <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
        <path d="M4 11a9 9 0 019 9"/><path d="M4 4a16 16 0 0116 16"/><circle cx="5" cy="19" r="1"/>
      </svg>
      <h1><xsl:value-of select="rss/channel/title"/></h1>
      <p class="subtitle"><xsl:value-of select="rss/channel/description"/></p>

      <div class="card">
        <h2>📡 Feed RSS</h2>
        <p>Esta página es un <strong>feed RSS</strong> — un formato XML para suscribirse a actualizaciones automáticas.</p>
        <p>No está pensada para leerse directamente en el navegador.</p>
        <div class="meta">
          <span>🔗 <a class="feed-title" href="{rss/channel/link}" target="_blank"><xsl:value-of select="rss/channel/link"/></a></span>
          <span>📅 Última actualización: <xsl:value-of select="rss/channel/lastBuildDate"/></span>
          <span>📄 <xsl:value-of select="count(rss/channel/item)"/> artículos</span>
        </div>
      </div>

      <div class="card">
        <h2>➕ Cómo suscribirse</h2>
        <p>Copia esta URL en tu lector de feeds favorito:</p>
        <p style="font-family:monospace; background:#0a0c12; padding:0.5rem 0.75rem; border-radius:6px; border:1px solid var(--border); word-break:break-all;">
          <a class="feed-title" href="{rss/channel/atom:link/@href}"><xsl:value-of select="rss/channel/atom:link/@href"/></a>
        </p>
        <p style="margin-top:0.75rem; color:var(--muted); font-size:0.9rem;">
          Lectores populares: <a class="feed-title" href="https://feedly.com" target="_blank">Feedly</a>,
          <a class="feed-title" href="https://inoreader.com" target="_blank">Inoreader</a>,
          <a class="feed-title" href="https://netnewswire.com" target="_blank">NetNewsWire</a>,
          <a class="feed-title" href="https://reederapp.com" target="_blank">Reeder</a>, etc.
        </p>
      </div>

      <div class="items">
        <h2 style="margin-bottom:1rem;">📝 Últimos artículos</h2>
        <xsl:for-each select="rss/channel/item">
          <div class="item">
            <div class="item-title">
              <a href="{link}" target="_blank"><xsl:value-of select="title"/></a>
            </div>
            <div class="item-desc"><xsl:value-of select="description"/></div>
            <div class="item-meta">
              <span>📅 <xsl:value-of select="pubDate"/></span>
              <xsl:if test="category">
                <span style="margin-left:1rem;">🏷️ <xsl:value-of select="category"/></span>
              </xsl:if>
            </div>
          </div>
        </xsl:for-each>
      </div>

      <div class="cta">
        <a class="btn" href="{rss/channel/link}" target="_blank">Ir a la web →</a>
      </div>

      <div class="footer">
        <p>Generado con Jekyll · <a href="{rss/channel/link}" target="_blank"><xsl:value-of select="rss/channel/title"/></a></p>
      </div>
    </div>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>