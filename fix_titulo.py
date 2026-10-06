content = open('index.html').read()
old = "body.lang-es [data-es] { display: block; }"
new = "body.lang-es [data-es] { display: block; }\n    body.lang-es .section-title[data-es],\n    body.lang-es .section-label[data-es],\n    body.lang-es .section-body[data-es] { display: block; }"
content = content.replace(old, new)
open('index.html', 'w').write(content)
print('Fix aplicado')
