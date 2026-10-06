with open('index.html','r',encoding='utf-8') as f: html=f.read()

# 1. Room to room -> De cuarto a cuarto
html = html.replace('<div class="service-name">Room to room</div>', '<div class="service-name">De cuarto a cuarto</div>')

# 2. Texto vertical en ingles
html = html.replace(
    '<span class="hero-vertical">Ambulancia ALS \u00b7 Puerto Rico \u00b7 Est. 2009</span>',
    '<span class="hero-vertical es">Ambulancia ALS \u00b7 Puerto Rico \u00b7 Est. 2009</span>\n    <span class="hero-vertical en" style="display:none">ALS Ambulance \u00b7 Puerto Rico \u00b7 Est. 2009</span>'
)

with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Primera ronda ok')
