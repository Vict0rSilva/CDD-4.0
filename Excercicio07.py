#Faça um codigo que calculer a area de um triangulo
base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))


if base > 0 and altura > 0:
    area = (base * altura) / 2
    print(f"A área do triângulo é {area}")
else:
    print("Os valores não pode ser negativo.")