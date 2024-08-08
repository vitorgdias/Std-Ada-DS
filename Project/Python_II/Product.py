from Resources import *

def create_register():
    while True:
        print('\nQual tipo de registro deseja criar?')
        print('='*50)
        print('1. Receita.')
        print('2. Despesa.')
        print('3. Investimento.')
        print('4. Voltar ao menu principal.')
        escolha = input('\nDigite um número de 1 a 3, ou 4 para retornar ao menu principal: ')
        if escolha == '1':
            return
        elif escolha == '2':
            return
        elif escolha == '3':
            return
        elif escolha == '4':
            break
        else:
            print('\nPor favor escolha uma opção válida.')
    return

def read_register():
    return

def update_register():
    return

def delete_register():
    return

def export_report():
    return