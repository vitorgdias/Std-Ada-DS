from Product import *

def active_system():
    while True:
        registros = create_register()
        print('\nBem-vindo(a) ao sistema "Nome do Sistema".')
        print('='*50)
        print('1. Criar Registro')
        print('2. Ler Registro')
        print('3. Atualizar Registro')
        print('4. Deletar Registro')
        print('5. Exportar Relatório')
        print('6. Sair')
        option = input('\nSelecione uma das opções acima de 1 à 6: ')
        if  option == '1':
            create_register()
        elif option == '2':
            read_register()
        elif option == '3':
            update_register()
        elif option == '4':
            delete_register()
        elif option == '5':
            export_report()
        elif option == '6':
            print('\n'+'='*45)
            print('Obrigado por utilizar o "Nome do Sistema".')
            print('='*45+'\n')
            print(registros)
            break
        else:
            print('\nOpção inválida, por favor insira uma opção válida.')

if __name__ == '__main__':
    active_system()