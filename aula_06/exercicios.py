# #  1 - Crie um vetor que leia 10 posições de números inteiros, armazene os valores e mostre-os.

# vetor = []
 
# for i in range(10):
#     numero = int(input(f"Digite o número da posição {i + 1}: "))
#     vetor.append(numero)

# print(vetor)

# ----------------------------------------------------------------------------------------------------------------

# #  2 - Crie uma matriz[4,4] de inteiros que leia 16 valores, conte e escreva quantos valores maiores que 10 a matriz possui.

# matriz = []
# numeros_maiores_10 = 0

# for j in range(4):
#     vetor = []
#     for i in range(4):
#         numero = int(input(f"Digite o valor da posição ({i}, {j}): "))

#         if numero > 10:
#             numeros_maiores_10 += 1

#         vetor.append(numero)
    
#     matriz.append(vetor)

# print(f"A quantidade de números maiores que 10 na matriz é: {numeros_maiores_10}")


# for i in range(len(matriz)):
#     print(matriz[i])

# ----------------------------------------------------------------------------------------------------------------

# # 3 - Leia 6 nomes de Capitais do Brasil e guarde numa matriz[2,3], e mostre todas as Capitais.

# capitais = []

# for j in range(2):
#     capital = []
#     for i in range(3):
#         nome = input("Digite o nome da capital de um estado do Brasil:  ")
#         capital.append(nome)

#     capitais.append(capital)

# for capital in capitais:
#     print(capital)

# ----------------------------------------------------------------------------------------------------------------

# #  4 - Crie um vetor para ler 5 cores mostre as cores armazenadas no vetor

# cores = []

# for i in range(5):
#     cor = input("Digite uma cor: ")
#     cores.append(cor)

# print(cores)

# ----------------------------------------------------------------------------------------------------------------

# # 5 - Crie um vetor para digitar nomes de Times de Futebol, sem especificar o tamanho do vetor e mostrar os nomes dos times no final.

# times = []
# quantidade = int(input("Insira a quantidade de times de futebol a serem digitados: "))

# for i in range(quantidade):
#     time = input("Digite o nome de um time de futebol: ")
#     times.append(time)

# for i in times:
#     print(i)

# ----------------------------------------------------------------------------------------------------------------

# #  6 - Crie um vetor que leia valores inteiros, e mostre os valores armazenados , e mostre quais são pares.

# inteiros = []
# pares = []

# quantidade = int(input("Insira a quantidade de numeros a serem digitados: "))

# for i in range(quantidade):
#     inteiro = int(input("Digite um número inteiro: "))

#     inteiros.append(inteiro)

#     if inteiro % 2 == 0:
#         pares.append(inteiro)

# print("**Números digitados**")
# for inteiro in inteiros:
#     print(f" - {inteiro}")

# print("\n**Números pares digitados**")
# for par in pares:
#     print(f" - {par}")

# ----------------------------------------------------------------------------------------------------------------

# # 7 - Crie uma matriz[5,2] leia 10 posições de números inteiros,armazene os valores e mostre.

# matriz = []

# for i in range(5):
#     vetor = []

#     for j in range(2):

#         inteiro = int(input("Digite um número inteiro: "))
#         vetor.append(inteiro)

#     matriz.append(vetor)

# print("****Valores inseridos***")

# for i in range(len(matriz)):n
#     print(f"Linha {i + 1}: {matriz[i]}")

# ----------------------------------------------------------------------------------------------------------------

# # 10 - Crie uma matriz, que leia 5 produtos e sua quantidade, e coloque em matriz[5,2], na primeira coluna armazena o nome produto e na segunda coluna a quantidade.

# matriz = []

# for i in range(5):
#     vetor = []

#     produto = input("Digite um produto: ")

#     quantidade = input("Digite a quantidade: ")

#     vetor.append(produto)
#     vetor.append(quantidade)

#     matriz.append(vetor)

# print("***Produtos inseridos***")

# for i in range(len(matriz)):
#     print(f"Linha {i + 1}: Produto: {matriz[i][0]} | Quantidade: {matriz[i][1]}")
