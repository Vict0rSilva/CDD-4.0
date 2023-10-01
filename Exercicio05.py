#Crie um algoritmo que leia um numero e diga se ele é par ou impar
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")