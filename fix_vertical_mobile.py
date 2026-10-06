h=open('index.html',encoding='utf-8').read()
if '@media (max-width: 900px) { .hero-vertical { display: none; }' not in h:
    h=h.replace('</style>','    @media(max-width:900px){.hero-vertical{display:none!important}}\n</style>',1)
    print('ok')
else:
    print('ya existe')
open('index.html','w',encoding='utf-8').write(h)
