h=open('index.html',encoding='utf-8').read()
h=h.replace('.hero-vertical{font-size:0.45rem!important;letter-spacing:.2em!important;left:8px!important;opacity:.4}', '.hero-vertical{font-size:0.5rem!important;letter-spacing:.2em!important;left:8px!important;opacity:.7}')
open('index.html','w',encoding='utf-8').write(h)
print('ok')
