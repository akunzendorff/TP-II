# # 1. Faça um Programa que verifique se uma letra digitada é consoante ou vogal.

# letra = input("Digite uma letra: ").lower

# match letra:
#     case 'a' | 'e' | 'i' | 'o' | 'u':
#         print(f"A letra digitada foi {letra}, e é uma vogal.")
#     case _:
#         print(f"A letra digitada foi {letra}, e é uma consoante.")

# # ------------------------------------------------------------------------------

# # 2. A Secretaria de Meio Ambiente, que controla o índice de poluição, mantém três grupos de indústrias que são altamente poluentes do meio ambiente. A tabela a seguir indica a ação a ser tomada pela Secretaria de acordo com o índice de poluição , leia o índice de poluição:
# # Ação Índice de Poluição
# # Considerar Aceitável 0 até 2
# # Suspender Atividades Grupo1 3 até 5
# # Suspender Atividades Grupo 1 e 2 6 até 7
# # Suspender atividade de todos grupos Acima de 8


# indice = int(input("Digite o índice de poluição: "))

# match indice:
#     case indice if indice >= 0 and indice <= 2:
#         print("O índice de poluição é aceitável.")
#     case indice if indice >= 3 and indice <= 5:
#         print("Suspender atividades do grupo 1.")
#     case indice if indice >= 6 and indice <= 7 :
#         print("Suspender atividades do grupo 1 e 2.")
#     case indice if indice >= 8:
#         print("Suspender atividades de todos os grupos.")

# # ------------------------------------------------------------------------------

# # 3. Observe a fórmula: U=R * i, onde,
# # U é a Tensão (em V),
# # R é a Resistência (em Ώ)
# # i é a Corrente (em A).
# # Construa um programa que apresente o seguinte menu e realize os cálculos:
# # **************** CÁLCULO DE GRANDEZAS ELÉTRICAS **********
# # 1. Tensão (em Volt) -------------- U = R * i
# # 2. Resistência (em Ohm) -------------- R = U / i
# # 3. Corrente (em Ampére) -------------- i= U / R
# # ******************* ************************************************

# print("Escolha uma opção para calcular:\n")
# print("1. Calcular a tensão elétrica em Volt.")
# print("2. Calcular a resistência elétrica em Ohm.")
# print("1. Calcular a corrente elétrica em Ámpere.")

# opcao = int(input("\nDigite o número da opção escolhida: "))

# match opcao:
#     case 1:
#         R = float(input("Insira o valor da resistência elétrica em ohm: "))
#         i = float(input("Insira o valor da corrente elétrica em ámpere: "))
#         U = R * i
#         print(f"A tensão elétrica é {U}")

#     case 2:
#         U = float(input("Insira o valor da tensão elétrica em volt: "))
#         i = float(input("Insira o valor da corrente elétrica em ámpere: "))
#         R = U / i
#         print(f"A resistência elétrica é {R}")

#     case 3:
#         U = float(input("Insira o valor da tensão elétrica em volt: "))
#         R = float(input("Insira o valor da resistência elétrica em ohm: "))
#         i = U / R
#         print(f"A corrente elétrica é {i}")

# # ------------------------------------------------------------------------------

# # 4. Na última Black Friday, o gerente de uma loja de perfumes colocou todo o seu estoque em promoção, de acordo com a tabela a seguir:
# # Construa um programa que solicite ao operador do caixa o preço total da compra, bem como a forma de pagamento. Ao fim, o programa deve informar o valor da compra e valor final a ser pago com desconto

# total = int(input("Digite o valor total da compra: "))

# print("\nEscolha uma opção de forma de pagamento.\n")
# print("1. À vista (em espécie)")
# print("2. Cartão de débito")
# print("3. Cartão de crédito")

# pagamento = int(input("\nDigite o código da forma de pagamento:"))

# match pagamento:
#     case 1:
#         porcentagem = (total * 15) / 100
#         total = total - porcentagem
#         print(f"O desconto é de {porcentagem}. O novo valor total é {total}")
#     case 2:
#         porcentagem = (total * 10) / 100
#         total = total - porcentagem
#         print(f"O desconto é de {porcentagem}. O novo valor total é {total}")
#     case 3:
#         porcentagem = (total * 5) / 100
#         total = total - porcentagem
#         print(f"O desconto é de {porcentagem}. O novo valor total é {total}")


# # ------------------------------------------------------------------------------

# # 5. Faça um algoritmo que leia a categoria e salário de um Empregado. A empresa irá dar um aumento de salário aos seus funcionários de acordo com a categoria de cada empregado. O aumento seguirá a seguinte regra: 
# # Funcionários das categorias A ganharão 10% de aumento sobre o salário
# # Funcionários das categorias B ganharão 15% de aumento sobre o salário
# # Funcionários das categorias C ganharão 25% de aumento sobre o salário
# # Mostre o salário atual e salário com aumento

# categoria = input("Digite a categoria do funcionário: ").lower()
# salario = int(input("Digite o valor do salário do funcionário: "))

# match categoria:
#     case 'a':
#         porcentagem = (salario * 10) / 100
#         salario = salario + porcentagem
#         print(f"O aumento do salário é de {porcentagem}, e o novo valor total do salário é de {salario}")
#     case 'b':
#         porcentagem = (salario * 15) / 100
#         salario = salario + porcentagem
#         print(f"O aumento do salário é de {porcentagem}, e o novo valor total do salário é de {salario}")
#     case 'c':
#         porcentagem = (salario * 25) / 100
#         salario = salario + porcentagem
#         print(f"O aumento do salário é de {porcentagem}, e o novo valor total do salário é de {salario}")

# # ------------------------------------------------------------------------------

# # 6. Escreva um programa que leia um peso de uma pessoa na Terra e o número de um planeta e mostre o valor do seu peso neste planeta. A relação de planetas é dada a seguir juntamente com o valor das gravidades relativas á Terra:
# # peso = pesodapessoa * gravidade

# peso_pessoa = int(input("Digite o seu peso na Terra: "))

# print("\nEscolha uma opção de planeta.\n")
# print("1. Mercúrio")
# print("2. Vênus")
# print("3. Marte")
# print("4. Júpiter")
# print("5. Saturno")

# planeta = int(input("\nDigite o código do planeta: \n"))

# match planeta:
#     case 1:
#         peso = peso_pessoa * 0.37
#         print(f"Seu peso em Mercúrio é {peso}")
#     case 2:
#         peso = peso_pessoa * 0.88
#         print(f"Seu peso em Vênus é {peso}")
#     case 3:
#         peso = peso_pessoa * 0.38
#         print(f"Seu peso em Marte é {peso}")
#     case 4:
#         peso = peso_pessoa * 2.64
#         print(f"Seu peso em Júpiter é {peso}")
#     case 5:
#         peso = peso_pessoa * 1.15
#         print(f"Seu peso em Saturno é {peso}")



# # ----------------------------------------------------------------------------