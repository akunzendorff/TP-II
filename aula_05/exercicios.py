# 1)Ler o ano atual e o ano de nascimento de uma  pessoa. Calcular a idade. Escrever uma mensagem  que diga se ela poderá ou não votar este ano, se ele  tiver mais de 16 anos →USE IF

ano_atual = int(input("Digite o ano atual: "))
ano_nasc = int(input("Digite o ano do seu nascimento: "))

if ano_atual - ano_nasc >= 16:
    print("Você tem mais de 16 anos e pode votar.")
else:
    print("Você tem menos que 16 anos e ainda não pode votar.")

# -------------------------------------------------------------------------------------------------------------------------------------

# 2) Faça um programa que leia a medida em metros e faça uma  conversão , e apresente um menu para conversão “ 1- decímetros 2- Centímetros 3- Milimetros “ , Lembrando:
# decímetros – 10.0
# centímetros – 100.0 
# milímetros – 1000.0 
# Exemplo: case 1: decímetros = metros * 10.0 → USE CASE

print("**CONVERSÃO DE MEDIDAS**")

metros = int(input("Digite um valor em metros: "))

print("1 - Decímetros\n")
print("2 - Centímetros\n")
print("3 - Milímetros\n")

escolha = int(input("Digite o valor de sua escolha: "))

match escolha:
    case 1:
        decimetros = metros * 10.0
        print(f"O valor convertido para decímetros é: {decimetros}")
    case 2:
        centimetros = metros * 100.0
        print(f"O valor convertido para centímetros é: {centimetros}")
    case 3:
        milimetros = metros * 1000.0
        print(f"O valor convertido para milímetros é: {milimetros}")

# -------------------------------------------------------------------------------------------------------------------------------------

# 3) Construa um programa que LEIA dois números reais e leia dos seguintes símbolos: +, -, * ou /, de acordo com símbolo escolhido deverá ser feita a operação.  O referido programa deve retornar o resultado da operação selecionada. 
# Exemplo: case “+”: soma = numero1 + numero2 → USE CASE

numero1 = int(input("Digite um número real: "))
numero2 = int(input("Digite outro número real: "))
simbolo = input("Digite um símbolo: ( * | - | + | / )")

match simbolo:
    case '+':
        soma = numero1 + numero2
        print(f"A soma dos valores inseridos é: {soma}")
    case '-':
        subtracao = numero1 - numero2
        print(f"A subtração dos valores inseridos é: {subtracao}")
    case '*':
        multiplicacao = numero1 * numero2
        print(f"A multiplicação dos valores inseridos é: {multiplicacao}")
    case '/':
        divisao = numero1 / numero2
        print(f"A divisão dos valores inseridos é: {divisao}")

# -------------------------------------------------------------------------------------------------------------------------------------

# 4) Faça um algoritmo e que leia dois números e apresente a subtração do maior pelo menor número. →USE IF

numero1 = int(input("Digite um número real: "))
numero2 = int(input("Digite outro número real: "))

if numero1 < numero2:
    subtracao = numero2 - numero1
    print(f"O resultado da subtração do maior número pelo menor é: {subtracao}")

elif numero1 > numero2:
    subtracao = numero1 - numero2
    print(f"O resultado da subtração do maior número pelo menor é: {subtracao}")

else:
    print("Os dois números são iguais")

# -------------------------------------------------------------------------------------------------------------------------------------

# 5) Elabore um algoritmo que leia o nome e altura e idade de duas pessoas e mostre os dados da pessoa mais alta. → USE IF

nome1 = input("Digite o nome da primeira pessoa: ")
altura1 = int(input("Digite a altura da primeira pessoa:"))
idade1 = int(input("Digite a idade da primeira pessoa:"))

nome2 = input("Digite o nome da segunda pessoa: ")
altura2 = int(input("Digite a altura da segunda pessoa:"))
idade2 = int(input("Digite a idade da segunda pessoa:"))

if altura1 < altura2:
    print(f"{nome2}, tem {idade2} anos e é maior que {nome1}.")

elif altura1 > altura2:
    print(f"{nome1}, tem {idade1} anos e é maior que {nome2}.")


# -------------------------------------------------------------------------------------------------------------------------------------

# 6) Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da compra for menor que R$ 20,00; caso contrário, o lucro será de 30%. Elabore um algoritmo que leia o valor da compra e mostre o valor de venda para o produto. →USE IF

valor_compra = float(input("Digite o valor da compra: "))

if valor_compra < 20.0:
    lucro = valor_compra * 0.45
    print(f"O valor de venda do produto com 45% de lucro é de R${valor_compra + lucro}")
else:
    lucro = valor_compra * 0.3
    print(f"O valor de venda do produto com 30% de lucro é de R${valor_compra + lucro}")    

# -------------------------------------------------------------------------------------------------------------------------------------

# 7) Faça um algoritmo para ler: nome do cliente, valor do depósito. Calcular e escrever o saldo atual (saldoatual = 800 + deposito). Também testar se saldo atual igual a zero escrever a mensagem 'SaldoLimite', se for acima de zero escrever a mensagem ‘Saldo Positivo’ senão escrever a mensagem 'Saldo Negativo'. Mostre nome do cliente , valor do saldo atual. →USE IF

nome_cliente = input("Digite o nome do cliente: ")
valor_deposito = float(input("Digite o valor do depósito: "))

saldo_atual = 800 + valor_deposito

if saldo_atual == 0:
    print(f"O saldo do cliente {nome_cliente} está no limite! \nSaldo = R${saldo_atual}")

elif saldo_atual > 0:
    print(f"O saldo do cliente {nome_cliente} está positivo! \nSaldo = R${saldo_atual}")

else:
    print(f"O saldo do cliente {nome_cliente} está negativo! \nSaldo = R${saldo_atual}")
