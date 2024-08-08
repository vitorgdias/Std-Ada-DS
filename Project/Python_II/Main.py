from Product import Create_Register

def active_system():
    while True:
        print('\nBem-vindo(a) ao sistema "Nome do Sistema".')
        print('1. Criar Registro')
        print('2. Ler Registro')
        print('3. Atualizar Registro')
        print('4. Deletar Registro')
        print('5. Sair')
        option = input('Selecione uma das opções acima de 1 à 5: ')
        if  option == '1':
            Create_Register()
        else:
            break

if __name__ == '__main__':
    active_system()



