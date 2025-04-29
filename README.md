# Monitoring System 📈

Sistema simples de monitoramento desenvolvido com Python + FastAPI.  
Este projeto faz parte de um estudo focado em DevOps e boas práticas de desenvolvimento.

## 📦 Tecnologias

- Python 3.11+
- FastAPI
- Docker
- Docker Compose
- GitHub Actions (CI/CD)

## 🚀 Como rodar localmente

### Rodar com Docker Compose

```bash
docker-compose up --build
```

O sistema estará disponível em: http://localhost:8000

### 📚 Endpoints disponíveis

| Método | Rota          | Descrição                                   |
|:------:|:--------------|:--------------------------------------------|
| `GET`  | `/healthcheck` | Retorna o status de saúde da aplicação.     |
| `GET`  | `/metrics`     | Retorna métricas de CPU e memória. |
| `GET`  | `/info`        | Retorna informações do sistema. |

### Exemplo de resposta /healthcheck
```json
{
  "status": "ok",
  "env": "development" // ou "staging" conforme ambiente
}
```
### Exemplo de resposta /metrics
```json
{
  "cpu_usage": "63%",
  "memory_usage": "286MB"
}
```
### Exemplo de resposta /info
```json
{
  "name": "Monitoring System",
  "version": "1.0.0",
  "description": "API de monitoramento de sistema com FastAPI",
  "author": "author"
}
```

### ⚙️ Pipeline CI (GitHub Actions)
- Checkout do repositório.
- Instalação do Docker.
- Build da imagem Docker.
- Inicialização do container.
- Teste de healthcheck automatizado.

| Observação |
|:----------|
| O pipeline é executado automaticamente em pushes e pull requests na branch main. |

### 🌎 Ambientes
- Development (local default)
- Staging (via docker-compose.override.yml)

### Definição de Ambiente
Utilize a variável ENV para configurar o ambiente:
```bash
ENV=staging
AUTHOR_SYSTEM="Autho do Sistema"
VERSION_SYSTEM=1.0.0
DESCRIPTION_SYSTEM="API de monitoramento de sistema com FastAPI"
NAME_SYSTEM="Monitoring System"
```

### 🛠️ Estrutura de pastas
```bash
.
├── app/
│   ├── main.py
│   └── ...
├── tests/
│   ├── test_healthcheck.py
│   └── ...
├── Dockerfile
├── docker-compose.yml
├── docker-compose.override.yml (em breve)
├── .github/
│   └── workflows/
│       └── ci.yml
├── README.md
└── requirements.txt
```