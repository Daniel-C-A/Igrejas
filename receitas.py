from datetime import date
from time import sleep
print('\nIgrejas')
print('=' * 25, 'Receitas', '=' * 25)

data = date.today()
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

    #Dízimos
    if opção == 1:
        sleep (1)
        descrição = str.upper(input('\nDigite o Nome da Receita: '))   
        receita = float(input('\nDigite o Valor da Receita R$ '))
        print(f'\nDescrição {descrição}\nValor R$ {receita} \nLançada {data}')
        sleep (1)
        print('=' *60) 
        sleep(1)
#-------------------------------------------------------------------------------
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
            print('Saindo! Muito Obrigado!')
            break
#-------------------------------------------------------------------------------  

    if opção == 2:
        sleep (1)
        descrição = str.upper(input('\nDigite o Nome da Receita: '))
        oferta = float(input('\nDigite o Valor da Oferta R$ '))
        print(f'\nDescrição {descrição}\nValor R$ {oferta} \nLançada {data}')
        sleep(1)
        print('=' *60) 
        sleep(1)
#-------------------------------------------------------------------------------
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
            print('Saindo! Muito Obrigado!')
            break

#-------------------------------------------------------------------------------
    if opção == 3:
        sleep (1)
        descrição = str.upper(input('\nDigite o Nome da Receita: '))
        oferta = float(input('\nDigite o Valor da Oferta Especial R$ '))
        print(f'\nDescrição {descrição}\nValor R$ {oferta} \nLançada {data}')
        sleep(1)
        print('=' *60) 
        sleep(1)
#--------------------------------------------------------------------------------
        #While Oferta Especial
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
            print('Saindo! Muito Obrigado!')
            break
#--------------------------------------------------------------------------------        

    if opção == 4:
        sleep (1)
        descrição = str.upper(input('\nDigite o Nome da Receita: '))
        missões = float(input('\nDigite o Valor da Oferta de Missões R$ '))
        print(f'\nDescrição {descrição}\nValor R$ {missões} \nLançada {data}')
        sleep(1)
        print('=' *60) 
        sleep(1)

#--------------------------------------------------------------------------------
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
            print('Saindo! Muito Obrigado!')
            break
#--------------------------------------------------------------------------------           

    if opção == 5:
        sleep (1)
        descrição = str.upper(input('\nDigite o Nome da Receita: '))
        campanha = float(input('\nDigite o Valor da Oferta de Campanha R$ '))
        print(f'\nDescrição {descrição}\nValor R$ {campanha} \nLançada {data}')
        sleep(1)
        print('=' *60) 
        sleep(1) 

#--------------------------------------------------------------------------------
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
            print('Saindo! Muito Obrigado!')
            break
#--------------------------------------------------------------------------------

    if opção == 6:
        print('Finalizando!\n')
        sleep (1)
        print('\nMuito Obrigado!')
        print('=' * 25, 'Receitas', '=' * 25)

    else:
        print('Essa Opção é Inválida!')
         