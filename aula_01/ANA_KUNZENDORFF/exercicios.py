# # exercicio 1

# quantidade = int(input("Digite a quantidade de softwares vendidos: "))
# bonus = quantidade * 50
# salario = 1500 + bonus

# print(f"O valor total do salário é: {salario}")

# # exercicio 2

# valor = float(input("Insira o valor da prestação: "))
# taxa = float(input("Insira o valor da taxa: "))
# meses = float(input("Insira a quantidade de meses em atraso: "))

# valor = valor + (valor * (taxa / 100) * meses)

# print(f"O valor atualizado da prestação é: {valor}")

# # exercicio 3

# c = float(input("Digite a temperatura em graus Celsius: "))

# f = c * 1.8 + 32

# print(f"O valor da temperatura em graus Fahrenheit é: {f}")

# exercicio 4

from datetime import date

nome = input("Digite seu nome: ")
dataNasc = int(input("Digite sua data de nascimento: "))

idade = date.today() - dataNasc

print(f"{nome}, você tem {idade} anos.")