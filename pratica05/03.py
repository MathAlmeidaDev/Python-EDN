'''3- Calculadora de Desconto em Produto
Desenvolva um programa que aplica um desconto sobre o preço de um produto. O programa deve:

* Solicitar o preço original do produto.  
* Solicitar o percentual de desconto desejado.  
* Calcular e exibir o preço final com desconto, arredondado para duas casas decimais.'''

preco_original = float(input("Digite o preço original do produto: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto desejado: "))
desconto = (percentual_desconto / 100) * preco_original
preco_final = preco_original - desconto

print(f"O preço final com desconto é: R$ {preco_final:.2f}")
print(f"Desconto aplicado: R$ {desconto:.2f}")
print(f"Percentual de desconto: {percentual_desconto}%")
print(f"Preço original: R$ {preco_original:.2f}")