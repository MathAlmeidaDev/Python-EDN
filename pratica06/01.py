'''
1- Gerador de Senhas Seguras  
Crie um programa que gera senhas aleatórias com letras, números e caracteres especiais. Siga as instruções abaixo:

* Solicite ao usuário o tamanho da senha desejada (por exemplo: 8, 12, 16 caracteres).  
* A senha gerada deve conter letras maiúsculas, minúsculas, números e símbolos (ex: !@#$%&*).  
* Exiba a senha gerada ao final do programa.  

Dica: Use os módulos `random` e `string` para gerar os caracteres aleatórios.'''

import random
import string


def gerar_senha(tamanho):
    # Define os caracteres que serão usados na senha
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation
    
    # Combina todos os caracteres
    todos_caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos
    
    # Gera a senha aleatória
    senha = ''.join(random.choice(todos_caracteres) for _ in range(tamanho))
    
    return senha

tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
senha_gerada = gerar_senha(tamanho_senha)

print(f"Senha gerada: {senha_gerada}")
