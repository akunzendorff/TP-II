# exercicio 1

quantidade = int(input("Digite a quantidade de softwares vendidos: "))
bonus = quantidade * 50
salario = 1500 + bonus

print(f"O valor total do salário é: {salario}")

# exercicio 2

valor = float(input("Insira o valor da prestação: "))
taxa = float(input("Insira o valor da taxa: "))
meses = float(input("Insira a quantidade de meses em atraso: "))

valor = valor + (valor * (taxa / 100) * meses)

print(f"O valor atualizado da prestação é: {valor}")

# exercicio 3

c = float(input("Digite a temperatura em graus Celsius: "))

f = c * 1.8 + 32

print(f"O valor da temperatura em graus Fahrenheit é: {f}")

# exercicio 4

from datetime import datetime

nome = input("Digite seu nome: ")
dataNasc = input("Digite sua data de nascimento (dd/mm/aaaa): ")
dataNasc = datetime.strptime(dataNasc, "%d/%m/%Y")

hoje = datetime.today()

idade = hoje.year - dataNasc.year

if(hoje.month, hoje.day) < (dataNasc.month, dataNasc.day):
    idade -= 1

print(f"{nome}, você tem {idade} anos.")

# exercicio 5

custoFabricacao = float(input("Digite o custo de fabricação do carro: "))

percDistribuidor = custoFabricacao * 28 / 100
percImposto = custoFabricacao * 45 / 100

custoFinal = custoFabricacao + percDistribuidor + percImposto

print(f"O custo final do carro é: {custoFinal}")
