import mysql.connector
from datetime import date

data = date.today()
dataformatada = ("{}/{}/{}".format(data.day,data.month,data.year))
print("Dia de hoje:",dataformatada)

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='pythondb',
)

cursor =  conexao.cursor()

opcao=input("O que deseja fazer? (INSERT:C SELECT:R UPDATE:U DELETE:D)")
if opcao == "C" or opcao == "c":
    nome=input("Qual o nome para ser inserido?")
    email=input("Qual o email para ser inserido?")
    telefone=input("Qual o telefone para ser inserido?")
    cidade=input("Qual a cidade para ser inserida?")
    datainsert=data
    insert=f'INSERT INTO Clientes (nome, email, telefone, cidade, datainsert) VALUES ("{nome}","{email}","{telefone}","{cidade}","{datainsert}")'
    cursor.execute(insert)
    conexao.commit()
    print("Valores inseridos com sucesso!")
elif opcao == "R" or opcao == "r":
    idCliente=input("Qual o ID do cliente?")
    read=f'SELECT * FROM Clientes WHERE idCliente = "{idCliente}"'
    cursor.execute(read)
    resultado=cursor.fetchall()
    print(resultado)
elif opcao == "D" or opcao == "d":
    idCliente=input("Qual o ID do cliente?")
    delete=f'DELETE FROM Clientes WHERE idCliente = "{idCliente}"'
    cursor.execute(delete)
    conexao.commit()
    print("Valores deletados com sucesso!")


cursor.close()
conexao.close()