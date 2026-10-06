h=open('index.html',encoding='utf-8').read()
css = '''    @media(max-width:900px){
      .hero-vertical{font-size:0.45rem!important;letter-spacing:.2em!important;left:8px!important;opacity:.4}
      .topbar-phone{display:inline!important;font-size:0.75rem;background:var(--orange);color:#fff;padding:6px 12px;text-decoration:none;font-weight:600}
    }
'''
h=h.replace('</style>', css + '</style>', 1)
open('index.html','w',encoding='utf-8').write(h)
print('ok')
