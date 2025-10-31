from flask import Flask, render_template, request, jsonify
import requests
import base64
import os
import traceback
from dotenv import load_dotenv

load_dotenv()  # Carga las variables de entorno



app = Flask(__name__)


# Rutas
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/project_original_designs')
def project_original_designs():
    return render_template('project_original_designs.html')

@app.route('/project_physical_projects')
def project_physical_projects():
    return render_template('project_physical_projects.html')

@app.route('/project_interior_plans')
def project_interior_plans():
    return render_template('project_interior_plans.html')


@app.route('/ai_rendering')
def ai_rendering():
    return render_template('ai_rendering.html')

@app.route('/ai_interior_modeling')
def ai_interior_modeling():
    return render_template('ai_interior_modeling.html')

@app.route('/ai_solutions')
def ai_solutions():
    return render_template('ai_solutions.html')

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True

if __name__ == "__main__":
    app.run(debug=True)
