with open('index.html','r',encoding='utf-8') as f: html=f.read()

css_add = '''
    .hero-left { position: relative; }
    .hero-vertical {
      position: absolute; left: 18px; top: 50%;
      transform: translateY(-50%) rotate(-90deg); transform-origin: left center;
      white-space: nowrap; font-size: 0.6rem; letter-spacing: .3em;
      color: #bbb; text-transform: uppercase; font-weight: 500;
    }
    .hero-title { font-weight: 400; }
    .hero-body-wrap { display: flex; gap: 14px; align-items: flex-start; }
    .hero-body-line { width: 1px; height: 40px; background: var(--orange); flex-shrink: 0; margin-top: 4px; }
    .hero-right { position: relative; }
    .hero-right::before { content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 2px; background: var(--orange); z-index: 2; }
    .hero-num { position: absolute; bottom: 28px; right: 28px; z-index: 2; text-align: right; }
    .hero-num p:first-child { font-family: 'DM Serif Display', serif; font-size: 2.2rem; color: var(--orange); margin: 0; line-height: 1; }
    .hero-num p:last-child { font-size: 0.55rem; color: rgba(255,255,255,.6); letter-spacing: .2em; text-transform: uppercase; margin: 4px 0 0; }
    @media (max-width: 900px) { .hero-vertical { display: none; } .hero-num { display: none; } }
'''
html = html.replace('</style>', css_add + '</style>', 1)

html = html.replace(
    '<div class="hero-left">\n    <p class="hero-eyebrow es">',
    '<div class="hero-left">\n    <span class="hero-vertical">Ambulancia ALS · Puerto Rico · Est. 2009</span>\n    <p class="hero-eyebrow es">'
)

html = html.replace(
    '<p class="hero-body es">Ambulancia Privada ALS en Puerto Rico — emergencias médicas, traslados hospitalarios y servicios programados con ambulancias Tipo III y personal paramédico certificado.</p>',
    '<div class="hero-body-wrap"><div class="hero-body-line"></div><p class="hero-body es" style="margin:0 0 48px">Emergencias médicas, traslados hospitalarios y servicios programados con unidades Tipo III y paramédicos certificados.</p></div>'
)

html = html.replace(
    '<div class="hero-right">\n    <img',
    '<div class="hero-right">\n    <div class="hero-num"><p>01</p><p>Servicios ALS</p></div>\n    <img'
)

with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Editorial aplicado')
