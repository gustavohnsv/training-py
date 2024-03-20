import datetime

date = datetime.datetime.now()

hora = date.hour
horario = date.strftime("%H:%M:%S")

if hora < 12:
    msg = "Bom dia,"
elif hora >= 12 and hora < 18:
    msg = "Boa tarde,"
else:
    msg = "Boa noite,"

print("Hora atual:",horario)
nome = input("Qual o seu nome?")
sobrenome = input("Qual o seu sobrenome?")
altura = float(input("Qual a sua altura?"))
peso = float(input("Qual o seu peso?"))

imc = peso/altura**2

if imc < 18.5:
    fisico = "Magreza"
elif imc >= 18.5 and imc < 24.9:
    fisico = "Peso normal"
elif imc >= 25 and imc < 29.9:
    fisico = "Sobrepeso"
elif 30 <= imc < 34.9:
    fisico = "Obesidade grau I"
elif 35 <= imc <= 40:
    fisico = "Obesidade grau II"
elif imc > 40:
    fisico = "Obesidade grau III"

print(msg,nome,sobrenome+"!")
print("Seu Índice de Massa Corporal é de: {:.2f}".format(imc))
print("Seu IMC é considerado:", fisico)