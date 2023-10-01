#Faça um codigo realize a media entre 4 numeros
soma = 0
cont = 4

for i in range(cont):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma += numero

media = soma / cont
print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media}")