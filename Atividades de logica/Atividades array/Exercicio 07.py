num = [""]*5
senha = [""]*5
for i in range(5):
    num[i] = input(f"Digite {i+1}° nome: ")
    senha[i] = input("Digite sua senha: ")

for x in range(5):
    print("-------------------|")
    print(f"Usuario: {num[x]} \nSenha: {senha[x]}")
