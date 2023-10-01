#Crie um codigo que leia um numero difertente de zero e diga se ele é positivo ou negativo
numero = float(input("Digite um número, não pode ser 0: "))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número não pode ser zero")