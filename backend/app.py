from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import os
from database import obter_todas_vagas, obter_vaga_por_id
from scraper import atualizar_vagas
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, 
            template_folder=os.path.join(os.path.dirname(__file__), '../frontend'),
            static_folder=os.path.join(os.path.dirname(__file__), '../frontend'),
            static_url_path='')

app.config['JSON_SORT_KEYS'] = False
CORS(app, resources={r"/api/*": {"origins": "*"}})


scheduler = BackgroundScheduler()
scheduler.add_job(func=atualizar_vagas, trigger="interval", hours=1, id="atualizar_vagas")
scheduler.start()

atexit.register(lambda: scheduler.shutdown())



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/vagas', methods=['GET'])
def get_vagas():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        
        vagas = obter_todas_vagas()
        
        start = (page - 1) * per_page
        end = start + per_page
        
        return jsonify({
            'sucesso': True,
            'total': len(vagas),
            'pagina': page,
            'vagas': vagas[start:end]
        }), 200
        
    except Exception as e:
        logger.error(f"Erro ao obter vagas: {str(e)}")
        return jsonify({'sucesso': False, 'erro': str(e)}), 500

@app.route('/api/vagas/<int:vaga_id>', methods=['GET'])
def get_vaga_detalhes(vaga_id):
    try:
        vaga = obter_vaga_por_id(vaga_id)
        if not vaga:
            return jsonify({'sucesso': False, 'erro': 'Vaga não encontrada'}), 404
        
        return jsonify({'sucesso': True, 'vaga': vaga}), 200
        
    except Exception as e:
        logger.error(f"Erro ao obter vaga {vaga_id}: {str(e)}")
        return jsonify({'sucesso': False, 'erro': str(e)}), 500

@app.route('/api/status', methods=['GET'])
def status():
    try:
        total_vagas = len(obter_todas_vagas())
        return jsonify({
            'sucesso': True,
            'status': 'online',
            'total_vagas': total_vagas,
            'versao': '1.0.0',
            'mensagem': 'FreelanceRadar rodando com sucesso'
        }), 200
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'status': 'error',
            'mensagem': str(e)
        }), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({'sucesso': False, 'erro': 'Rota não encontrada'}), 404

@app.errorhandler(500)
def server_error(error):
    logger.error(f"Erro interno: {str(error)}")
    return jsonify({'sucesso': False, 'erro': 'Erro interno do servidor'}), 500

if __name__ == '__main__':
    print('🚀 Iniciando FreelanceRadar...')
    print('📍 Acessar em: http://localhost:5000')
    print('⏰ Scraper rodará automaticamente a cada 1 hora')
    print('=' * 50)
    
    atualizar_vagas()
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False
    )