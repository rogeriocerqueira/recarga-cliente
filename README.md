# Recarga Inteligente de Veículos Elétricos

Este projeto implementa um sistema distribuído para gerenciar pontos de recarga de veículos elétricos, otimizando o uso da infraestrutura e reduzindo tempos de espera.

## 📋 Requisitos
- Docker
- Python 3.10+
- Conexão com internet

## 🚀 Como executar
1. Clone o repositório:
   git clone https://github.com/seu-usuario/recarga-inteligente-veiculos.git

2. Acesse a pasta do projeto e execute:
   docker-compose up --build

3. 📂 Estrutura do Repositório

    📦 recarga-inteligente
│── 📂 carro/                    # Código do cliente (veículo elétrico)
│   │── cliente.py                # Implementação do cliente
│   │── Dockerfile                 # Configuração para Docker
│   │── requirements.txt           # Dependências do cliente
│   └── tests/                     # Testes do cliente
│       └── test_cliente.py
│
│── 📂 nuvem/                    # Código do servidor central
│   │── servidor.py                # Implementação do servidor
│   │── database.py                # Gerenciamento do banco de dados
│   │── Dockerfile                 # Configuração para Docker
│   │── requirements.txt           # Dependências do servidor
│   └── tests/                     # Testes do servidor
│       └── test_servidor.py
│
│── 📂 ponto_de_recarga/          # Código da estação de carregamento
│   │── ponto_recarga.py           # Implementação do ponto de recarga
│   │── Dockerfile                 # Configuração para Docker
│   │── requirements.txt           # Dependências do ponto de recarga
│   └── tests/                     # Testes do ponto de recarga
│       └── test_ponto.py
│
│── 📂 docker/                    # Configuração para orquestração de contêineres
│   │── docker-compose.yml         # Arquivo para subir os serviços juntos
│
│── 📂 docs/                      # Documentação do projeto
│   │── README.md                  # Instruções para rodar o projeto
│   │── relatorio.pdf               # Relatório final do projeto
│
│── 📂 scripts/                   # Scripts auxiliares
│   │── start_all.sh               # Script para iniciar todos os serviços
│
│── 📂 tests/                     # Testes gerais do sistema
│   │── test_integration.py        # Testes de integração entre cliente, servidor e ponto
│
│── .gitignore                     # Arquivos a serem ignorados no Git
│── requirements.txt                # Dependências gerais
│── LICENSE                         # Licença do projeto
│── README.md                       # Descrição geral do projeto


     ## 👨‍💻 Equipe
- Discente 1 @rogeriocerqueira
- Discente 2 @jeferson
