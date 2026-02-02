from flask import Flask, jsonify, render_template
from flask_cors import CORS
import os
from database import obter_todas_vagas
from scraper import atualizar_vagas
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

app = Flask(__name__, 
            template_folder=os.path.join(os.path.dirname(__file__), '../frontend'),
            static_folder=os.path.join(os.path.dirname(__file__), '../frontend'),
            static_url_path='')

CORS(app)

scheduler = BackgroundScheduler()
scheduler.add_job(func=atualizar_vagas, trigger="interval", hours=1)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/vagas')
def get_vagas():
    vagas = obter_todas_vagas()
    return jsonify(vagas)

@app.route('/api/status')
def status():
    total_vagas = len(obter_todas_vagas())
    return jsonify({
        'status': 'online',
        'total_vagas': total_vagas,
        'mensagem': 'FreelanceRadar rodando com sucesso'
    })

if __name__ == '__main__':
    print(' Iniciando FreelanceRadar...')
    print(' Acessar em: http://localhost:5000')
    print(' Scraper rodará a cada 1 hora automaticamente')
    
    atualizar_vagas()
    app.run(debug=True, port=5000)