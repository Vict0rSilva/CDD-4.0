import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="4002",
    database="academia"
)


def cadastrar_aluno(nome, cpf, end, tel, email):
    meucursor = banco.cursor()
    inserir = 'INSERT INTO alunos (nome, cpf, end, tel, email) VALUES (%s, %s, %s, %s, %s)'
    data = (nome, cpf, end, tel, email)
    meucursor.execute(inserir, data)
    banco.commit()


def cadastrar_funcionarios(nome, cpf, departamento, salario, filhos):
    meucursor = banco.cursor()
    inserir = 'INSERT INTO func (nome, cpf, departamento, salario, quantidade_filhos) VALUES (%s, %s, %s, %s, %s)'
    data = (nome, cpf, departamento, salario, filhos)
    meucursor.execute(inserir, data)
    banco.commit()


def cadastrar_modalidade(modalidade):
    meucursor = banco.cursor()
    inserir = 'INSERT INTO modalidades (nome) values (%s)'
    data = (modalidade,)
    meucursor.execute(inserir, data)
    banco.commit()


def cadastrar_personal(cpf, nome, cref, tel, email):
    meucursor = banco.cursor()
    inserir = 'INSERT INTO personal (cpf, nome, cref, tel, email) VALUES (%s, %s, %s, %s, %s)'
    data = (cpf, nome, cref, tel, email)
    meucursor.execute(inserir, data)
    banco.commit()


def deletar_alunos(id_aluno):
    meucursor = banco.cursor()
    delet = f"delete from alunos where matricula = {id_aluno}"
    meucursor.execute(delet)
    banco.commit()


def deletar_personal(id_personal):
    meucursor = banco.cursor()
    delet = f"delete from personal where cpf = {id_personal}"
    meucursor.execute(delet)
    banco.commit()


def delete_funcionarios(id_funcionario):
    meucursor = banco.cursor()
    delet = f"delete from func where id_funcionario = {id_funcionario}"
    meucursor.execute(delet)
    banco.commit()


def deletar_modalidades(id_modalidade):
    meucursor = banco.cursor()
    delet = f"delete from modalidades where id_mod = {id_modalidade}"
    meucursor.execute(delet)
    banco.commit()


def exibir_modalidade():
    meucursor = banco.cursor()
    pesquisar = 'SELECT * FROM MODALIDADES;'
    meucursor.execute(pesquisar)
    result = meucursor.fetchall()
    for x in result:
        print(x)
    banco.commit()


def exibir_aluno():
    meucursor = banco.cursor()
    pesquisar = 'SELECT * FROM ALUNOS;'
    meucursor.execute(pesquisar)
    result = meucursor.fetchall()
    for x in result:
        print(x)
    banco.commit()


def exibir_funcionarios():
    meucursor = banco.cursor()
    pesquisar = 'SELECT * FROM FUNCIONARIOS;'
    meucursor.execute(pesquisar)
    result = meucursor.fetchall()
    for x in result:
        print(x)
    banco.commit()


def exibir_personal():
    meucursor = banco.cursor()
    pesquisar = 'SELECT * FROM PERSONAL;'
    meucursor.execute(pesquisar)
    result = meucursor.fetchall()
    for x in result:
        print(x)
    banco.commit()
