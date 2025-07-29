'''4- Conversor de Moedas (para Reais - BRL)  
Crie um programa que mostra a cotação atual de moedas estrangeiras em relação ao Real. O programa deve:

* Solicitar ao usuário o código da moeda estrangeira (ex: USD, EUR, GBP).  
* Acessar a API: "https://economia.awesomeapi.com.br/last/{moeda}-BRL".  
* Exibir a cotação atual, o valor máximo, o valor mínimo e a data/hora da última atualização.  
* Informar ao usuário se o código da moeda for inválido ou houver falha na conexão.  

Dica: A conversão da data/hora pode ser feita com o módulo `datetime`.'''


import requests
from datetime import datetime

def consultar_cotacao(moeda):
    try:
        # Faz a requisição à API
        response = requests.get(f"https://economia.awesomeapi.com.br/last/{moeda}-BRL")
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

        # Converte a resposta para JSON
        dados_cotacao = response.json()

        # Define a chave correta baseada na moeda
        chave = f"{moeda}BRL"

        # Verifica se a chave existe no dicionário retornado
        if chave not in dados_cotacao:
            return None

        # Extrai os dados da cotação
        cotacao_info = dados_cotacao[chave]
        cotacao_atual = cotacao_info['bid']
        valor_maximo = cotacao_info['high']
        valor_minimo = cotacao_info['low']
        data_hora = datetime.fromisoformat(cotacao_info['create_date'].replace('Z', '+00:00'))

        # Retorna os dados formatados
        return {
            'cotacao_atual': cotacao_atual,
            'valor_maximo': valor_maximo,
            'valor_minimo': valor_minimo,
            'data_hora': data_hora
        }

    except requests.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None

# Entrada do usuário
moeda_usuario = input("Digite o código da moeda estrangeira (ex: USD, EUR): ").upper()
cotacao = consultar_cotacao(moeda_usuario)

# Exibe os resultados
if cotacao:
    print(f"\nCotação atual de {moeda_usuario} em relação ao Real:")
    print(f"Valor Atual: R$ {cotacao['cotacao_atual']}")
    print(f"Valor Máximo: R$ {cotacao['valor_maximo']}")
    print(f"Valor Mínimo: R$ {cotacao['valor_minimo']}")
    print(f"Última Atualização: {cotacao['data_hora'].strftime('%d/%m/%Y %H:%M:%S')}")
else:
    print("\nCódigo de moeda inválido ou não encontrado. Verifique o código e tente novamente.")

