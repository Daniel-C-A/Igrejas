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
    print('Deseja continuar Lançando Receitas?')

    while opção !='N':
        print('''
        ['S'] Sim
        ['N'] Não ''')
        sleep (1)
        opção = str.upper(input('\nEscolha uma Opção Válida: '))

        if opção == 'S':
            print ('-' * 28, 'OK', '-' * 28)
            sleep (1)
            break

    if opção == 'N':
            print ('\nFinalizando!')
            sleep (1)
            print('\nBom Trabalho!')
            print('-' * 60)
            sleep (1)
            break


else:
    print('Opção Inválida, Digite 1 para Continuar ou 2 para Sair! \n')
print('=' * 25, 'Receitas', '=' * 25)  


        

    #Ofertas
    