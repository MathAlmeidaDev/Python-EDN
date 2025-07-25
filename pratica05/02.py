'''2- Verificador de Palíndromos
Crie um programa que verifica se uma palavra ou frase é um palíndromo, ou seja, se pode ser lida da mesma forma de trás para frente, desconsiderando espaços, acentos e pontuação. Para isso:

*Solicite ao usuário uma palavra ou frase.
*Desconsidere letras maiúsculas, espaços e sinais de pontuação.
*Verifique se a frase é um palíndromo.
*Exiba "Sim" se for palíndromo ou "Não" se não for.

Exemplo: A frase "A cara rajada da jararaca" deve ser reconhecida como um palíndromo.
'''

import re


def verificar_palindromo(frase):
    # Remove espaços, pontuação e converte para minúsculas
    frase_limpa = re.sub(r'[\W_]', '', frase.lower())
    # Verifica se a frase é igual à sua reversa
    return frase_limpa == frase_limpa[::-1]

frase_usuario = input("Digite uma palavra ou frase: ")
if verificar_palindromo(frase_usuario):
    print("Sim, é um palíndromo.")
else:
    print("Não, não é um palíndromo.")
