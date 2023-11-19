from funcoes import *

while True:
    opcao = input("Selecione uma das opções abaixo para acessar o banco\n"
                  "1 - Alunos\n"
                  "2 - Modalidades\n"
                  "3 - Funcionários\n"
                  "4 - Personal\n"
                  "-> ")

    while opcao == '1':
        opcao_alunos = input("Bem - Vindo a Tabela Alunos! selecione a opção desejada:\n"
                             "1 - Adicionar\n"
                             "2 - Deletar\n"
                             "3 - Exibir\n"
                             "4 - Voltar\n"
                             "-> ")
        if opcao_alunos == '4':
            break

        elif opcao_alunos == '1':
            nome = str(input("Digite o nome do aluno: "))
            cpf = input("Digite o cpf do aluno: ")
            end = input("Digite o endereço do aluno: ")
            tel = input("Digite o telefone do aluno: ")
            email = str(input("Digite o email do aluno: "))
            cadastrar_aluno(nome, cpf, end, tel, email)
            print("Aluno cadastrado com sucesso!!")

        elif opcao_alunos == '2':
            id_alunos = input("Digite o aluno que deseja deletar: ")
            deletar_alunos(id_alunos)

        elif opcao_alunos == '3':
            exibir_aluno()

        else:
            print("opção invalida!")

    while opcao == '2':
        opcao_Modalidades = input("Bem - Vindo(a) a Tabela Modalidades! selecione a opção desejada:\n"
                                  "1 - Adicionar\n"
                                  "2 - Deletar\n"
                                  "3 - Exibir\n"
                                  "4 - Voltar\n"
                                  "-> ")

        if opcao_Modalidades == '4':
            break

        elif opcao_Modalidades == '1':
            modalidade = input("Digite o nome da modalidade: ")
            cadastrar_modalidade(modalidade)
            print("Modalidade cadastrado com sucesso!!")

        elif opcao_Modalidades == '2':
            id_modalidades = input("Digite a modalidade que deseja deletar: ")
            deletar_modalidades(id_modalidades)

        elif opcao_Modalidades == '3':
            exibir_modalidade()

        else:
            print("opção invalida!")

    while opcao == '3':
        opcao_Funcionarios = input("Bem - Vindo! a Tabela Funcionarios! selecione a opção desejada:\n"
                                   "1 - Adicionar\n"
                                   "2 - Deletar\n"
                                   "3 - Exibir\n"
                                   "4 - Voltar\n"
                                   "-> ")

        if opcao_Funcionarios == '4':
            break

        elif opcao_Funcionarios == '1':
            nome = str(input("Digite o nome do funcionario: "))
            cpf = input("Digite o cpf do funcionario: ")
            departamento = input("Digite o departamento do funcionario: ")
            salario = input("Digite o salario do funcionario: ")
            quantdeFilhos = input("Digite a quantidade de filhos: ")
            cadastrar_funcionarios(nome, cpf, departamento, salario, quantdeFilhos)
            print("Funcionario cadastrado com sucesso!!")

        elif opcao_Funcionarios == '2':
            id_funcionarios = input("Digite o id do funcionario que deseja deletar: ")
            delete_funcionarios(id_funcionarios)

        elif opcao_Funcionarios == '3':
            exibir_funcionarios()

        else:
            print("opção invalida!")

    while opcao == '4':
        opcao_Personal = input("Bem - Vindo a Tabela Personal! selecione a opção desejada:\n"
                               "1 - Adicionar\n"
                               "2 - Deletar\n"
                               "3 - Exibir\n"
                               "4 - Voltar\n"
                               "-> ")
        if opcao_Personal == '4':
            break

        elif opcao_Personal == '1':
            nome = input("Digite o nome do personal: ")
            cpf = input("Digite o cpf do personal: ")
            cref = input("Digite o cref do personal: ")
            tel = input("Digite o telefone do personal: ")
            email = input("Digite o email do personal: ")
            cadastrar_personal(cpf, nome, cref, tel, email)
            print("Personal cadastrado com sucesso!!")

        elif opcao_Personal == '2':
            id_personal = input("Digite o id do personal que deseja deletar: ")
            deletar_personal(id_personal)

        elif opcao_Personal == '3':
            exibir_personal()

        else:
            print("opção invalida!")
    else:
        print("opção invalida!!")
