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

def grouping():
    return

def csv_export():
    return

def json_export():
    return