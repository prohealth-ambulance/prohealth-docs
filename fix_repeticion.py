with open('index.html','r',encoding='utf-8') as f: html=f.read()

html=html.replace('<p class="hero-eyebrow es">Servicios ALS \u00b7 Puerto Rico</p>\n    <p class="hero-eyebrow en">ALS Services \u00b7 Puerto Rico</p>\n','')

html=html.replace(
    'Ambulancia privada ALS en Puerto Rico, con unidades Tipo III y param\u00e9dicos certificados para emergencias, traslados hospitalarios y servicios programados.',
    'Ambulancia privada ALS en Puerto Rico. Unidades Tipo III, param\u00e9dicos certificados. Emergencias, traslados hospitalarios y servicios programados.'
)
html=html.replace(
    'Private ALS ambulance in Puerto Rico, with Type III units and certified paramedics for emergencies, hospital transfers and scheduled services.',
    'Private ALS ambulance in Puerto Rico. Type III units, certified paramedics. Emergencies, hospital transfers and scheduled services.'
)

with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Corregido')
