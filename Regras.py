import tkinter as ttk


def abrir_janela2():
    janela2 = ttk.Toplevel()
    janela2.title("Regras")
    janela2.geometry("600x450+500+50")
    janela2.minsize(600, 450)
    janela2.maxsize(600, 450)
    janela2.configure(background="#ADD8E6")

    texto_introdução = ttk.Label(
        janela2,
        text="REGRAS",
        font="Arial 19",
        background="#ADD8E6",
        pady=20
    )
    texto_introdução.pack()
    regra1 = ttk.Label(
        janela2,
        text="1.Objetivo do jogo: criar uma arte ou texto com tema sorteado.",
        font="Arial 15",
        background="#ADD8E6")
    regra1.place(x=20, y=70)
    regra2 = ttk.Label(
        janela2,
        text="2.Jogadores devem fazer todos uma arte ou um texto.",
        font="Arial 15",
        background="#ADD8E6"
    )
    regra2.place(x=20, y=120)
    regra3 = ttk.Label(
        janela2,
        text="3.Cada partida tem uma duração máxima de 15 minutos.",
        font="Arial 15",
        background="#ADD8E6"
    )
    regra3.place(x=20, y=170)
    regra4 = ttk.Label(
        janela2,
        text="4.Jogadores ou pessoas fora do jogo avaliam qual é o melhor.",
        font="Arial 15",
        background="#ADD8E6"
    )
    regra4.place(x=20, y=220)
    regra5 = ttk.Label(
        janela2,
        text="5.É proibido o uso de internet ou fotos que ajudam o jogador.",
        font="Arial 15",
        background="#ADD8E6"
    )
    regra5.place(x=20, y=270)
