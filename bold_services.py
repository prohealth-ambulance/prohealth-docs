with open('index.html','r',encoding='utf-8') as f: html=f.read()

css_add = '''
    .service-item { position: relative; overflow: hidden; }
    .service-num {
      position: absolute; top: 8px; right: 20px;
      font-size: 6.5rem; font-weight: 400; font-style: italic;
      color: transparent; -webkit-text-stroke: 1.5px rgba(240,124,26,.25);
      line-height: 1; margin: 0; pointer-events: none;
      transition: all .4s cubic-bezier(.16,1,.3,1);
    }
    .service-item:hover .service-num {
      color: rgba(240,124,26,.12); -webkit-text-stroke: 1.5px rgba(240,124,26,.5);
      transform: translateX(-6px);
    }
    .service-name {
      position: relative; padding-left: 16px;
      border-left: 2px solid var(--orange);
      margin-top: 32px;
    }
    .service-desc { padding-left: 18px; position: relative; }
    @media (max-width: 900px) {
      .service-num { font-size: 4.5rem; right: 12px; top: 4px; }
    }
'''
html = html.replace('</style>', css_add + '</style>', 1)

with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Servicios atrevidos')
