from datetime import date
from time import sleep
print('\nIgrejas')
print('=' * 25, 'Despesas', '=' * 25)

data = date.today()
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

    #Despesas Pessoais
    if opção == 1:
        sleep (1)
        descrição = str.upper(input('\nDigite o Nome da Despesa: '))   
        despesa = float(input('\nDigite o Valor da Despesa R$ '))
        print(f'\nDescrição {descrição}\nValor R$ {despesa} \nLançada {data}')
        sleep (1)
        print('=' *60) 
        sleep(1) 
        print('Deseja continuar Lançando Despesas?')

    #Despesas de Salários        
    if opção == 2:
        sleep (1)
        descrição = str.upper(input('\nDigite o Nome da Despesa: '))
        salarios = float(input('\nDigite o Valor da Oferta R$ '))
        print(f'\nDescrição {descrição}\nValor R$ {salarios} \nLançada {data}')
        sleep(1)
        print('=' *60) 
        sleep(1) 
        print('Deseja continuar Lançando Despesas?')

    #Despesas de Investimentos
    if opção == 3:
        sleep (1)
        descrição = str.upper(input('\nDigite o Nome da Despesa: '))
        investimentos = float(input('\nDigite o Valor da Oferta Especial R$ '))
        print(f'\nDescrição {descrição}\nValor R$ {investimentos} \nLançada {data}')
        sleep(1)
        print('=' *60) 
        sleep(1) 
        print('Deseja continuar Lançando Despesas?')

    #Despesas Fixas
    if opção == 4:
        sleep (1)
        descrição = str.upper(input('\nDigite o Nome da Despesa: '))
        fixas = float(input('\nDigite o Valor da Oferta de Missões R$ '))
        print(f'\nDescrição {descrição}\nValor R$ {fixas} \nLançada {data}')
        sleep(1)
        print('=' *60) 
        sleep(1) 
        print('Deseja continuar Lançando Despesas?')

    #Despesas de Manutenções
    if opção == 5:
        sleep (1)
        descrição = str.upper(input('\nDigite o Nome da Despesa: '))
        manutenções = float(input('\nDigite o Valor da Oferta de Campanha R$ '))
        print(f'\nDescrição {descrição}\nValor R$ {manutenções} \nLançada {data}')
        sleep(1)
        print('=' *60) 
        sleep(1) 
        print('Deseja continuar Lançando Despesas?')
    
    #Finalizar Programa
    if opção == 6:
        print('Finalizando!\n')
        sleep (1)
        print('\nMuito Obrigado!')
        print('=' * 25, 'Despesas', '=' * 25)
        break

    else:
        print('Opção Invalida! Quer Continuar? ') 

        while opção !='N':
            print('''
            ['S'] Sim
            ['N'] Não ''')
            sleep (1)
            opção = str.upper(input('\nEscolha uma Opção Válida: '))
            break

        if opção == 'S':
            print ('-' * 28, 'OK', '-' * 28)
            sleep (1)

        if opção == 'N':
            print ('\nFinalizando!')
            sleep (1)
            print('\nBom Trabalho!')
            print('-' * 60)
            sleep (1)
            break  

    
    