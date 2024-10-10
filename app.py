from flask import Flask, jsonify, render_template, request, url_for
from generate_sitecore_components import get_sitecore_components

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello-world')
def hello_world():
    return """<div class="text-green-500">Hello from the server!</div>"""

@app.route('/submit-blind-mode', methods=['POST'])
def submit_blind_mode():
    return """<button class="absolute m-4 right-0 top-10 lg:top-0 md:top-0 sm:top-0" hx-post="/submit-night-mode" hx-on::before-request="toggleDarkMode(true);" hx-swap="outerHTML"><i class="fas fa-moon"></i></button>"""

@app.route('/submit-night-mode', methods=['POST'])
def submit_night_mode():
    return """<button class="absolute m-4 right-0 top-10 lg:top-0 md:top-0 sm:top-0: text-white" hx-post="/submit-blind-mode" hx-on::before-request="toggleDarkMode(false);" hx-swap="outerHTML"><i class="fas fa-sun"></i></button>"""

@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    values = request.form.get('values')
    
    if not name or not values:
       return """<div class="text-red-600 text-sm dark: text-red-800">Component Name and Component Fields are required.</div>"""

    return get_sitecore_components(name, values)
    
if __name__ == '__main__':
    app.run(debug=True)