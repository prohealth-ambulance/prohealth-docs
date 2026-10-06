h=open('index.html',encoding='utf-8').read()

# 1. Quitar telefono del nav en movil (redundante con el boton del hero)
h=h.replace(
    ".topbar-phone{display:inline!important;font-size:0.75rem;background:var(--orange);color:#fff;padding:6px 12px;text-decoration:none;font-weight:600}",
    ".topbar-phone{display:none!important}"
)

# 2. Texto vertical: mas a la derecha y mas oscuro
h=h.replace(
    ".hero-vertical{font-size:0.5rem!important;letter-spacing:.2em!important;left:8px!important;opacity:.7}",
    ".hero-vertical{font-size:0.5rem!important;letter-spacing:.2em!important;left:14px!important;opacity:1;color:#999}"
)

open('index.html','w',encoding='utf-8').write(h)
print('ok')
