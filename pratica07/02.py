'''
2- Escrita de Arquivo CSV  
Crie um programa que escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV. Para isso:

* Crie uma lista de listas com dados fictícios de pelo menos três pessoas.  
* Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.  
* Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.  
* Confirme a gravação exibindo uma mensagem com o nome do arquivo.  
* Trate possíveis erros de escrita de arquivo.

Dica: Use `csv.writer()` para escrever os dados linha por linha.
'''


import csv


def escrever_csv(nome_arquivo, dados):
    try:
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(['Nome', 'Idade', 'Cidade'])  # Cabeçalhos
            escritor.writerows(dados)  # Escreve os dados
        print(f"Dados salvos com sucesso em '{nome_arquivo}'")
    except Exception as e:
        print(f"Erro ao escrever no arquivo: {e}")


def main():
    # Lista de dados fictícios
    dados_pessoas = [
        ['Alice', 30, 'São Paulo'],
        ['Bob', 25, 'Rio de Janeiro'],
        ['Charlie', 28, 'Belo Horizonte']
    ]
    
    # Solicita o nome do arquivo CSV
    nome_arquivo = input("Digite o nome do arquivo CSV (ex: pessoas.csv): ")
    
    # Chama a função para escrever os dados no arquivo CSV
    escrever_csv(nome_arquivo, dados_pessoas)


if __name__ == "__main__": 
    main() 
