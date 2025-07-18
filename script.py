
import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("400x500") #LarguraxAltura
janela.iconbitmap("calculator-outline.ico")
#Cria uma VAR que recebe o texto do visor
visor_texto = tk.StringVar()

# Cria um visor
visor = tk.Entry(janela, textvariable=visor_texto, font=("Arial", 24), justify='right')
visor.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

def clicar(valor):
    atual = visor_texto.get()
    visor_texto.set(atual + str(valor))

# Lista Botões

botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Lista de botões com seus textos e posições
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Criando os botões dinamicamente
for (texto, linha, coluna) in botoes:
    if texto == '=':
        botao = tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 18), command=lambda: calcular())
    elif texto == 'C':
        botao = tk.Button(janela, text=texto, width=22, height=2, font=("Arial", 18), command=lambda: visor_texto.set(""))
        botao.grid(row=linha, column=coluna, columnspan=4, padx=5, pady=5)
        continue
    else:
        botao = tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 18), command=lambda t=texto: clicar(t))
    botao.grid(row=linha, column=coluna, padx=5, pady=5)

def calcular():
    try:
        resultado = eval(visor_texto.get())
        visor_texto.set(str(resultado))
    except:
        visor_texto.set("Erro")    

janela.mainloop()









