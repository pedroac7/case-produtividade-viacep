# Produtividade Digital – Integração ViaCEP

Projeto desenvolvido para processo seletivo com foco em consumo de APIs REST utilizando a API pública ViaCEP.

## Formas de integração com a API:
* Script em Python para consulta de CEP e busca de endereço, com validações e tratamento de erros
* Collection no Postman com exemplos de requisições
* Workflow no n8n para automação de consultas

## Estrutura do projeto:
```
case-produtividade-viacep/
├── python/   
│   ├── main.py                                    
│   └── requirements.txt
├── postman/         
│   └── viacep_collection.json                      
├── n8n/             
│   └── workflow.json                          
├── evidencias/                                          
└── README.md
```

## Como executar o script:
Certifique-se de ter o **Python** instalado em sua máquina.

### 1. Instalação
Instale as dependências com:
```bash
pip install -r python/requirements.txt
```

### 2. Execução
Execute o script com:
```bash
python python/main.py
```

### 3. Uso
Ao rodar o script, um menu interativo será exibido no terminal permitindo:
1. Consultar endereço por CEP
2. Pesquisar CEPs por UF, cidade e logradouro

## Ferramentas utilizadas
* Python
* Postman
* n8n
* API ViaCEP
* Git/GitHub

*** 

### Autor: Pedro Cursino
