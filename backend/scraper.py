import random
from datetime import datetime, timedelta
from database import inserir_vaga, limpar_vagas


UPWORK_VAGAS = [
    {'titulo': 'Desenvolvedor Python Senior', 'preco': 'R$ 80-150/h', 'descricao': 'Projeto de automação com Python e APIs'},
    {'titulo': 'Script Python para Web Scraping', 'preco': 'R$ 60-100/h', 'descricao': 'Coletar dados de websites específicos'},
    {'titulo': 'API REST com Flask', 'preco': 'R$ 70-120/h', 'descricao': 'Criar API para integração com mobile app'},
    {'titulo': 'Bot Telegram com Python', 'preco': 'R$ 50-90/h', 'descricao': 'Desenvolver bot automático para Telegram'},
]

WORKANA_VAGAS = [
    {'titulo': 'Frontend React Developer', 'preco': 'R$ 40-80/h', 'descricao': 'Componentes React para dashboard de dados'},
    {'titulo': 'Desenvolvedor Full Stack', 'preco': 'R$ 60-100/h', 'descricao': 'Django + React para e-commerce'},
    {'titulo': 'Designer UI/UX', 'preco': 'R$ 35-70/h', 'descricao': 'Design de aplicativo mobile'},
    {'titulo': 'Especialista em SEO', 'preco': 'R$ 45-85/h', 'descricao': 'Otimização de site para buscadores'},
]

FIVERR_VAGAS = [
    {'titulo': 'Logo Design', 'preco': 'R$ 25-60/h', 'descricao': 'Criar logo criativo para startup'},
    {'titulo': 'Redator de Conteúdo', 'preco': 'R$ 20-50/h', 'descricao': 'Artigos para blog sobre tecnologia'},
    {'titulo': 'Ilustrador Digital', 'preco': 'R$ 30-80/h', 'descricao': 'Ilustrações para livro infantil'},
    {'titulo': 'Tradutor Inglês-Português', 'preco': 'R$ 15-40/h', 'descricao': 'Tradução de documentos técnicos'},
]

PLATAFORMAS = {
    'Upwork': UPWORK_VAGAS,
    'Workana': WORKANA_VAGAS,
    'Fiverr': FIVERR_VAGAS
}

def raspar_vagas_simuladas():
    
    vagas_coletadas = []
    
    for plataforma, vagas_lista in PLATAFORMAS.items():
        
        vagas_selecionadas = random.sample(vagas_lista, min(2, len(vagas_lista)))
        
        for vaga in vagas_selecionadas:
        
            dias_atras = random.randint(0, 7)
            data = (datetime.now() - timedelta(days=dias_atras)).strftime('%Y-%m-%d')
            
            vaga_completa = {
                'titulo': vaga['titulo'],
                'plataforma': plataforma,
                'preco': vaga['preco'],
                'descricao': vaga['descricao'],
                'data': data
            }
            vagas_coletadas.append(vaga_completa)
    
    return vagas_coletadas

def atualizar_vagas():

    print('[SCRAPER] Iniciando coleta de vagas...')
    
    try:
        
        limpar_vagas()
        print('[SCRAPER] Banco de dados limpo')
        
    
        vagas = raspar_vagas_simuladas()
        print(f'[SCRAPER] {len(vagas)} vagas coletadas')
        
        
        for vaga in vagas:
            inserir_vaga(
                titulo=vaga['titulo'],
                plataforma=vaga['plataforma'],
                preco=vaga['preco'],
                descricao=vaga['descricao'],
                data=vaga['data']
            )
        
        print(f'[SCRAPER] ✅ {len(vagas)} vagas inseridas com sucesso')
        return True
        
    except Exception as e:
        print(f'[SCRAPER] ❌ Erro durante scraping: {str(e)}')
        return False

if __name__ == '__main__':
    
    atualizar_vagas()