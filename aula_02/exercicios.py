# # 1. Construa um programa que receba o peso de duas pessoas e diga qual a pessoa mais pesada, e verifica se as pessoas tem o mesmo peso.

# peso1 = int(input("Digite o peso da primeira pessoa: "))
# peso2 = int(input("Digite o peso da segunda pessoa: "))

# if peso1 > peso2:
#     print(f"O pessoa mais pesada é a primeira pessoa, que pesa {peso1} quilos.")
# elif peso1 < peso2:
#     print(f"O pessoa mais pesada é a segunda pessoa, que pesa {peso2} quilos.")
# elif peso1 == peso2:
#     print(f"As duas pessoas tem o mesmo peso, que é {peso1} quilos.")

# -------------------------------------------------------------------------------

# # 2. Construa um programa que receba um número inteiro positivo informado pelo usuário. Caso ele seja par, o programa deve calcular o seu quadrado. Mas, se ele for ímpar, deve ser calculado o seu cubo. Ao fim, o programa deve mostrar o valor calculado e dizer se o número é impar ou par.

# numero = int(input("Digite um número inteiro positivo: "))

# if numero % 2 == 0:
#     quadrado = numero ** 2
#     print(f"O número digitado é par, e o seu valor ao quadrado é {quadrado}.")
# elif numero % 2 == 1:
#     cubo = numero ** 3
#     print(f"O número digitado é ímpar, e o seu valor ao cubo é {cubo}.")

# -------------------------------------------------------------------------------

# # 3. Escreva um programa que solicite ao usuário a estatura de 3 pessoas. Ao fim, o programa deve mostrar as estaturas em ordem decrescente.

# estatura1 = float(input("Digite a estatura da primeira pessoa (em metros): "))
# estatura2= float(input("Digite a estatura da segunda pessoa (em metros): "))
# estatura3 = float(input("Digite a estatura da terceira pessoa (em metros): "))

# estaturas = [estatura1, estatura2, estatura3]

# estaturas.sort(reverse= True)

# print("\nEstaturas em ordem decrescente: \n")

# for estatura in estaturas:
#     print(f"{estatura} metros.")

# -------------------------------------------------------------------------------

# # 4. Construa um programa que solicite ao usuário dois números positivos. Em seguida, o programa deve apresentar o seguinte menu.
# # 1 Média ponderada, com pesos 2 e 3, respectivamente
# # 2. Quadrado da soma dos 2 números
# # 3. Cubo do menor número Escolha uma opção:
# # De acordo com a opção informada, o programa deve calcular a operação apresentada no menu. Se a opção escolhida for inválida, o programa deve mostrar a mensagem “Opção inválida” e ser encerrado.

# import os

# os.system('cls')
# numero1 = int(input("Insira um número positivo: ")) 
# numero2 = int(input("Insira outro número positivo: ")) 

# def opcao_invalida():
#     print("Opção inválida. Tente novamente!")
#     main()

# def opcoes():
#     print("\nEscolha uma das opções:\n")
#     print("1. Média ponderada, com pesos 2 e 3, respectivamente.")
#     print("2. Quadrado da soma dos 2 números")
#     print("3. Cubo do menor número")

# def escolha():
#     escolha = int(input("\nA sua escolha é: "))

#     if escolha == 1:
#         media_ponderada = ((numero1 * 2) + (numero2 * 3)) / 5
#         print(f"\nA média ponderada, com pesos 2 e 3, respectivamente é {media_ponderada}")

#     elif escolha == 2:
#         soma = numero1 + numero2
#         quadrado = soma ** 2
#         print(f"\nO quadrado da soma dos dois números é: {quadrado}")

#     elif escolha == 3:
#         menor = min(numero1, numero2)
#         cubo = menor ** 3
#         print(f"\nO cubo do menor número é {cubo}")

#     else: 
#         opcao_invalida()

# def main():
#     os.system('cls')
#     opcoes()
#     escolha()

# if __name__ == '__main__':
#     main()