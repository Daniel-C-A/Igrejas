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
    #-----------------------------------------------------------------------
        #Despesas Pessoais
        if opção == 1:
            sleep (1)
            descrição = str.upper(input('\nDescreva a Despesa: '))   
            despesa = float(input('\nDigite o Valor da Despesa R$ '))
            print(f'\nDespesa Pessoal: {descrição}\nValor R$ {despesa:,.2f} \nLançada {data_em_texto}')
            sleep (1)
            print('=' *60) 
            sleep(1) 

            #While Despesas Pessoais
            while opção != 'N':
                print('Continuar Lançando Despesas?')
                print('''
                [S] Sim
                [N] Não ''')
                sleep (1)
                opção = str.upper(input('\nEscolha uma Opção Válida: '))
        
                if opção == 'S':
                    print ('-' * 28, 'OK', '-' * 28)
                    sleep (1)
                    break  
            else:
                print('\nMuito Obrigado!\n')
                print('=' * 25, 'Receitas', '=' * 25)
                sleep (1)
                break
    #-----------------------------------------------------------------------
        #Despesas de Salários        
        if opção == 2:
            sleep (1)
            descrição = str.upper(input('\nPagamento para: '))
            salarios = float(input('\nDigite o Valor do Salário R$ '))
            print(f'\nPagamento de Salário: {descrição}\nValor R$ {salarios:,.2f} \nLançada {data_em_texto}')
            sleep(1)
            print('=' *60) 
            sleep(1) 

            #While Despesas de Salários
            while opção != 'N':
                print('Continuar Lançando Despesas?')
                print('''
                [S] Sim
                [N] Não ''')
                sleep (1)
                opção = str.upper(input('\nEscolha uma Opção Válida: '))
        
                if opção == 'S':
                    print ('-' * 28, 'OK', '-' * 28)
                    sleep (1)
                    break  
            else:
                print('\nMuito Obrigado!\n')
                print('=' * 25, 'Receitas', '=' * 25)
                sleep (1)
                break
    #-----------------------------------------------------------------------
        #Despesas de Investimentos
        if opção == 3:
            sleep (1)
            descrição = str.upper(input('\nDescreva o Investimento: '))
            investimentos = float(input('\nDigite o Valor do Investimento R$ '))
            print(f'\nInvestimento em: {descrição}\nValor R$ {investimentos:,.2f} \nLançada {data_em_texto}')
            sleep(1)
            print('=' *60) 
            sleep(1) 

            #While Despesas de Investimentos
            while opção != 'N':
                print('Continuar Lançando Despesas?')
                print('''
                [S] Sim
                [N] Não ''')
                sleep (1)
                opção = str.upper(input('\nEscolha uma Opção Válida: '))
        
                if opção == 'S':
                    print ('-' * 28, 'OK', '-' * 28)
                    sleep (1)
                    break  
            else:
                print('\nMuito Obrigado!\n')
                print('=' * 25, 'Receitas', '=' * 25)
                sleep (1)
                break
    #-----------------------------------------------------------------------
        #Despesas Fixas
        if opção == 4:
            sleep (1)
            descrição = str.upper(input('\nDescreva Despesa Fixa: '))
            fixas = float(input('\nDigite o Valor R$ '))
            print(f'\nPagamento da Despesa Fixa: {descrição}\nValor R$ {fixas:,.2f} \nLançada {data_em_texto}')
            sleep(1)
            print('=' *60) 
            sleep(1) 

            #While Despesas Fixas
            while opção != 'N':
                print('Continuar Lançando Despesas?')
                print('''
                [S] Sim
                [N] Não ''')
                sleep (1)
                opção = str.upper(input('\nEscolha uma Opção Válida: '))
        
                if opção == 'S':
                    print ('-' * 28, 'OK', '-' * 28)
                    sleep (1)
                    break  
            else:
                print('\nMuito Obrigado!\n')
                print('=' * 25, 'Receitas', '=' * 25)
                sleep (1)
                break
    #-----------------------------------------------------------------------
        #Despesas de Manutenções
        if opção == 5:
            sleep (1)
            descrição = str.upper(input('\nDescreva a Manutenção: '))
            manutenções = float(input('\nDigite o Valor da Manutenção R$ '))
            print(f'\nManutenção: {descrição}\nValor R$ {manutenções:,.2f} \nLançada {data_em_texto}')
            sleep(1)
            print('=' *60) 
            sleep(1) 

            #While Manutenções
            while opção != 'N':
                print('Continuar Lançando Despesas?')
                print('''
                [S] Sim
                [N] Não ''')
                sleep (1)
                opção = str.upper(input('\nEscolha uma Opção Válida: '))
        
                if opção == 'S':
                    print ('-' * 28, 'OK', '-' * 28)
                    sleep (1)
                    break  
            else:
                print('\nMuito Obrigado!\n')
                print('=' * 25, 'Receitas', '=' * 25)
                sleep (1)
                break
    #---------------------------------------------------------------------- 
        #Finalizar Programa
        if opção == 6:
            print('Finalizando!\n')
            sleep (1)
    else:
        print('\nMuito Obrigado!\n') 
        print('=' * 25, 'Receitas', '=' * 25)
        sleep (1) 
    #-----------------------------------------------------------------------
lançar_despesas()

janela = Tk()
janela.title('Igrejas')
janela.geometry('200x200')


janela.mainloop()