#!/usr/bin/python3
import tkinter as ttk
import random

# Recebendo arquivo csv
# Animal

arq_anim = open('animais.csv')
dad_anim = arq_anim.read().splitlines()
dad_anim.remove(dad_anim[0])
arq_anim.close()

# Tema
arq_tema = open('tema.csv')
dad_tema = arq_tema.read().splitlines()
dad_tema.remove(dad_tema[0])
arq_tema.close()

# Random dos dados


def aperte_sim():
    sorteio = f'{random.choice(dad_anim)} + {random.choice(dad_tema)}'
    texto_tema["text"] = sorteio

# Interface Gráfica
# layout Geral


janela = ttk.Tk()
janela.title('Random Theme')
janela.geometry("420x420+350+150")
janela.minsize(420, 420)
##janela.maxsize(420, 420)
janela.configure(background="#92CBEC")

# ESPAÇO
espaco1 = ttk.Label(text="", background="#92CBEC")
espaco1.grid(column=0, row=0)
espaco2 = ttk.Label(text="", background="#92CBEC")
espaco2.grid(column=0, row=1)

# Linha 1
texto_pergunta = ttk.Label(
    janela,
    text="O tema de hoje será:",
    background="#92CBEC",
    font="Arial 20",
    padx=20
)
texto_pergunta.place(x=60, y=30)

# linha 2
botao_sim = ttk.Button(janela,
                       text="MOSTRAR",
                       command=aperte_sim,
                       font="Arial 15"
                       )
botao_sim.place(x=150, y=100)

# linha 3
texto_tema = ttk.Label(
    janela,
    text="",
    font="Arial 25",
    background="#92CBEC",
    justify="center",
)
texto_tema.grid(column=0, row=4, pady=150, padx=60)


janela.mainloop()
