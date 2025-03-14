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

3. 📂 Estrutura do Repositório <br>

    📦 recarga-inteligente <br>
│── 📂 carro/                    # Código do cliente (veículo elétrico) <br>
│   │── cliente.py                # Implementação do cliente <br>
│   │── Dockerfile                 # Configuração para Docker <br>
│   │── requirements.txt           # Dependências do cliente <br>
│   └── tests/                     # Testes do cliente <br>
│       └── test_cliente.py
│
│── 📂 nuvem/                    # Código do servidor central <br>
│   │── servidor.py                # Implementação do servidor <br>
│   │── database.py                # Gerenciamento do banco de dados <br>
│   │── Dockerfile                 # Configuração para Docker <br>
│   │── requirements.txt           # Dependências do servidor <br>
│   └── tests/                     # Testes do servidor<br> 
│       └── test_servidor.py
│
│── 📂 ponto_de_recarga/          # Código da estação de carregamento <br>
│   │── ponto_recarga.py           # Implementação do ponto de recarga <br>
│   │── Dockerfile                 # Configuração para Docker <br>
│   │── requirements.txt           # Dependências do ponto de recarga <br>
│   └── tests/                     # Testes do ponto de recarga <br>
│       └── test_ponto.py
│
│── 📂 docker/                    # Configuração para orquestração de contêineres <br>
│   │── docker-compose.yml         # Arquivo para subir os serviços juntos <br>
│
│── 📂 docs/                      # Documentação do projeto <br>
│   │── README.md                  # Instruções para rodar o projeto <br>
│   │── relatorio.pdf               # Relatório final do projeto <br>
│
│── 📂 scripts/                   # Scripts auxiliares <br>
│   │── start_all.sh               # Script para iniciar todos os serviços <br>
│
│── 📂 tests/                     # Testes gerais do sistema <br>
│   │── test_integration.py        # Testes de integração entre cliente, servidor e ponto <br>
│
│── .gitignore                     # Arquivos a serem ignorados no Git <br>
│── requirements.txt                # Dependências gerais <br>
│── LICENSE                         # Licença do projeto <br>
│── README.md                       # Descrição geral do projeto <br>


     ## 👨‍💻 Equipe <br>
- Discente 1 @rogeriocerqueira <br>
- Discente 2 @jeferson <br>
