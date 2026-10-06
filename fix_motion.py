with open('index.html','r',encoding='utf-8') as f: html=f.read()

html = html.replace("""
  const heroImg = document.querySelector('.hero-right img');
  if (heroImg && window.innerWidth > 900) {
    window.addEventListener('scroll', () => {
      const y = window.scrollY;
      if (y < 900) heroImg.style.transform = 'translateY(' + (y * 0.25) + 'px) scale(1.08)';
    }, { passive: true });
  }
""", """
  if (window.innerWidth > 900) {
    document.querySelectorAll('.service-item').forEach(item => {
      const num = item.querySelector('.service-num');
      if (!num) return;
      item.addEventListener('mousemove', e => {
        const r = item.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width - 0.5;
        const y = (e.clientY - r.top) / r.height - 0.5;
        num.style.transform = 'translate(' + (x * 24) + 'px,' + (y * 16) + 'px) rotate(' + (x * 6) + 'deg)';
      });
      item.addEventListener('mouseleave', () => { num.style.transform = ''; });
    });
  }
""")

html = html.replace('.hero-right img { will-change: transform; transition: transform .1s linear; }\n', '')

with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Parallax quitado, cursor agregado')
