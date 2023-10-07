user = [""]*2
senha = [""]*2
for i in range(2):
    user[i] = input(f"Digite {i+1}° nome: ")
    senha[i] = input("Digite sua senha: ")

login = input("Digite seu login: ")
passw = input("Digite sua senha: ")

sucesso = False#para verificar

for i in range(2):
    if login == user[i] and passw == senha[i]:
        print("login efetuado")
        sucesso = True#caso a condição seja verdadeira ele ira finalizar
        break

if not sucesso:#caso não seja verdadeira ele ira executar a baixo
    print("login invalido!")