tag = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-10900640971"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag("js", new Date());
  gtag("config", "AW-10900640971");
</script>
"""
with open('index.html','r') as f: html=f.read()
html=html.replace('</head>', tag+'</head>', 1)
with open('index.html','w') as f: f.write(html)
print('Tag agregado')
