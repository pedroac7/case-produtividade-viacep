import requests
import json
import re

def consultar_cep(cep_input):
    """ Endpoint 1: Busca por CEP """
    print(f"\n--- Consultando CEP: {cep_input} ---")
    
    # Remove caracteres não numéricos
    cep_limpo = re.sub(r'\D', '', cep_input)
    
    # Validação de formato para CEP
    if len(cep_limpo) != 8:
        print(f"Erro: O CEP deve ter exatamente 8 dígitos.")
        return

    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
    executar_requisicao(url)

def consultar_endereco(uf, cidade, logradouro):
    """ Endpoint 2: Busca por Endereço (UF/Cidade/Rua) """
    print(f"\n--- Buscando Endereço: {logradouro}, {cidade}-{uf} ---")
    
    # Validação de formato para cidade e logradouro
    if len(cidade) < 3 or len(logradouro) < 3:
        print(f"Erro de Validação: Cidade e Logradouro precisam ter pelo menos 3 caracteres.")
        return

    # Validação de formato para UF
    if len(uf) != 2:
        print("Erro: UF deve conter apenas 2 letras (Ex: RN, SP).")
        return

    url = f"https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json/"
    executar_requisicao(url)

def executar_requisicao(url):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            dados = response.json()
            
            # Tratamento para lista vazia 
            if isinstance(dados, list) and len(dados) == 0:
                print("Resultado: Nenhum endereço encontrado com esses termos.")
                return

            # Tratamento para CEP inexistente 
            if isinstance(dados, dict) and "erro" in dados:
                print("Resultado: CEP válido, mas inexistente na base de dados.")
                return

            print("Sucesso! Retorno da API:")
            print(json.dumps(dados, indent=4, ensure_ascii=False))
        elif response.status_code == 400:
            print("Erro 400: Requisição inválida (verifique se a cidade/rua tem 3+ caracteres).")
        else:
            print(f"Erro na requisição. Status: {response.status_code}")

    except Exception as e:
        print(f"Erro de conexão: {e}")

def menu():
    while True:
        print("\n=== CLIENTE VIACEP  ===")
        print("1. Consultar por CEP")
        print("2. Pesquisar por Endereço")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cep = input("Digite o CEP: ")
            consultar_cep(cep)
        elif opcao == '2':
            uf = input("Digite a UF: ")
            cidade = input("Digite a Cidade: ")
            logradouro = input("Digite o Logradouro (Rua/Av): ")
            consultar_endereco(uf, cidade, logradouro)
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()