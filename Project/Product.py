import datetime

def date_validation(data_input):
    try:
        return datetime.datetime.strptime(data_input, "%d/%m/%Y")
    except ValueError:
        return False
    
def value_converter():
    while True:
        value = input('Digite o valor (Exemplo: 1234.56): ')
        try:
            value_converted = float(value)
            if value_converted == round(value_converted, 2):
                return value_converted
            else:
                print('Número inválido! Insira um número com até duas casas decimais.')
        except ValueError:
            print('Valor inválido. Por favor, digite um número.')


def Print_Registros(dicionario):
    print("\nForam feitos os seguintes registros:")
    for chave, valor in dicionario.items():
        print(f"\n{chave} no dia {valor}")

def Create_Register():
    dict_registros = {}
    data = input('\nO registro é de hoje (S/N)? ')
    if data.lower() == 's':
        data = datetime.datetime.now().strftime("%d/%m/%Y")
        pass
    elif data.lower() == 'n':
        data = input('\nEntre com a data do registro (dd/MM/AAAA): ')
        if date_validation(data):
            pass
        else:
            print('\nAtenção a data inserida é inválida, por favor insira uma data válida.')
            Create_Register()

    registro = input('\nQual o registro a ser criado? ')
    try:    
        if registro.lower() == 'despesa':
            print('\nRegistro de despesa inserido com sucesso!')
            pass
        elif registro.lower() == 'receita':
            print('\nRegistro de receita inserido com sucesso!')
            pass
        elif registro.lower() == 'investimento':
            print('\nRegistro de investimento inserido com sucesso!')
            pass
        else:
            print('\nRegistro Inválido.')
            Create_Register()
    except ValueError:
        print(f'{ValueError}')
    
    continuar = input('\nInserir outro registro (S/N)? ')
    if continuar.lower() == 's':
        Create_Register()
    elif continuar.lower() == 'n':
        pass
    else:
        return
    
    dict_registros = {registro.capitalize():data}

    return Print_Registros(dict_registros)

def Read_Register():
    return

def Update_Register():
    return

def Delete_Register():
    return

def Export_Report():
    return

def Grouping():
    return

Create_Register()
