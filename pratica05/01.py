'''1- Calculadora de Gorjeta
Crie um programa que calcula o valor da gorjeta a partir do total da conta e da porcentagem escolhida. Use as instruções abaixo:

* Defina o valor da conta (ex: R$ 100,00).  
* Informe a porcentagem da gorjeta (ex: 10%, 15%, 20%).  
* O programa deve calcular o valor correspondente e exibir o resultado com duas casas decimais.'''


valor_conta = float(input("Digite o valor da conta: R$ "))
porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta (ex: 10, 15, 20): "))
gorjeta = valor_conta * (porcentagem_gorjeta / 100)
valor_total = valor_conta + gorjeta

print(f"Valor da gorjeta: R$ {gorjeta:.2f}")
print(f"Valor total da conta com gorjeta: R$ {valor_total:.2f}")



