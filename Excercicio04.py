# Solicita ao usuário que insira três números
numero1 = float(input("Digite o 1°número: "))
numero2 = float(input("Digite o 2°número: "))
numero3 = float(input("Digite o 3°número: "))

maior = numero1

if numero2 > maior:
    maior = numero2

if numero3 > maior:
    maior = numero3

print(f"O maior número é {maior}.")