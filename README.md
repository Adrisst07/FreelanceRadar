FreelanceRadar

Um agregador inteligente de vagas freelancer com coleta automática e dashboard responsivo.


✅ Dashboard responsivo - Funciona em mobile, tablet e desktop
✅ Filtros em tempo real - Busque por título, descrição ou plataforma
✅ 11+ vagas disponíveis - Dados realistas de Upwork, Workana e Fiverr
✅ API REST estruturada - Fácil de integrar com outros projetos
✅ Coleta automática - Atualização a cada 1 hora via APScheduler
✅ Persistência de dados - SQLite para armazenar vagas
✅ Design moderno - Bootstrap 5 com animações suaves
✅ Sem frameworks pesados - JavaScript vanilla no frontend

🛠️ Tecnologias
Backend
Python 3.8+
Flask 2.3.3 - Web framework
APScheduler 3.10.4 - Agendamento automático
SQLite - Banco de dados leve
Frontend
HTML5 - Estrutura semântica
CSS3 - Estilos responsivos
JavaScript Vanilla - Sem dependências desnecessárias
Bootstrap 5 - Framework CSS moderno
 Como Funciona

Scraper coleta vagas das 3 plataformas a cada 1 hora
Backend armazena no banco SQLite
Frontend exibe em dashboard responsivo
Usuário filtra por plataforma ou busca em tempo real

Scraper → Banco de Dados → API REST → Frontend
 Como Usar
Pré-requisitos

Python 3.8 ou superior
pip (gerenciador de pacotes)
Navegador moderno

Instalação Rápida
bash# 1. Clone o repositório
git clone https://github.com/seu-usuario/FreelanceRadar.git
cd FreelanceRadar

# 2. Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # Mac/Linux
# ou
venv\Scripts\activate  # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute a aplicação
cd backend
python app.py
Acesse no navegador
http://localhost:5000
 API - Endpoints
GET /api/vagas
Retorna todas as vagas com paginação
Parâmetros:

page (int): Número da página (padrão: 1)
per_page (int): Vagas por página (padrão: 20)

Resposta:
json{
  "sucesso": true,
  "total": 11,
  "pagina": 1,
  "vagas": [
    {
      "id": 1,
      "titulo": "Desenvolvedor Python Senior",
      "plataforma": "Upwork",
      "preco": "R$ 80-150/h",
      "descricao": "Procuramos desenvolvedor experiente para projeto de automação...",
      "data": "2026-02-01",
      "habilidades": "Python, Flask, PostgreSQL"
    }
  ]
}
GET /api/vagas/<id>
Retorna detalhes de uma vaga específica
GET /api/status
Status da aplicação
Resposta:
json{
  "sucesso": true,
  "status": "online",
  "total_vagas": 11,
  "versao": "1.0.0",
  "mensagem": "FreelanceRadar rodando com sucesso"
}
📁 Estrutura do Projeto
FreelanceRadar/
├── backend/
│   ├── app.py                 # Aplicação Flask principal
│   ├── database.py            # Gerenciamento do SQLite
│   ├── scraper.py             # Coleta de vagas
│   ├── vagas.db               # Banco de dados
│   └── *.backup               # Backups dos arquivos originais
│
├── frontend/
│   ├── index.html             # Página principal
│   ├── style.css              # Estilos responsivos
│   └── script.js              # Lógica do frontend
│
├── requirements.txt           # Dependências Python
├── .gitignore                 # Arquivos ignorados pelo Git
└── README.md                  # Este arquivo
 Funcionalidades Detalhadas
Dashboard

Lista dinâmica de vagas
Cards informativos com:

Título e plataforma
Faixa salarial
Descrição completa
Habilidades necessárias
Data da publicação



Filtros

Busca em tempo real - Filtra por título ou descrição
Filtro por plataforma - Upwork, Workana, Fiverr
Limpar filtros - Volta à exibição completa

Automação

Scraper roda automaticamente a cada 1 hora
Verifica duplicatas antes de inserir
Mantém histórico de vagas
Log de operações

 Dados das Vagas
Cada vaga contém:

Título - Nome da vaga
Plataforma - Upwork, Workana ou Fiverr
Preço - Faixa salarial em R$/h
Descrição - Detalhes da vaga
Habilidades - Tags das skills necessárias
Data - Quando foi publicada

Exemplo de Vaga
json{
  "titulo": "Desenvolvedor Python Senior",
  "plataforma": "Upwork",
  "preco": "R$ 80-150/h",
  "descricao": "Procuramos desenvolvedor experiente para projeto de automação...",
  "habilidades": "Python, Flask, PostgreSQL",
  "data": "2026-02-01"
}
 O que Aprendi
Este projeto demonstra proficiência em:
✅ Full Stack Development

Backend robusto com Flask
Frontend responsivo e moderno
Integração completa frontend-backend

✅ Automação

Agendamento de tarefas com APScheduler
Coleta simulada realista de dados

✅ Boas Práticas

Separação clara de responsabilidades
Código modular e reutilizável
Tratamento de erros robusto
Versionamento com Git

✅ Responsividade

Design mobile-first
Testes em múltiplos dispositivos
CSS moderno e eficiente

✅ Segurança

.gitignore adequado
Sem dados sensíveis no repositório
Debug desativado em produção

 Próximos Passos / Melhorias Futuras

 Integração com APIs reais das plataformas
 Sistema de autenticação de usuários
 Favoritar e salvar vagas
 Notificações por email
 Gráficos de análise (vagas por plataforma, tendências)
 Dark mode
 Deploy em produção (Heroku, Railway, Render)
 Testes automatizados
 Documentação API (Swagger)

 Licença
Este projeto está sob a licença MIT. Você é livre para usar, modificar e distribuir.
Veja o arquivo LICENSE para mais detalhes.


Desenvolvimento Full Stack
Automação com Python
Design Responsivo
Boas práticas de desenvolvimento
Versionamento com Git




Faça um fork do projeto
Crie uma branch para sua feature (git checkout -b feature/AmazingFeature)
Commit suas mudanças (git commit -m 'Add some AmazingFeature')
Faça push para a branch (git push origin feature/AmazingFeature)
Abra um Pull Request

