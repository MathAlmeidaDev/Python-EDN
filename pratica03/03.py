'''3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.'''

temperatura = float(input("Digite a temperatura: "))

unidade_origem = input("Digite a unidade de origem (C para Celsius, F para Fahrenheit, K para Kelvin): ").strip().upper()
unidade_destino = input("Digite a unidade de destino (C para Celsius, F para Fahrenheit, K para Kelvin): ").strip().upper()

if unidade_origem not in ['C', 'F', 'K'] or unidade_destino not in ['C', 'F', 'K']:
    print("Unidade de temperatura inválida.")

else:
    if unidade_origem == 'C':
        if unidade_destino == 'F':
            temperatura_convertida = (temperatura * 9/5) + 32
        elif unidade_destino == 'K':
            temperatura_convertida = temperatura + 273.15
        else:
            temperatura_convertida = temperatura

    elif unidade_origem == 'F':
        if unidade_destino == 'C':
            temperatura_convertida = (temperatura - 32) * 5/9
        elif unidade_destino == 'K':
            temperatura_convertida = (temperatura - 32) * 5/9 + 273.15
        else:
            temperatura_convertida = temperatura

    elif unidade_origem == 'K':
        if unidade_destino == 'C':
            temperatura_convertida = temperatura - 273.15
        elif unidade_destino == 'F':
            temperatura_convertida = (temperatura - 273.15) * 9/5 + 32
        else:
            temperatura_convertida = temperatura

    print(f"A temperatura convertida é: {temperatura_convertida:.2f} {unidade_destino}")