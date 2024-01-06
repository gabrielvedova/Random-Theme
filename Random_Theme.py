#!/usr/bin/python3
import tkinter as ttk
import Regras as Rg
import dados as d
import random


def aperte_sim():
    sorteio = f'{random.choice(d.animal)} + {random.choice(d.tema)}'
    texto_tema["text"] = sorteio

# Interface Gráfica
# layout Geral


janela = ttk.Tk()
janela.title('Random Theme')
janela.geometry("420x420+350+150")
janela.minsize(420, 420)
janela.maxsize(420, 420)
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
botao_sim.place(x=80, y=100)

botao_janela2 = ttk.Button(janela,
                           text="REGRAS",
                           command=Rg.abrir_janela2,
                           font="Arial 15"
                           )
botao_janela2.place(x=260, y=100)

# linha 3
texto_tema = ttk.Label(
    janela,
    text="",
    font="Arial 25",
    background="#92CBEC",
)
texto_tema.grid(column=0, row=4, pady=150, padx=60)


janela.mainloop()
