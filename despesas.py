from datetime import date
from time import sleep
print('\nIgrejas')
print('=' * 25, 'Despesas', '=' * 25)

data = date.today()
opção = 0

while opção !=6:
    print('''
    [1] Despesa Pessoal
    [2] Despesa Salário
    [3] Despesas Investimentos
    [4] Despesas Fixas
    [5] Despesas Manutenção
    [6] Sair! ''')
    sleep (1)
    opção = int(input('\nEscolha uma Opção Válida: '))

#despesas pessoais
    if opção == 1:
        sleep (1)
    descrição = str.upper(input('\nDigite o Nome da Despesa: '))   
    despesa = float(input('\nDigite o Valor da Despesa R$ '))
    print(f'\nDescrição {descrição}\nValor R$ {despesa} \nLançada {data}')
    sleep (1)
    print('=' *60) 
    sleep(1) 
    print('Deseja continuar Lançando Despesas?')
    print('''
    [1] SIM
    [2] NÃO''')
    opção = int(input('\nDigite sua Opção: '))
    if opção == 1:
        print ('-' * 28, 'OK', '-' * 28)
        sleep (1)
    if opção == 2:
        print ('\nFinalizando!')
        sleep (1)
        print('\nBom Trabalho!')
        print('-' * 60)
        sleep (1)
        break
    else:
        print('Digite 1 para Continuar e 2 para Sair! ')
    print('=' * 25, 'Despesas', '=' * 25)
    
         

#despesas de salário
    