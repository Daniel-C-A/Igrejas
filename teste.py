#Como Criar Uma tela Gráfica Interativa para seu programa Python

import requests

#passo1 importar Tkinter

from tkinter import *

#----------------------------------------------------------------------
#passo2 Jogar o código dentro de uma Função

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes['text'] = texto

#-----------------------------------------------------------------------

#passo3 Criar Janela usando o Tkinter

janela = Tk()
janela.title('Igrejas')
janela.geometry('200x200')

texto_orientação = Label(janela, text = 'Clique no Botão')
texto_orientação.grid(column=0, row=0, padx=50, pady=20)

botao = Button(janela, text= 'Cotações', command= pegar_cotacoes)
botao.grid(column=0, row=1, padx=10,pady=10)

texto_cotacoes = Label(janela, text='')
texto_cotacoes.grid(column=0, row=2, padx=0, pady=0) 

janela.mainloop()

#Fim