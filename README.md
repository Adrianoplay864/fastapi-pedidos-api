🍕 API de Pedidos com FastAPI

API backend desenvolvida em FastAPI, simulando um sistema real de pedidos (ex: pizzaria).
O projeto contempla autenticação de usuários, criptografia de senhas, persistência em banco de dados, migrations, containerização com Docker e boas práticas de backend.

Projeto desenvolvido com foco em portfólio profissional e preparação para vagas Backend Júnior (Python).

🚀 Tecnologias Utilizadas

Python 3.12

FastAPI

SQLAlchemy

SQLite

Pydantic

Alembic

Passlib + bcrypt

JWT (implementação simples)

Uvicorn

Python-dotenv

Docker

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
├── Dockerfile             # Containerização da aplicação
├── requirements.txt       # Dependências com versões fixadas
└── README.md

🔐 Funcionalidades
👤 Usuários

Criação de usuários

Criptografia de senha com bcrypt

Login com validação de credenciais

Geração de token de acesso

📦 Pedidos

Criação de pedidos vinculados a usuários

Status inicial automático (PENDENTE)

Persistência no banco de dados

🔑 Autenticação

Senhas armazenadas de forma segura com Passlib + bcrypt

Validação por email e senha

Retorno de token de autenticação (modelo inicial)

🗄️ Banco de Dados

Banco de dados SQLite

ORM com SQLAlchemy

Controle de versão do banco com Alembic (migrations)

⚠️ Observação sobre Compatibilidade

As versões das bibliotecas passlib e bcrypt foram fixadas propositalmente no requirements.txt para evitar problemas conhecidos de incompatibilidade entre essas dependências.

Isso garante estabilidade tanto em ambiente local quanto em Docker.

⚙️ Como Executar o Projeto (Local)
1️⃣ Clone o repositório
git clone https://github.com/Adrianoplay864/fastapi-pedidos-api.git

2️⃣ Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3️⃣ Instale as dependências
pip install -r requirements.txt

4️⃣ Execute a aplicação
uvicorn main:app --reload

🐳 Como Executar com Docker
docker build -t fastapi-pedidos-api .
docker run -p 8000:8000 fastapi-pedidos-api


Acesse:
👉 http://localhost:8000/docs

📌 Rotas Principais
🔐 Autenticação
Método	Rota	Descrição
POST	/auth/criar_usuario	Criar novo usuário
POST	/auth/login	Login do usuário
📦 Pedidos
Método	Rota	Descrição
POST	/order/pedido	Criar novo pedido
📖 Documentação Automática

Swagger UI:
👉 http://127.0.0.1:8000/docs

ReDoc:
👉 http://127.0.0.1:8000/redoc

🎯 Objetivo do Projeto

Este projeto demonstra conhecimento prático em:

Desenvolvimento de APIs REST com FastAPI

Autenticação e segurança de senhas

Uso de ORM e migrations

Organização de código em camadas

Containerização com Docker

Boas práticas para projetos backend profissionais

👨‍💻 Autor

Adriano Heiderscheidt
Backend Developer | Python | FastAPI | SQLAlchemy

🔗 GitHub: https://github.com/Adrianoplay864