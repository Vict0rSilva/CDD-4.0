import mysql.connector

banco = mysql.connector.connect(
    host ="localhost",
    user="root",
    password="4002",
    database="academia"
)
print(banco)

nome1 = 'bila'
tel1 = '00000000000'
meucursor = banco.cursor()
pesquisar = 'insert into alunos (nome, tel) values(%s,%s);'
data =(nome1,tel1)
meucursor.execute(pesquisar,data)
banco.commit()
userid= meucursor.lastrowid
print(userid)
result = meucursor.fetchall()
for x in result:
    print(x)
meucursor.close()
banco.close()