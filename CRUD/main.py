import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "302302",
    database = "academiaturmad"
)
print(banco)

meucursor = banco.cursor()
pesquisa = "select matricula, nome, cpf, telefone from alunos;"
meucursor.execute(pesquisa)
resultado = meucursor.fetchall()

for e in resultado:
    print(e)

# nome1 = "Felipe"
# telefone1 = "81993220878"
# sql = "insert into alunos (nome, telefone) values (%s, %s)"
# data = (nome1, telefone1)
# meucursor.execute(sql, data)
# banco.commit()
genero = "F"
sql = "alter table alunos add colunmn genero;"
sql1 = "insert into alunos (genero) values (%s)"
data = (genero)
meucursor.execute(sql,sql1)
tiposexo1 = "M"
sql = "alter table func add colunmn genero;"
sql1 = "insert into func (genero) values (%s)"
data = (genero1)
meucursor.execute(sql,sql1)
banco.commit()
# userid = meucursor.lastrowid
# print(userid)

meucursor.close()
banco.close()