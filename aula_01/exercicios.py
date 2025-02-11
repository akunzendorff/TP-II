# exercicio 1
altura = float(input("Digite a sua altura em metros: "))

altura = altura * 100

print(f"A sua altura em centímetros é: {altura}")

# exercicio 2

deslocamento = int(input("Digite a distância percorrida: "))
tempo = int(input("Digite o tempo em segundos: "))

vm = deslocamento / tempo

print(f"A velocidade do objeto é {vm}")

# exercicio 3

import math

raio = float(input("Digite o valor do raio: "))

area = math.pi * raio ** 2

print(f"O valor da área é: {area}")

# exercicio 4

base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))

resposta = float(input("Digite o valor que você obteve: \n"))

area = base * altura / 2

if area == resposta:
    print(f"A sua resposta está correta!\n")
    print(f"O valor da área é: {area}")

else: 
    print(f"A sua resposta está incorreta! Verifique novamente...\n")
    print(f"O valor correto da área é: {area}")

# exercicio 5

valor1 = int(input("Insira o primeiro valor: "))
valor2 = int(input("Insira o segundo valor: "))

adicao = valor1 + valor2
subtracao = valor1 - valor2
multiplicacao = valor1 * valor2
divisao = valor1 / valor2

print(f"\nO resultado da adição dos dois números é: {adicao}")
print(f"O resultado da subtração dos dois números é: {subtracao}")
print(f"O resultado da multiplicação dos dois números é: {multiplicacao}")
print(f"O resultado da divisão dos dois números é: {divisao}")

# exercicio 6

salario = float(input("Insira o valor do seu salário atual: "))
reajuste = float(input("Insira a porcentagem do reajuste: "))

reajuste = salario * reajuste / 100
salario = salario + reajuste

print(f"O valor do novo salário é: {salario}")

# exercicio 7

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

dias = idade * 365

print(f"{nome}, você ja viveu {dias}!")

# exercicio 8

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

soma = n1 + n2 + n3
soma = soma ** 2

print(f"O valor da soma dos números elevado ao quadrado é: {soma}")

# exercicio 9

votosBrancos = int(input("Digite o número de votos em branco: "))
votosNulos = int(input("Digite o número de votos nulos: "))
votosValidos = int(input("Digite o número de votos válidos: "))

totalEleitores = votosBrancos + votosNulos + votosValidos
percBrancos = (votosBrancos * 100) / totalEleitores
percNulos = (votosNulos * 100) / totalEleitores
percValidos = (votosValidos * 100) / totalEleitores

print(f"O percentual de votos em branco é: {percBrancos}")
print(f"O percentual de votos nulos é: {percNulos}")
print(f"O percentual de votos válidos é: {percValidos}")

# exercicio 10
import math

raio = float(input("Digite o valor do raio: "))
altura = float(input("Digite o valor da altura: "))

volume = math.pi * raio ** 2 * altura

print(f"O valor do volume do cilíndro é: {volume}")

# exercicio 11

nome = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade comprada: "))
valor = float(input("Digite o valor unitário: "))

valor = valor * quantidade

print(f"O valor total da compra de {quantidade} unidades do produto {nome}, é de R$ {valor}")

# exercicio 12

alturaParede = float(input("Digite a altura da parede:"))
larguraParede = float(input("Digite a largura da parede:"))
alturaAzuleijo = float(input("Digite a altura do azuleijo:"))
larguraAzuleijo = float(input("Digite a largura do azuleijo:"))

areaParede = alturaParede * larguraParede / 2
areaAzuleijo = alturaAzuleijo * larguraAzuleijo / 2

quantidade = areaParede / areaAzuleijo

print(f"A quantidade de azuleijos necessário pra preencher a parede é: {quantidade}")

