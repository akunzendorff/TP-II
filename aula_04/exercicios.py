# # EXERCÍCIOS

# # ------------------------------------------------------------------------------------------------------------------------------------------------

# # 1) Faça um algoritmo utilizando while que mostre os número em ordem crescente de 1 a 100 

# numero = 1

# while numero <= 100:
#     print(numero)
#     numero += 1

# # ------------------------------------------------------------------------------------------------------------------------------------------------

# # 2) Digite um número e mostre a sequência, do número 1 até o número que foi digitado , utilize o while

# numero = int(input("Digite um número: "))
# i = 1

# while i <= numero:
#     print(i)
#     i += 1

# # ------------------------------------------------------------------------------------------------------------------------------------------------

# # 3) Leia a tabuada e faça a sequência utilizando while de 1 a 10 mostrando os resultados da tabuada:

# numero = int(input("Digite um número: "))
# tabuada = 1

# while tabuada <= 10:
#     resultado = numero * tabuada
#     print(f"{numero} x {tabuada} = {resultado}")
#     tabuada += 1

# # ------------------------------------------------------------------------------------------------------------------------------------------------

# # 4) Leia a tabuada e digite o valor inicial e valor final e faça a repetição utilizando while, do valor inicial até o final :

# numero = int(input("Digite um número: "))
# numeroInicial = int(input("Digite o número inicial: "))
# numeroFinal = int(input("Digite o número final: "))

# while numeroInicial <= numeroFinal:
#     resultado = numero * numeroInicial
#     print(f"{numero} x {numeroInicial} = {resultado}")
#     numeroInicial += 1


# # ------------------------------------------------------------------------------------------------------------------------------------------------

# # 5) Faça um algoritmo utilizando while que leia 4 respostas de 3 questões , se a primeira for resposta “A” será contabilizado 1 ponto, se a segunda questão for resposta “C”, será contabilizado mais um 1 ponto , se a resposta da terceira questão for “D” será contabilizado mais 1 ponto. No final mostre a pontuação total. (UTILIZE WHILE E IF)

# pontuacao = 0
# contador = 1

# while contador <= 3:
#     if contador == 1:
#         resposta = input("Digite a resposta da primeira questão: A/B/C/D ").lower()
#         if resposta == 'a':
#             pontuacao += 1
    
#     elif contador == 2:
#         resposta = input("Digite a resposta da segunda questão: A/B/C/D ").lower()
#         if resposta == 'c':
#             pontuacao += 1

#     elif contador == 3:
#         resposta = input("Digite a resposta da terceira questão: A/B/C/D ").lower()
#         if resposta == 'd':
#             pontuacao += 1

#     contador +=1


# print(f"Pontuação final: {pontuacao}")


# # ------------------------------------------------------------------------------------------------------------------------------------------------

# # 6) As lojas Quase dois possui uma grande loja de artigos de R$ 1,99. Para agilizar o cálculo de quanto cada cliente deve pagar foi desenvolvido uma tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo: (UTILIZE FOR)

# preco = 1.99

# for i in range(1,51):
#     print(f"{i} - R${(preco * i):.2f}")


# # ------------------------------------------------------------------------------------------------------------------------------------------------

# # 7) A panificadora Pão de Ontem, pretende implantar a metodologia da tabelinha. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão R$ 0.54 informado pelo usuário, Mostre somente a quantidade de pães pares. (UTILIZE FOR)

# preco = 0.54

# for i  in range(1, 51):
#     if i % 2 == 0:
#         print(f"{i} - R${(preco * i):.2f}")

# # ------------------------------------------------------------------------------------------------------------------------------------------------

# # 8) O Sr. Luiz possui uma loja de conveniências. Faça um programa que deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. (UTILIZE WHILE FOR IF)

# total = 0

# while True:
#     preco = float(input("Digiteo o preço da mercadoria (ou 0 pra finalizar a compra): R$"))

#     if preco == 0: 
#         break

#     total += preco

# print(f"O preço total da compra é R${total:.2f}")

# pago = float(input("Digite o valor pago pelo cliente: R$"))

# if pago >= total:
#     troco = pago - total
#     print(f"O troco é R${troco:.2f}")
# else:
#     print("Valor insuficiente para a compra!")

# # ------------------------------------------------------------------------------------------------------------------------------------------------

# # 9) Dado uma lista com nomes [“Maria”, “João”, “Paulo”, “Magali”]. Digite um nome para localizar , se o nome pertence a lista , se existir o nome na lista , mostre uma mensagem com o nome encontrado, e pare a repetição, caso não encontre mostre nome não encontrado. (UTILIZE FOR E IF)

# nomes = ["Maria", "João", "Paulo", "Magali"]
# nomeLocalizar = "Maria"

# for nome in nomes:
#     if nome == nomeLocalizar:
#         print(f"O nome {nomeLocalizar} foi encontrado!")
#         break
    
#     else:
#         print("Nome não encontrado...")

# # ------------------------------------------------------------------------------------------------------------------------------------------------

# # 10) Numa sequência de 3 a 200 mostre os números, num passo de 3 em 3 usando for range. (UTILIZE FOR)

# for i in range(3, 201, 3):
#     print(i)

# # ------------------------------------------------------------------------------------------------------------------------------------------------

# # 11) Dado uma lista com nomes ["Luiz","Ana","Cristina","Fernanda","Maria Alice", "Joaquina" ] Utilize o while e if para fazer a repetição perguntando se o usuário digitar 1 ele faz a busca se apertar 0 , sai da aplicação. Se o usuário escolher fazer a busca: Digite um nome para localizar , se existir o nome na lista , mostre uma mensagem com o nome encontrado, e pare a repetição, caso não encontre mostre nome não encontrado. (UTILIZE FOR E IF)

# nomes = ["Luiz", "Ana", 'Cristina', 'Fernanda', 'Maria Alice', 'Joaquina']

# numero = int(input("Digite 1 para fazer a busca ou 0 para sair: "))

# while numero != 0:
#     if numero == 1:
#         nome_localizar = input("Digite um nome para localizar: ").title()

#         nome_encontrado = False

#         for nome in nomes:
#             if nome_localizar == nome:
#                 print(f"O nome {nome_localizar} foi encontrado!")
#                 nome_encontrado = True
#                 break

#         if not nome_encontrado:
#             print(f"O nome {nome_localizar} não foi encontrado...")

#     else:
#         print("Número inválido")

#     numero = int(input("Digite 1 para fazer a busca ou 0 para sair: "))

# print("Finalizando a aplicação...")

# # ------------------------------------------------------------------------------------------------------------------------------------------------

# # 12) Digite 7 nomes e armazene esses valores em uma lista e mostre os nomes que foram armazenados , e sua posição na lista. (UTILIZE FOR)

# nomes = []

# for i in range(7):
#     nome = input("Insira um nome:")
#     nomes.append(nome)
    
# for i, nome in enumerate(nomes):
#     print(f"Nome: {nome.ljust(20)} | Posição na lista: {i+1}")

# # ------------------------------------------------------------------------------------------------------------------------------------------------

# # 13) Leia 10 números e verifique e se são números pares ou ímpares , e mostre os números pares e os números ímpares (UTILIZE FOR E IF)

# numeros = []
# pares = []
# impares = []

# for i in range(10):
#     numero = int(input("Digite um número: "))
#     numeros.append(numero)

#     if numero % 2 == 0:
#         pares.append(numero)

#     elif numero % 2 == 1:
#         impares.append(numero)

# print("\n**Números pares**\n")
# for numero_par in pares:
#     print(f" - {numero_par}")


# print("\n**Números ímpares**\n")
# for numero_impar in impares:
#     print(f" - {numero_impar}")


# # ------------------------------------------------------------------------------------------------------------------------------------------------

# # 14) Numa sequência decrescente de 500 a 1 mostre os números pulando passos de 3 em 3. (UTILIZE FOR)



# # ------------------------------------------------------------------------------------------------------------------------------------------------

# # 15) Na sequência de 1 a 800 mostre a soma de todos os números utilizando a estrutura While

# i = 1
# soma = 0

# while i <= 800:
#     soma = soma + i
#     i += 1

# print(f"A soma dos números de 1 a 800 é: {soma}")

# # ------------------------------------------------------------------------------------------------------------------------------------------------

# # 16) Na sequência de 1 a 750 mostre os número com espaçamento de 4 em 4, e no final mostre a quantidade de número que foram mostrados na tela (UTILIZE FOR)

# numeros_exibidos = 0

# for i in range(750):

#     if i % 4 == 0:
#         print(f" - {i+1}")
#         numeros_exibidos += 1

#     i += 1

# print(f"A quantidade de números exibidos foi: {numeros_exibidos}")

# # ------------------------------------------------------------------------------------------------------------------------------------------------

# # 17) Dado a lista de Linguagens de Programação: ["python","c#","Visual Basic","C++","Delphi","Cobol"] Mostre somente as linguagens que possui mais de 3 caracteres, e no final mostre a quantidade de caracteres, de todas as linguagens da lista. (UTILIZE FOR E IF)

# linguagens = ["python","c#","Visual Basic","C++","Delphi","Cobol"]

# print("\nLinguagens com mais de três caracteres:\n")

# for linguagem in linguagens:
#     if len(linguagem) > 3:
#         print(f"- {linguagem}")

# print("\nQuantidade de caracteres de cada linguagem: \n")

# for linguagem in linguagens:
#     print(f"{linguagem.ljust(15)} | {len(linguagem)} caracteres")

# # ------------------------------------------------------------------------------------------------------------------------------------------------

# # 18) Digite o nome de uma linguagem e verifique se o nome está na lista: ["python","c#","Visual Basic","C++","Delphi","Cobol","Clipper","PHP","Java"] Se o nome digitado estiver na lista, diga que foi encontrado, senão tiver diga que não foi encontrado , no final mostre a posição na lista, que se encontra o nome da linguagem digitada (UTILIZE FOR E IF)

# linguagens = ["Python","c#","Visual Basic","C++","Delphi","Cobol","Clipper","PHP","Java"]

# linguagem_encontrada = False

# linguagem_localizar = input("Digite a linguagem a ser localizada: ").title()

# for i, linguagem in enumerate(linguagens):

#     if linguagem_localizar == linguagem:
#         print(f"A linguagem {linguagem_localizar} foi encontrada na posição {i+1}!")
#         linguagem_encontrada = True
#         break

# if not linguagem_encontrada:
#     print(f"A linguagem {linguagem_localizar} não foi encontrada...")

# # ------------------------------------------------------------------------------------------------------------------------------------------------

# # 19) Dado uma lista de vogais, digite 10 letras e verifique se a letra digitada é uma vogal, verifique na lista de vogais , se a letra estiver na lista, diga que a letra digitada é uma vogal. (UTILIZE FOR E IF)

# vogais = ['a', 'e', 'i', 'o', 'u']
# letras = []

# for i in range(10):
#     letra = input("Digite uma letra: ").lower()
#     letras.append(letra)


# for letra in letras:
#     if letra in vogais:
#         print(f"A letra {letra} é uma vogal!")

#     else:
#         print(f"A letra {letra} não é uma vogal.")

# OU

# conjunto_vogais = ['a', 'e', 'i', 'o', 'u']
# letras = []
# consoantes = []
# vogais = []

# for i in range(10):
#     letra = input("Digite uma letra: ").lower()
#     letras.append(letra)


# for letra in letras:
#     if letra in conjunto_vogais:
#         vogais.append(letra)

#     else:
#         consoantes.append(letra)

# print("**VOGAIS**")

# for vogal in vogais:
#     print(f" - {vogal}")


# print("**CONSOANTES**")

# for consoante in consoantes:
#     print(f" - {consoante}")

# # ------------------------------------------------------------------------------------------------------------------------------------------------

# # 20) Crie uma lista de 1 a 20 números e mostre apenas os números que são múltiplos de 3, e diga quantos números são múltiplos de 3 (UTILIZE FOR)

# numeros = range(20)
# multiplos = 0

# print("***Números entre 1 e 20 que são multiplos de 3***")

# for numero in numeros:
#     if numero % 3 == 0:
#         print(f" - {numero}")
#         multiplos += 1

# print(f"A quantidade de números multiplos de três entre 1 e 20 são: {multiplos}")

# # ------------------------------------------------------------------------------------------------------------------------------------------------

# # 21) Uma empresa precisa fazer um determinado exame, somente para os funcionários do sexo masculino , digite o nome e o sexo dos 15 funcionários da empresa, e mostre o nome , e se necessita fazer o exame. Verifique se o usuário digitou F ou M , senão mostre que o sexo foi digitado incorretamente. (UTILIZE WHILE E IF)

for i in range(15):
    nome = input("Digite o nome do funcionário: ").title()
    sexo = input(f"Digite o sexo do funcionário {nome}: ").upper()

    if sexo == 'M':
        print(f"O funcionário {nome} precisa fazer o exame!")

    elif sexo == 'F':
        print(f"A funcionária {nome} não precisa fazer o exame!")

    else:
        print(f"O sexo do funcionário {nome} foi digitado incorretamente...")
