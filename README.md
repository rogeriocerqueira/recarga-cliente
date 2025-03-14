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
│── 📂 carro/                    <br>
│   │── cliente.py               <br>
│   │── Dockerfile               <br>
│   │── requirements.txt         <br>
│   └── tests/                   <br>
│       └── test_cliente.py <br> 
│ <br> 
│── 📂 nuvem/                    <br>
│   │── servidor.py              <br>
│   │── database.py              <br>
│   │── Dockerfile               <br>
│   │── requirements.txt         <br>
│   └── tests/                   <br> 
│       └── test_servidor.py     <br> 
│ <br> 
│── 📂 ponto_de_recarga/    <br>
│   │── ponto_recarga.py    <br>
│   │── Dockerfile          <br>
│   │── requirements.txt    <br>
│   └── tests/              <br>
│       └── test_ponto.py <br> 
│ <br> 
│── 📂 docker/         <br>
│   │── docker-compose.yml      <br>
│
│── 📂 docs/             <br>
│   │── README.md         <br>
│   │── relatorio.pdf     <br>
│ <br> 
│── 📂 scripts/           <br>
│   │── start_all.sh       <br>
│ <br> 
│── 📂 tests/            <br>
│   │── test_integration.py        <br>
│
│── .gitignore                <br>
│── requirements.txt         <br>
│── LICENSE                  <br>
│── README.md                <br>


     ## 👨‍💻 Equipe <br>
- Discente 1 @rogeriocerqueira <br>
- Discente 2 @jeferson <br>
