FROM python:3.12-slim

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos
COPY requirements.txt .
COPY . .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta do FastAPI
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
