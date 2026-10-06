h=open('index.html',encoding='utf-8').read()
h=h.replace('src="ph-logo.jpg"', 'src="ph-logo.png"')
open('index.html','w',encoding='utf-8').write(h)
print('ok')
