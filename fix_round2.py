with open('index.html','r',encoding='utf-8') as f: html=f.read()

# reCAPTCHA note bilingue
html = html.replace(
    '<p class="recaptcha-note">Este sitio est\u00e1 protegido por reCAPTCHA. Se aplican la <a href="https://policies.google.com/privacy" target="_blank">Pol\u00edtica de privacidad</a> y los <a href="https://policies.google.com/terms" target="_blank">T\u00e9rminos de servicio</a> de Google.</p>',
    '<p class="recaptcha-note es">Este sitio est\u00e1 protegido por reCAPTCHA. Se aplican la <a href="https://policies.google.com/privacy" target="_blank">Pol\u00edtica de privacidad</a> y los <a href="https://policies.google.com/terms" target="_blank">T\u00e9rminos de servicio</a> de Google.</p>\n          <p class="recaptcha-note en" style="display:none">This site is protected by reCAPTCHA. The Google <a href="https://policies.google.com/privacy" target="_blank">Privacy Policy</a> and <a href="https://policies.google.com/terms" target="_blank">Terms of Service</a> apply.</p>'
)

# Opciones del formulario separadas por idioma
old_select = '''<select name="service" required>
              <option value="" disabled selected></option>
              <option value="emergencia" data-es>Emergencia m\u00e9dica</option>
              <option value="traslado" data-es>Traslado m\u00e9dico</option>
              <option value="psiquiatrico" data-es>Transporte psiqui\u00e1trico</option>
              <option value="evento" data-es>Cobertura de evento</option>
              <option value="signos" data-es>Evaluaci\u00f3n de signos vitales</option>
              <option value="room" data-es>Room to room</option>
              <option value="otro" data-es>Otro</option>
              <option value="emergency" data-en>Medical emergency</option>
              <option value="transport" data-en>Medical transport</option>
              <option value="psychiatric" data-en>Psychiatric transport</option>
              <option value="event" data-en>Event coverage</option>
              <option value="vitals" data-en>Vital signs assessment</option>
              <option value="room2" data-en>Room to room</option>
              <option value="other" data-en>Other</option>
            </select>'''

new_select = '''<select name="service" required class="svc-select-es">
              <option value="" disabled selected></option>
              <option value="emergencia">Emergencia m\u00e9dica</option>
              <option value="traslado">Traslado m\u00e9dico</option>
              <option value="psiquiatrico">Transporte psiqui\u00e1trico</option>
              <option value="evento">Cobertura de evento</option>
              <option value="signos">Evaluaci\u00f3n de signos vitales</option>
              <option value="room">De cuarto a cuarto</option>
              <option value="otro">Otro</option>
            </select>
            <select name="service_en" class="svc-select-en" style="display:none">
              <option value="" disabled selected></option>
              <option value="emergency">Medical emergency</option>
              <option value="transport">Medical transport</option>
              <option value="psychiatric">Psychiatric transport</option>
              <option value="event">Event coverage</option>
              <option value="vitals">Vital signs
cd ~/Downloads/prohealth-docs && cat > fix_round2.py << 'EOF'
with open('index.html','r',encoding='utf-8') as f: html=f.read()

# reCAPTCHA note bilingue
html = html.replace(
    '<p class="recaptcha-note">Este sitio est\u00e1 protegido por reCAPTCHA. Se aplican la <a href="https://policies.google.com/privacy" target="_blank">Pol\u00edtica de privacidad</a> y los <a href="https://policies.google.com/terms" target="_blank">T\u00e9rminos de servicio</a> de Google.</p>',
    '<p class="recaptcha-note es">Este sitio est\u00e1 protegido por reCAPTCHA. Se aplican la <a href="https://policies.google.com/privacy" target="_blank">Pol\u00edtica de privacidad</a> y los <a href="https://policies.google.com/terms" target="_blank">T\u00e9rminos de servicio</a> de Google.</p>\n          <p class="recaptcha-note en" style="display:none">This site is protected by reCAPTCHA. The Google <a href="https://policies.google.com/privacy" target="_blank">Privacy Policy</a> and <a href="https://policies.google.com/terms" target="_blank">Terms of Service</a> apply.</p>'
)

# Opciones del formulario separadas por idioma
old_select = '''<select name="service" required>
              <option value="" disabled selected></option>
              <option value="emergencia" data-es>Emergencia m\u00e9dica</option>
              <option value="traslado" data-es>Traslado m\u00e9dico</option>
              <option value="psiquiatrico" data-es>Transporte psiqui\u00e1trico</option>
              <option value="evento" data-es>Cobertura de evento</option>
              <option value="signos" data-es>Evaluaci\u00f3n de signos vitales</option>
              <option value="room" data-es>Room to room</option>
              <option value="otro" data-es>Otro</option>
              <option value="emergency" data-en>Medical emergency</option>
              <option value="transport" data-en>Medical transport</option>
              <option value="psychiatric" data-en>Psychiatric transport</option>
              <option value="event" data-en>Event coverage</option>
              <option value="vitals" data-en>Vital signs assessment</option>
              <option value="room2" data-en>Room to room</option>
              <option value="other" data-en>Other</option>
            </select>'''

new_select = '''<select name="service" required class="svc-select-es">
              <option value="" disabled selected></option>
              <option value="emergencia">Emergencia m\u00e9dica</option>
              <option value="traslado">Traslado m\u00e9dico</option>
              <option value="psiquiatrico">Transporte psiqui\u00e1trico</option>
              <option value="evento">Cobertura de evento</option>
              <option value="signos">Evaluaci\u00f3n de signos vitales</option>
              <option value="room">De cuarto a cuarto</option>
              <option value="otro">Otro</option>
            </select>
            <select name="service_en" class="svc-select-en" style="display:none">
              <option value="" disabled selected></option>
              <option value="emergency">Medical emergency</option>
              <option value="transport">Medical transport</option>
              <option value="psychiatric">Psychiatric transport</option>
              <option value="event">Event coverage</option>
              <option value="vitals">Vital signs assessment</option>
              <option value="room2">Room to room</option>
              <option value="other">Other</option>
            </select>'''

html = html.replace(old_select, new_select)

with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Formulario y recaptcha separados')
