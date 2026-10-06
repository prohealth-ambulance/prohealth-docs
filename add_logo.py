h=open('index.html',encoding='utf-8').read()
h=h.replace(
    '<div class="topbar-logo"><span>Pro</span>Health Ambulance</div>',
    '<a href="/" class="topbar-logo"><img src="ph-logo.jpg" alt="Pro Health Ambulance Services" style="height:28px;width:auto;display:block"></a>'
)
open('index.html','w',encoding='utf-8').write(h)
print('ok')
