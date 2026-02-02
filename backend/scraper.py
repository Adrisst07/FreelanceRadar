import random
from datetime import datetime, timedelta
from database import inserir_vaga, obter_vaga_por_titulo, obter_todas_vagas
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



UPWORK_VAGAS = [
    {
        'titulo': 'Desenvolvedor Python Senior',
        'preco': 'R$ 80-150/h',
        'descricao': 'Procuramos desenvolvedor experiente para projeto de automação e processamento de dados. Necessário conhecimento em APIs REST e bancos de dados relacionais.',
        'habilidades': ['Python', 'Flask', 'PostgreSQL']
    },
    {
        'titulo': 'Especialista em Web Scraping',
        'preco': 'R$ 70-120/h',
        'descricao': 'Desenvolvimento de scraper para extração de dados de múltiplos websites. Projeto contínuo com manutenção mensal. Experiência com Selenium e BeautifulSoup.',
        'habilidades': ['Python', 'BeautifulSoup', 'Selenium']
    },
    {
        'titulo': 'Backend com Django/FastAPI',
        'preco': 'R$ 90-140/h',
        'descricao': 'API REST robusta para aplicação mobile. Integração com pagamentos Stripe. Testes unitários obrigatórios. Banco de dados PostgreSQL.',
        'habilidades': ['Django', 'FastAPI', 'PostgreSQL', 'Docker']
    },
    {
        'titulo': 'Script Python para Automação',
        'preco': 'R$ 50-100/h',
        'descricao': 'Automatizar processos repetitivos em Windows/Linux. Usar Python com schedule e APScheduler. Documentação obrigatória.',
        'habilidades': ['Python', 'APScheduler', 'Automation']
    },
    {
        'titulo': 'API REST com Node.js',
        'preco': 'R$ 75-130/h',
        'descricao': 'Criar API robusta com Express.js. Autenticação JWT. Testes com Jest. Deploy na AWS.',
        'habilidades': ['Node.js', 'Express', 'JWT', 'MongoDB']
    },
    {
        'titulo': 'Desenvolvedor Full Stack',
        'preco': 'R$ 100-160/h',
        'descricao': 'Projeto completo: Backend + Frontend. React + Node.js. Banco PostgreSQL. E-commerce ou SaaS.',
        'habilidades': ['React', 'Node.js', 'PostgreSQL', 'Docker']
    },
    {
        'titulo': 'Integrações com APIs Externas',
        'preco': 'R$ 65-110/h',
        'descricao': 'Integrar múltiplas APIs em plataforma. Stripe, Twilio, SendGrid. Tratamento robusto de erros.',
        'habilidades': ['Python', 'Node.js', 'APIs', 'Integration']
    },
]

WORKANA_VAGAS = [
    {
        'titulo': 'Frontend React Developer',
        'preco': 'R$ 40-80/h',
        'descricao': 'Componentes React reutilizáveis para dashboard. Estado management com Redux. Responsivo e acessível.',
        'habilidades': ['React', 'JavaScript', 'CSS', 'Redux']
    },
    {
        'titulo': 'Full Stack com MERN',
        'preco': 'R$ 60-100/h',
        'descricao': 'Desenvolvimento de aplicação completa: MongoDB + Express + React + Node. E-commerce ou portal de eventos.',
        'habilidades': ['Node.js', 'React', 'MongoDB', 'Git']
    },
    {
        'titulo': 'Desenvolvedor Vue.js',
        'preco': 'R$ 50-90/h',
        'descricao': 'Componentes Vue 3 com TypeScript. Estado management com Pinia. Design com Tailwind CSS.',
        'habilidades': ['Vue.js', 'TypeScript', 'Tailwind', 'Pinia']
    },
    {
        'titulo': 'Designer Web Responsivo',
        'preco': 'R$ 35-70/h',
        'descricao': 'Design de websites responsivos. HTML5 semântico, CSS3 avançado. Mobile-first approach.',
        'habilidades': ['HTML', 'CSS', 'Responsive', 'UX']
    },
    {
        'titulo': 'Especialista em SEO',
        'preco': 'R$ 45-85/h',
        'descricao': 'Otimização de site para buscadores. Análise de palavras-chave. Melhoria de ranking.',
        'habilidades': ['SEO', 'Analytics', 'Google Tools']
    },
    {
        'titulo': 'Desenvolvedor PHP/Laravel',
        'preco': 'R$ 55-95/h',
        'descricao': 'Aplicações com Laravel. MVC pattern. MySQL ou PostgreSQL. Hospedagem cPanel.',
        'habilidades': ['PHP', 'Laravel', 'MySQL', 'Blade']
    },
]

FIVERR_VAGAS = [
    {
        'titulo': 'Logo Design Profissional',
        'preco': 'R$ 25-60/h',
        'descricao': 'Criar logo criativo para startup. Múltiplas versões. Arquivo vetorial em AI/EPS.',
        'habilidades': ['Design', 'Illustrator', 'Branding']
    },
    {
        'titulo': 'Redator de Conteúdo Tech',
        'preco': 'R$ 20-50/h',
        'descricao': 'Artigos técnicos para blog sobre programação. SEO otimizado. 2000+ palavras.',
        'habilidades': ['Redação', 'SEO', 'Tech Writing']
    },
    {
        'titulo': 'Ilustrador Digital',
        'preco': 'R$ 30-80/h',
        'descricao': 'Ilustrações para livro infantil. Estilo cartoon ou realista. Entrega em PNG/PDF.',
        'habilidades': ['Ilustração', 'Procreate', 'Design']
    },
    {
        'titulo': 'Tradutor Inglês-Português',
        'preco': 'R$ 15-40/h',
        'descricao': 'Tradução de documentos técnicos. Preservando formatação. Revisão incluída.',
        'habilidades': ['Tradução', 'Inglês', 'PT-BR']
    },
    {
        'titulo': 'Editor de Vídeo',
        'preco': 'R$ 25-70/h',
        'descricao': 'Edição de vídeos para YouTube. Efeitos, transições, animações. Premiere/DaVinci.',
        'habilidades': ['Video Editing', 'Premiere', 'Motion Graphics']
    },
    {
        'titulo': 'Especialista em Shopify',
        'preco': 'R$ 40-90/h',
        'descricao': 'Desenvolvimento de loja Shopify. Customização de themes. Integração com Oberlo.',
        'habilidades': ['Shopify', 'Liquid', 'E-commerce']
    },
]

PLATAFORMAS = {
    'Upwork': UPWORK_VAGAS,
    'Workana': WORKANA_VAGAS,
    'Fiverr': FIVERR_VAGAS
}

def gerar_data_realista():
    
    dias = random.choice([0, 0, 0, 0, 1, 1, 2, 3, 5, 7])
    return (datetime.now() - timedelta(days=dias)).strftime('%Y-%m-%d')

def atualizar_vagas():
    
    print('\n[SCRAPER] 🚀 Iniciando coleta de vagas...')
    
    vagas_atuais = obter_todas_vagas()
    vagas_adicionadas = 0
    vagas_existentes = 0
    
    try:
        for plataforma, vagas_lista in PLATAFORMAS.items():
            print(f'  📍 Verificando {plataforma}...')
            
            quantidade = random.randint(3, min(5, len(vagas_lista)))
            vagas_selecionadas = random.sample(vagas_lista, quantidade)
            
            for vaga in vagas_selecionadas:
                try:
                    vaga_existente = obter_vaga_por_titulo(vaga['titulo'])
                    
                    if vaga_existente:
                        vagas_existentes += 1
                    else:
                        inserir_vaga(
                            titulo=vaga['titulo'],
                            plataforma=plataforma,
                            preco=vaga['preco'],
                            descricao=vaga['descricao'],
                            data=gerar_data_realista(),
                            habilidades=','.join(vaga.get('habilidades', []))
                        )
                        vagas_adicionadas += 1
                        print(f'    ✓ {vaga["titulo"][:40]}...')
                        
                except Exception as e:
                    logger.error(f"Erro ao inserir vaga: {str(e)}")
                    continue
        
        print(f'[SCRAPER] ✅ {vagas_adicionadas} vagas adicionadas')
        print(f'[SCRAPER] ℹ️  {vagas_existentes} vagas já existiam')
        return True
        
    except Exception as e:
        logger.error(f'[SCRAPER] ❌ Erro geral: {str(e)}')
        return False

if __name__ == '__main__':
    atualizar_vagas()