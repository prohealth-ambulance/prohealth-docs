with open('index.html','r',encoding='utf-8') as f: html=f.read()
import re
html = re.sub(r"\n  if \(window\.innerWidth > 900\) \{\n    document\.querySelectorAll\('\.service-item'\).*?\n  \}\n", "\n", html, flags=re.DOTALL)
with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Cursor removido')
