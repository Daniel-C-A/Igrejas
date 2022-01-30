from datetime import date
from time import sleep
print('\nIgrejas')
print('=' * 25, 'Receitas', '=' * 25)

data = date.today()
data_em_texto = data.strftime("%d/%m/%Y")

opção = 0

while opção !=6:
    print('''
    [1] Dízimos
    [2] Ofertas
    [3] Ofertas Especiais
    [4] Missões
    [5] Campanhas
    [6] Sair! ''')
    sleep (1)
    opção = int(input('\nEscolha uma Opção Válida: '))
#-----------------------------------------------------------------------
    #Dízimos
    if opção == 1:
        sleep (1)
        descrição = str.upper(input('\nNome do Dizimista: '))   
        receita = float(input('\nDigite o Valor do Dízimo R$ '))
        print(f'\nDízimo: {descrição}\nValor R$ {receita:,.2f} \nLançado {data_em_texto}')
        sleep (1)
        print('=' *60) 
        sleep(1)

        #While Dizimos
        while opção != 'N':
            print('Continuar Lançando Receitas?')
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
    #Ofertas
    if opção == 2:
        sleep (1)
        descrição = str.upper(input('\nDigite o Nome da Oferta: '))
        oferta = float(input('\nDigite o Valor da Oferta R$ '))
        print(f'\nOferta: {descrição}\nValor R$ {oferta:,.2f} \nLançada {data_em_texto}')
        sleep(1)
        print('=' *60) 
        sleep(1)

        #while Ofertas
        while opção != 'N':
            print('Continuar Lançando Receitas?')
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
    #Ofertas Especiais
    if opção == 3:
        sleep (1)
        descrição = str.upper(input('\nDescrição da Oferta: '))
        oferta = float(input('\nDigite o Valor da Oferta Especial R$ '))
        print(f'\nOferta Especial: {descrição}\nValor R$ {oferta:,.2f} \nLançada {data_em_texto}')
        sleep(1)
        print('=' *60) 
        sleep(1)

        #While Ofertas Especiais
        while opção != 'N':
            print('Continuar Lançando Receitas?')
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
    #Missões       
    if opção == 4:
        sleep (1)
        descrição = str.upper(input('\nDescreva a Oferta de Missões: '))
        missões = float(input('\nDigite o Valor da Oferta de Missões R$ '))
        print(f'\nMissões: {descrição}\nValor R$ {missões:,.2f} \nLançada {data_em_texto}')
        sleep(1)
        print('=' *60) 
        sleep(1)

        #While Missões
        while opção != 'N':
            print('Continuar Lançando Receitas?')
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
#----------------------------------------------------------------------     #Campanha
    if opção == 5:
        sleep (1)
        descrição = str.upper(input('\nDigite o Nome da Campanha: '))
        campanha = float(input('\nDigite o Valor da Oferta de Campanha R$ '))
        print(f'\nCampanha: {descrição}\nValor R$ {campanha:,.2f} \nLançada {data_em_texto}')
        sleep(1)
        print('=' *60) 
        sleep(1) 

        #While Campanha
        while opção != 'N':
            print('Continuar Lançando Receitas?')
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
    #Finalizar Programa
    if opção == 6:
        print('Finalizando!\n')
        sleep (1)
else:
    print('\nMuito Obrigado!\n') 
    print('=' * 25, 'Receitas', '=' * 25)
    sleep (1) 
#----------------------------------------------------------------------      