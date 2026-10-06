with open('index.html','r',encoding='utf-8') as f: html=f.read()

# Quitar JS del cursor
start = html.find("  if (window.innerWidth > 900) {\n    document.querySelectorAll('.service-item')")
if start > -1:
    end = html.find("  }\n", html.find("mouseleave", start)) + 4
    html = html[:start] + html[end:]

# Quitar hover CSS que mueve el numero
html = html.replace("""    .service-item:hover .service-num {
      color: rgba(240,124,26,.12); -webkit-text-stroke: 1.5px rgba(240,124,26,.5);
      transform: translateX(-6px);
    }
""", "")
html = html.replace("      transition: all .4s cubic-bezier(.16,1,.3,1);\n", "")

with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Movimiento de numeros eliminado')
