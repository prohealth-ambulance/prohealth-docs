snippet = """
<script>
function gtag_report_conversion(url) {
  var callback = function () {
    if (typeof(url) != 'undefined') {
      window.location = url;
    }
  };
  gtag('event', 'conversion', {
      'send_to': 'AW-10900640971/PkhMCLLjiI0dEMup6s0o',
      'event_callback': callback
  });
  return false;
}
</script>
"""
with open('index.html','r') as f: html=f.read()
html=html.replace('</head>', snippet+'</head>', 1)
html=html.replace('href="tel:7872124700"', 'href="tel:7872124700" onclick="return gtag_report_conversion(\'tel:7872124700\')"')
with open('index.html','w') as f: f.write(html)
print('Conversion snippet agregado')
