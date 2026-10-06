with open('index.html','r',encoding='utf-8') as f: html=f.read()

html=html.replace('<div class="hero-num"><p>01</p><p>Servicios ALS</p></div>\n','')

html=html.replace(
    'Cada servicio comienza con la misma responsabilidad: cuidar al paciente durante todo el trayecto.<br><br><span style="font-size:0.85rem;color:#999;">',
    '<span style="font-family:\'DM Serif Display\',serif;font-size:1.35rem;line-height:1.35;color:#111;display:block;margin-bottom:14px;">Cada servicio comienza con la misma responsabilidad: <em style="color:var(--orange);">cuidar al paciente durante todo el trayecto.</em></span><span style="font-size:0.85rem;color:#999;">'
)
html=html.replace(
    'Every service begins with the same responsibility: caring for the patient throughout the entire journey.<br><br><span style="font-size:0.85rem;color:#999;">',
    '<span style="font-family:\'DM Serif Display\',serif;font-size:1.35rem;line-height:1.35;color:#111;display:block;margin-bottom:14px;">Every service begins with the same responsibility: <em style="color:var(--orange);">caring for the patient throughout the entire journey.</em></span><span style="font-size:0.85rem;color:#999;">'
)

with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Listo')
