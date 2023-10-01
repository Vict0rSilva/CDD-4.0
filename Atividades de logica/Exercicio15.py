valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor (diferente do primeiro): "))


while valor1 == valor2:
    print("Os valores são iguais. Por favor, insira valores diferentes.")
    valor2 = float(input("Digite o segundo valor (diferente do primeiro): "))

if valor1 > valor2:
    print(f"Ordem crescente: {valor2}, {valor1}")
else:
    print(f"Ordem crescente: {valor2}, {valor1}")