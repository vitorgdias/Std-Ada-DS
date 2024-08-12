from Resources import *

def create_register():
    registros = []
    id_registro = 1
    while True:
        print('\nQual tipo de registro deseja criar?')
        print('='*50)
        print('1. Receita.')
        print('2. Despesa.')
        print('3. Investimento.')
        print('4. Voltar ao menu principal.')
        escolha = input('\nDigite um número de 1 a 3, ou 4 para retornar ao menu principal: ')
        if escolha == '4':
            break
        elif escolha != '1' and escolha != '2' and escolha != '3':
            print('\nPor favor escolha uma opção válida.')

        data = input('\nPrimeiro insira a data (digite no formato dd/mm/aaaa): ')
        if date_validation(data):
            pass
        else:
            print('\n' + '='*55 + '\nData inválida, por gentileza entre com uma data válida.\n' + '='*55)
            return create_register()
        valor = value_converter()
        if valor:
            pass
        else:
            return create_register()

        if escolha == '1':
            tipo = 'Receita'
            print('\nCerto, vamos registra sua Receita:' + '\n' + '='*50)
        elif escolha == '2':
            tipo = 'Despesa'
            print('\nCerto, vamos registra sua Despesa:' + '\n' + '='*50)
        elif escolha == '3':
            tipo = 'Investimento'
            print('\nCerto, vamos registra seu Investimento:' + '\n' + '='*50)
        
        registros.append({'ID': id_registro, 'registro': tipo, 'data':data, 'valor':valor})
        id_registro += 1

        print(registros)
        

    return registros

def read_register():
    return

def update_register():
    return

def delete_register():
    return

def export_report():
    return