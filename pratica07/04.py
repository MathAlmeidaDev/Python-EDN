'''
4- Leitura e Escrita de Arquivo JSON  
Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON. Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo. Para isso:

* Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).  
* Solicite ao usuário o nome do arquivo JSON.  
* Salve os dados no arquivo usando o módulo `json`.  
* Após salvar, leia o mesmo arquivo e imprima os dados carregados.  
* Trate possíveis erros como ausência do arquivo ou problemas na escrita.

Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo.
'''


import json


def salvar_json(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
        print(f"Dados salvos com sucesso em '{nome_arquivo}'")
    except Exception as e:
        print(f"Erro ao escrever no arquivo: {e}")


def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
            dados = json.load(arquivo_json)
            return dados
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: Problema na leitura do arquivo JSON '{nome_arquivo}'.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")


def main():
    # Dicionário com dados de uma pessoa
    dados_pessoa = {
        'nome': 'João',
        'idade': 28,
        'cidade': 'Curitiba'
    }
    
    # Solicita o nome do arquivo JSON
    nome_arquivo = input("Digite o nome do arquivo JSON (ex: pessoa.json): ")
    
    # Salva os dados no arquivo JSON
    salvar_json(nome_arquivo, dados_pessoa)
    
    # Lê os dados do arquivo JSON e exibe
    dados_lidos = ler_json(nome_arquivo)
    if dados_lidos:
        print("Dados lidos do arquivo JSON:")
        print(dados_lidos)


if __name__ == "__main__":
    main()