with open('index.html','r',encoding='utf-8') as f: html=f.read()

html=html.replace(
    'Emergencias m\u00e9dicas, traslados hospitalarios y servicios programados con unidades Tipo III y param\u00e9dicos certificados.',
    'Ambulancia privada ALS en Puerto Rico, con unidades Tipo III y param\u00e9dicos certificados para emergencias, traslados hospitalarios y servicios programados.'
)
html=html.replace(
    'Private ALS Ambulance in Puerto Rico \u2014 medical emergencies, hospital transfers and scheduled services with Type III ambulances and certified paramedic staff.',
    'Private ALS ambulance in Puerto Rico, with Type III units and certified paramedics for emergencies, hospital transfers and scheduled services.'
)
html=html.replace(
    'Desde emergencias m\u00e9dicas ALS hasta traslados programados, ofrecemos en Puerto Rico un servicio atendido con el mismo est\u00e1ndar cl\u00ednico y el mismo compromiso con el paciente.',
    'Cada servicio comienza con la misma responsabilidad: cuidar al paciente durante todo el trayecto.<br><br><span style="font-size:0.85rem;color:#999;">Preparaci\u00f3n cl\u00ednica, atenci\u00f3n profesional y un equipo comprometido con hacer bien cada parte del servicio.</span>'
)
html=html.replace(
    'From ALS medical emergencies to scheduled transfers, we offer in Puerto Rico a service handled with the same clinical standard and the same commitment to the patient.',
    'Every service begins with the same responsibility: caring for the patient throughout the entire journey.<br><br><span style="font-size:0.85rem;color:#999;">Clinical preparation, professional care and a team committed to doing every part of the service right.</span>'
)

with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Copy final aplicado')
