import re, os
with open('index.html','r') as f:
    html = f.read()
html = re.sub(r'src="data:image/jpeg;base64,[^"]*"(\s+alt="Unidad de ambulancia)', r'src="hero-opt.jpg"\1', html, count=1)
html = re.sub(r'src="data:image/jpeg;base64,[^"]*"(\s+alt="Ambulancia ALS Pro Health)', r'src="hero-2-opt.jpg"\1', html, count=1)
with open('index.html','w') as f:
    f.write(html)
print(f'HTML: {os.path.getsize("index.html")/1024:.0f}KB')
