with open('index.html','r', encoding='utf-8') as f: html=f.read()
viejo='Con unidades ALS y param\u00e9dicos certificados, atendemos a Puerto Rico con un servicio de ambulancia dise\u00f1ado para emergencias cr\u00edticas, traslados entre hospitales, transporte especializado y servicios programados, manteniendo siempre un est\u00e1ndar profesional y confiable.'
nuevo='Ambulancia Privada ALS en Puerto Rico \u2014 emergencias m\u00e9dicas, traslados hospitalarios y servicios programados con ambulancias Tipo III y personal param\u00e9dico certificado.'
html=html.replace(viejo, nuevo)
viejo_en='With ALS units and certified paramedics, we serve Puerto Rico with an ambulance service designed for critical emergencies, hospital transfers, specialized transport, and scheduled services \u2014 always maintaining a professional and reliable standard.'
nuevo_en='Private ALS Ambulance in Puerto Rico \u2014 medical emergencies, hospital transfers and scheduled services with Type III ambulances and certified paramedic staff.'
html=html.replace(viejo_en, nuevo_en)
with open('index.html','w', encoding='utf-8') as f: f.write(html)
print('Parrafo actualizado')
