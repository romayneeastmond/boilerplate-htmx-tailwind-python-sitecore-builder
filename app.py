from flask import Flask, jsonify, render_template, request, url_for
from generate_sitecore_components import get_sitecore_components

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello-world')
def hello_world():
    return "<div class='text-green-500'>Hello from the server!</div>"

@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    values = request.form.get('values')
    
    if not name or not values:
       return """<div class="text-red-600 text-sm dark: text-red-800">Component Name and Component Fields are required.</div>"""

    return get_sitecore_components(name, values)
    
if __name__ == '__main__':
    app.run(debug=True)