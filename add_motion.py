with open('index.html','r',encoding='utf-8') as f: html=f.read()

css_add = '''
    @keyframes slideL { from { opacity:0; transform:translateX(-40px); } to { opacity:1; transform:none; } }
    @keyframes slideR { from { opacity:0; transform:translateX(40px); } to { opacity:1; transform:none; } }
    .hero-title { animation: none; opacity: 1; }
    .hero-title span.w1 { display:block; opacity:0; animation: slideL .8s .1s cubic-bezier(.16,1,.3,1) forwards; }
    .hero-title span.w2 { display:block; opacity:0; animation: slideR .8s .3s cubic-bezier(.16,1,.3,1) forwards; }
    .hero-title span.w3 { display:block; opacity:0; animation: slideL .8s .5s cubic-bezier(.16,1,.3,1) forwards; }
    .hero-right img { will-change: transform; transition: transform .1s linear; }
'''
html = html.replace('</style>', css_add + '</style>', 1)

html = html.replace(
    '<h1 class="hero-title es">Capacidad.<br><em>Respuesta.</em><br>Confianza.</h1>',
    '<h1 class="hero-title es"><span class="w1">Capacidad.</span><span class="w2"><em>Respuesta.</em></span><span class="w3">Confianza.</span></h1>'
)
html = html.replace(
    '<h1 class="hero-title en">Capacity.<br><em>Response.</em><br>Trust.</h1>',
    '<h1 class="hero-title en"><span class="w1">Capacity.</span><span class="w2"><em>Response.</em></span><span class="w3">Trust.</span></h1>'
)

js_add = '''
  const heroImg = document.querySelector('.hero-right img');
  if (heroImg && window.innerWidth > 900) {
    window.addEventListener('scroll', () => {
      const y = window.scrollY;
      if (y < 900) heroImg.style.transform = 'translateY(' + (y * 0.25) + 'px) scale(1.08)';
    }, { passive: true });
  }
'''
html = html.replace('</script>\n</body>', js_add + '</script>\n</body>', 1)

with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Movimiento agregado')
