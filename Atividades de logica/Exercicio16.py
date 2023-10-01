print("Maçã R$1,30 a unidade \n 12 por R$1,00 cada")
unidade = int(input("Quantas maçãs você deseja? "))

if unidade == 12:
    duzia = 12
    print("Aqui esta sua duzia de maçãs custando R$12,00")
else:
    valor = 1.30 * unidade
    print(f"Aqui esta suas {unidade} de maçãs, custando R${valor:.2f}")