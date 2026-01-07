 FreelanceRadar
Um agregador inteligente de vagas de freelancer que coleta automaticamente oportunidades de múltiplas plataformas e as organiza em um dashboard responsivo e intuitivo.
 Funcionalidades

 Dashboard responsivo (mobile first)
 Busca e filtros em tempo real
 Coleta automática de vagas a cada hora
 Persistência de dados com SQLite
 API REST para consulta de vagas
 Design totalmente responsivo com Bootstrap 5
 Automação backend com APScheduler

 Tecnologias Utilizadas
Backend

Flask - Framework web Python
Flask-CORS - Habilitação de CORS
APScheduler - Agendamento de tarefas automáticas
SQLite - Banco de dados leve e embarcado

Frontend

HTML5 - Estrutura semântica
CSS3 - Estilos responsivos
JavaScript Vanilla - Lógica do cliente
Bootstrap 5 - Framework CSS mobile first

 Pré-requisitos

Python 3.8+
pip (gerenciador de pacotes Python)
Navegador moderno

 Instalação e Execução
1. Clonar o repositório
bashgit clone https://github.com/seu-usuario/FreelanceRadar.git
cd FreelanceRadar
2. Criar ambiente virtual
bashpython -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
3. Instalar dependências
bashpip install -r requirements.txt
4. Executar a aplicação
bashcd backend
python app.py
A aplicação estará disponível em: http://localhost:5000
 Estrutura do Projeto
FreelanceRadar/
├── backend/
│   ├── app.py              # Aplicação Flask principal
│   ├── database.py         # Gerenciamento do banco de dados
│   ├── scraper.py          # Lógica de coleta de vagas
│   └── vagas.db            # Banco de dados SQLite
├── frontend/
│   ├── index.html          # Página principal
│   ├── style.css           # Estilos responsivos
│   └── script.js           # Lógica frontend
├── requirements.txt        # Dependências Python
├── .gitignore             # Arquivos ignorados pelo Git
└── README.md              # Este arquivo
Endpoints da API
GET /
Retorna a página principal (index.html)
GET /api/vagas
Retorna todas as vagas em formato JSON
json[
  {
    "id": 1,
    "titulo": "Desenvolvedor Python",
    "plataforma": "Upwork",
    "preco": "R$ 80-150/h",
    "descricao": "Projeto de automação com Python",
    "data": "2026-01-07"
  }
]
GET /api/status
Retorna o status da aplicação
json{
  "status": "online",
  "total_vagas": 12,
  "mensagem": "FreelanceRadar rodando com sucesso"
}
 Automação
O sistema coleta automaticamente novas vagas a cada 1 hora. O scraper simula a coleta de vagas de três plataformas:

Upwork
Workana
Fiverr

Os dados são armazenados em um banco SQLite e servidos através da API REST.
Características do Frontend

Mobile First: Desenvolvido primeiramente para dispositivos móveis
Responsivo: Funciona perfeitamente em tablets e desktops
Filtros Dinâmicos: Busca e filtro por plataforma em tempo real
Animações Suaves: Transições e hover effects
Bootstrap 5: Framework CSS moderno e profissional

 Melhorias Futuras

 Integração com APIs reais de plataformas
 Sistema de autenticação de usuários
 Favoritar vagas
 Notificações por email
 Gráficos de análise de vagas
 Deploy em produção (Heroku, PythonAnywhere, etc)

 Licença
Este projeto está sob a licença MIT. Você é livre para usar, modificar e distribuir.
 Autor
Desenvolvido como projeto de portfólio para demonstrar habilidades em:

Desenvolvimento Full Stack
Automação Backend
Design Responsivo
Versionamento com Git


Desenvolvido  usando Python e JavaScript