'''3- Consulta de CEP  
Desenvolva um programa que consulta dados de endereço a partir de um CEP brasileiro. Siga os passos abaixo:

* Solicite ao usuário que digite um CEP (apenas números, sem traço).  
* Acesse a API pública do ViaCEP: "https://viacep.com.br/ws/{cep}/json/".  
* Exiba as seguintes informações: logradouro, bairro, cidade, estado e o próprio CEP.  
* Caso o CEP não exista ou haja erro, informe isso de forma clara ao usuário.  

Dica: Use o módulo `requests` e trate exceções com `try/except`.'''


import requests


def consultar_cep(cep):
    try:
        # Faz a requisição à API do ViaCEP
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        
        # Converte a resposta para JSON
        dados_cep = response.json()
        
        # Verifica se o CEP é válido
        if 'erro' in dados_cep:
            return None
        
        return dados_cep
    
    except requests.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None


cep_usuario = input("Digite um CEP (apenas números, sem traço): ")
dados_endereco = consultar_cep(cep_usuario)

if dados_endereco:
    print(f"Logradouro: {dados_endereco['logradouro']}")
    print(f"Bairro: {dados_endereco['bairro']}")
    print(f"Cidade: {dados_endereco['localidade']}")
    print(f"Estado: {dados_endereco['uf']}")
    print(f"CEP: {dados_endereco['cep']}")

else:
    print("CEP inválido ou não encontrado. Verifique o número e tente novamente.")