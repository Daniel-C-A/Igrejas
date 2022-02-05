from datetime import date
from time import sleep
from tkinter import *

def lançar_despesas():

    print('\nIgrejas')
    print('=' * 25, 'Despesas', '=' * 25)

    data = date.today()
    data_em_texto = data.strftime("%d/%m/%Y")

    opção = 0

    while opção !=6:
        print('''
        [1] Despesas Pessoais
        [2] Despesas de Salários
        [3] Despesas de Investimentos
        [4] Despesas Fixas
        [5] Despesas de Manutenções
        [6] Sair! ''')
        sleep (1)
        opção = int(input('\nEscolha uma Opção Válida: '))

        nome_programa['text'] = opção
    
janela = Tk()
janela.title('Igrejas')
janela.geometry('200x200')

nome_programa = Label(janela, text = 'Contábil Igrejas')
nome_programa.grid(column=0, row=0,)

botao = Button(janela, text='Lançar Despesas', command= lançar_despesas)
botao.grid(column=0, row=1,)

Entry().grid(row= 2, column= 0)
Entry().grid(row= 3, column= 0)
janela.mainloop()