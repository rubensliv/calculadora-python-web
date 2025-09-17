# syntax=docker/dockerfile:1
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PORT=8501

WORKDIR /app

# Dependências do sistema opcionais (comentadas)
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . ./

EXPOSE 8501

CMD ["streamlit", "run", "calculadora_web.py", "--server.address", "0.0.0.0", "--server.port", "8501"]
