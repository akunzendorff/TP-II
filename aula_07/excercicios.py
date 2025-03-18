# from tkinter import *

# # Criação da variável
# tela = Tk()

# # Titulo da barra de titulos
# tela.title("Cadastro de Clientes")

# # Cor da tela
# tela.configure(background = '#1e3743')

# # Configurar o tamanho da tela
# tela.geometry("700x600")

# # Define reajuste da tela
# tela.resizable(True, True)

# # Tamanho máximo que a tela pode chegar
# tela.maxsize()

# # Colocando caixa de texto
# lbl_titulo = Label(tela, text = "CADASTRO DE CLIENTES", font = "Arial 25 bold italic", bg = "#1e3743", fg = "#bcd1ad")
# lbl_titulo.pack()

# lbl_nome = Label(tela, text = "Digite o nome: ", font = "Arial 15 bold italic", bg = "#1e3743", fg = "#f0ffff")
# lbl_nome.place(x = 10, y = 45)
# txt_nome = Entry(tela, width = 60, borderwidth = 5, fg = "blue")
# txt_nome.place(x = 165, y = 45)
# txt_nome.insert(0, "Digite seu nome aqui")

# lbl_email= Label(tela, text = "Digite o e-mail: ", font = "Arial 15 bold italic", bg = '#1e3743', fg = '#f0ffff')
# lbl_email.place(x = 10, y = 85)
# txt_email = Entry(tela, width = 60, borderwidth = 5, fg = "blue")
# txt_email.place(x = 165, y = 85)
# txt_email.insert(0, "Digite seu e-mail aqui")

# lbl_telefone= Label(tela, text = "Digite o telefone: ", font = "Arial 15 bold italic", bg = '#1e3743',fg = '#f0ffff')
# lbl_telefone.place(x = 10, y = 125)
# txt_telefone = Entry(tela, width = 60, borderwidth = 5, fg = "blue")
# txt_telefone.place(x = 185, y = 125)
# txt_telefone.insert(0, "Digite seu telefone aqui")

# lbl_endereco= Label(tela, text = "Digite o endereço: ", font = "Arial 15 bold italic", bg = '#1e3743', fg = '#f0ffff')
# lbl_endereco.place(x = 10, y = 165)
# txt_endereco = Entry(tela, width = 60, borderwidth = 5, fg = "blue")
# txt_endereco.place(x = 205, y = 165)
# txt_endereco.insert(0, "Digite seu endereço aqui")


# # Definindo uma função
# def mostrar_dados():
#     lbl_titulo_cliente = Label(tela, text = "Dados do Cliente", font = "Arial 25 bold italic", bg = "#1e3743", fg = "#bcd")
#     lbl_titulo_cliente.place(x = 205, y = 200)
#     lbl_ola = Label(tela, text = "Nome: " + txt_nome.get() + "\nTelefone: " + txt_telefone.get() + "\nEndereço: " + txt_endereco.get() + "\nE-mail: " + txt_email.get())
#     lbl_ola.place(x = 205, y = 235)

    
# # Adicionando um botão 
# btn_botao = Button(tela, text = "Cadastrar Cliente", font = "Arial 15 bold ", bg = '#1ed', command = mostrar_dados)
# btn_botao.place(x=250, y=325)

# def verificaFocusCaixa(event):    
#     txt_nome.delete(0,END)

# txt_nome.bind("<FocusIn>", verificaFocusCaixa)

# # Executando a tela
# tela.mainloop()

# --------------------------------------------------------------------------------------------------

# exercicio 2

from tkinter import *

# Criação da variável
tela = Tk()

# Titulo da barra de titulos
tela.title("Cadastro de Clientes")

# Cor da tela
tela.configure(background = '#1e3743')

# Configurar o tamanho da tela
tela.geometry("700x600")

# Define reajuste da tela
tela.resizable(True, True)

# Tamanho máximo que a tela pode chegar
tela.maxsize()

# Colocando caixa de texto
lbl_titulo = Label(tela, text = "Calculo soma", font = "Arial 25 bold italic", bg = "#1e3743", fg = "#bcd1ad")
lbl_titulo.pack()

lbl_numero1 = Label(tela, text = "Digite o primeiro número: ", font = "Arial 15 bold italic", bg = "#1e3743", fg = "#f0ffff")
lbl_numero1.place(x = 10, y = 45)
txt_numero1 = Entry(tela, width = 60, borderwidth = 5, fg = "blue")
txt_numero1.place(x = 165, y = 45)
txt_numero1.insert(0, "Digite o primeiro número aqui")

lbl_numero2= Label(tela, text = "Digite o segundo número: ", font = "Arial 15 bold italic", bg = '#1e3743', fg = '#f0ffff')
lbl_numero2.place(x = 10, y = 85)
txt_numero2 = Entry(tela, width = 60, borderwidth = 5, fg = "blue")
txt_numero2.place(x = 165, y = 85)
txt_numero2.insert(0, "Digite o segundo número aqui")


# Definindo uma função
def calcular():
    soma = txt_numero1 + txt_numero2
    print(soma)
    
    lbl_resultado = Label(tela, text = "Resultado: " + calcular[soma])
    
# Adicionando um botão 
btn_botao = Button(tela, text = "Calcular", font = "Arial 15 bold ", bg = '#1ed', command = calcular)
btn_botao.place(x=250, y=325)

def verificaFocusCaixa(event):    
    txt_numero1.delete(0,END)

txt_numero1.bind("<FocusIn>", verificaFocusCaixa)

# Executando a tela
tela.mainloop()
