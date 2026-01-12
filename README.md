🍕 API de Pedidos com FastAPI

API backend desenvolvida em FastAPI para gerenciamento de usuários e pedidos, simulando o funcionamento de um sistema de pedidos (ex: pizzaria).
O projeto inclui autenticação, criptografia de senha, persistência em banco de dados e organização em camadas.

🚀 Tecnologias Utilizadas

Python 3.12

FastAPI

SQLAlchemy

SQLite

Pydantic

Alembic

Passlib (bcrypt)

JWT (simples)

Uvicorn

Python-dotenv

📁 Estrutura do Projeto
├── main.py                # Inicialização da aplicação
├── models.py              # Models do banco de dados (SQLAlchemy)
├── schemas.py             # Schemas Pydantic
├── dependencies.py        # Dependências (Session DB)
├── auth_routes.py         # Rotas de autenticação
├── order_routes.py        # Rotas de pedidos
├── banco.db               # Banco SQLite
├── alembic.ini            # Configuração do Alembic
├── env.py                 # Configuração das migrations
└── README.md

🔐 Funcionalidades
👤 Usuários

Criar usuário

Criptografia de senha com bcrypt

Login com validação de credenciais

Geração de token de acesso

📦 Pedidos

Criar pedidos vinculados a usuários

Status inicial automático (PENDENTE)

Persistência no banco de dados

🔑 Autenticação

Senhas criptografadas usando Passlib + bcrypt

Validação de login por email e senha

Geração de token simples para autenticação

🗄️ Banco de Dados

SQLite

ORM com SQLAlchemy

Migrations gerenciadas com Alembic

⚙️ Como Executar o Projeto
1️⃣ Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

2️⃣ Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3️⃣ Instale as dependências
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-dotenv python-jose[cryptography]

4️⃣ Execute a aplicação
uvicorn main:app --reload

📌 Rotas Principais
🔐 Autenticação
Método	Rota	Descrição
POST	/auth/criar_usuario	Criar novo usuário
POST	/auth/login	Login do usuário
📦 Pedidos
Método	Rota	Descrição
POST	/order/pedido	Criar novo pedido
📖 Documentação Automática

Após iniciar o servidor, acesse:

Swagger UI:
👉 http://127.0.0.1:8000/docs

ReDoc:
👉 http://127.0.0.1:8000/redoc

🎯 Objetivo do Projeto

Projeto desenvolvido com foco em:

Prática de backend com FastAPI

Organização de código em camadas

Autenticação e segurança básica

Uso profissional de ORM e migrations

Preparação para vagas Backend Júnior

👨‍💻 Autor

Adriano Heiderscheidt
Backend Developer | Python | FastAPI | SQLAlchemy

🔗 GitHub: https://github.com/Adrianoplay864