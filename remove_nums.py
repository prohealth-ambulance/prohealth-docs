with open('index.html','r',encoding='utf-8') as f: html=f.read()
import re
html = re.sub(r'<div class="service-num">0[1-6]</div>', '', html)
html = html.replace('      margin-top: 32px;\n', '')
with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Numeros eliminados')
