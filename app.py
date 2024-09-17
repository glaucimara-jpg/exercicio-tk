
import tkinter as tk
from tkinter import TclError, ttk


def create_input_frame(container):

    frame = ttk.Frame(container)

    # layout de grade para o quadro de entrada
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)

    # encontrar
    ttk.Label(frame, text='encontre o que:').grid(column=0, row=0, sticky=tk.W)
    keyword = ttk.Entry(frame, width=30)
    keyword.focus()
    keyword.grid(column=1, row=0, sticky=tk.W)

    # substituir por
    ttk.Label(frame, text='substitua por:').grid(column=0, row=1, sticky=tk.W)
    replacement = ttk.Entry(frame, width=30)
    replacement.grid(column=1, row=1, sticky=tk.W)

    # Match Case checkbox
    match_case = tk.StringVar()
    match_case_check = ttk.Checkbutton(
        frame,
        text='caso de jogo',
        variable=match_case,
        command=lambda: print(match_case.get()))
    match_case_check.grid(column=0, row=2, sticky=tk.W)

    # Caixa de seleção Contornar
    wrap_around = tk.StringVar()
    wrap_around_check = ttk.Checkbutton(
        frame,
        variable=wrap_around,
        text='selecione',
        command=lambda: print(wrap_around.get()))
    wrap_around_check.grid(column=0, row=3, sticky=tk.W)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame


def create_button_frame(container):
    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=1)

    ttk.Button(frame, text='encontre o proximo').grid(column=0, row=0)
    ttk.Button(frame, text='substitua').grid(column=0, row=1)
    ttk.Button(frame, text='substitua tudo').grid(column=0, row=2)
    ttk.Button(frame, text='Cancelar').grid(column=0, row=3)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame


def create_main_window():
    root = tk.Tk()
    root.title('substituir')
    root.resizable(0, 0)
    try:
        # somente janelas (remova o botão minimizar/maximizar)
        root.attributes('-toolwindow', True)
    except TclError:
        print('não suportado pela plataforma')

    # layout na janela raiz
    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=1)

    input_frame = create_input_frame(root)
    input_frame.grid(column=0, row=0)

    button_frame = create_button_frame(root)
    button_frame.grid(column=1, row=0)

    root.mainloop()


if __name__ == "__main__":
    create_main_window()
