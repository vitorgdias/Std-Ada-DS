import datetime
import csv

def confere_data(data):
    try:
        return datetime.datetime.strptime(data, "%d/%m/%Y")
    except ValueError:
        return False

def converte_valor(valor):
    try:
      valor_convertido = float(valor)
      if valor_convertido == round(valor_convertido, 2):
        return valor_convertido
      else:
        print('Número inválido. Insira um número com até duas casas decimais.')
    except ValueError:
        print('Valor inválido. Por favor, digite um número.')

id_registro = 0
registros = []
registros_removidos = []

def menu():
  while True:
    escolha ='''
    ============== REGISTROS ==============
    [1] Criar cadastro
    [2] Atualizar registros
    [3] Consultar registros
    [4] Exportar registros
    [5] Sair
    =======================================
    O que você deseja? '''
    menu = ['1', '2', '3', '4']
    escolha = input(escolha)
    if escolha == '5':
      break
    elif escolha not in menu:
      print('\nPor favor escolha uma opção válida.')
      return menu()

    if escolha == '1':
      criar_cadastro()
    elif escolha == '2':
      atualizar_registros()
    elif escolha == '3':
      ler_registros()
    elif escolha == '4':
      exporta_registros()

def criar_cadastro():

  global id_registro
  while True:
    escolha ='''
    ============== CRIANDO CADASTRO ==============
    [1] Receita
    [2] Despesa
    [3] Investimento
    [4] Sair
    ==============================================
    O que você deseja? '''
    menu = ['1', '2', '3', '4']
    escolha = input(escolha)
    if escolha == '4':
      break
    elif escolha not in menu:
      print('\nPor favor escolha uma opção válida.')
      return criar_cadastro()
    data = input('\nPrimeiro insira a data (digite no formato dd/mm/aaaa): ')
    if confere_data(data):
      pass
    else:
      print('\n' + '='*55 + '\nData inválida, por gentileza entre com uma data válida.\n' + '='*55)
      return criar_cadastro()

    valor = input('Digite o valor do registro (Exemplo: 1234.56): ')
    if converte_valor(valor):
      valor = float(valor)
    else:
      return criar_cadastro()

    if escolha == '1':
      tipo = 'Receita'
      juros = None
    elif escolha == '2':
      tipo = 'Despesa'
      valor = -valor
      juros = None
    elif escolha == '3':
      tipo = 'Investimento'
      juros = input('\nDigite o valor da taxa de juros (apenas números): ')
      try:
         juros_convertido = float(juros)
         if juros_convertido:
            juros = float(juros)/100
      except ValueError:
        print('O valor digitado não é um número. Por gentileza digite um valor válido.')
        return criar_cadastro()

    registros.append({'ID':id_registro, 'tipo':tipo, 'data': data, 'valor':valor, 'juros': juros})
    print('\nRegistro criado com sucesso!\n')
    print(registros)
    id_registro += 1


def ler_registros():
  while True:
    escolha ='''
    ============== REGISTROS ==============
    [1] Consultar por data
    [2] Consultar por operação
    [3] Consultar por valor
    [4] Sair
    =======================================
    O que você deseja? '''
    menu = ['1', '2', '3', '4']
    escolha = input(escolha)
    if escolha == '4':
      break
    elif escolha not in menu:
      print('\nPor favor escolha uma opção válida.')
      return ler_registros()
    if escolha == '1':
      data = input('\nPrimeiro insira a data (digite no formato dd/mm/aaaa): ')

      if confere_data(data):
        pass
      else:
        print('\n' + '='*55 + '\nData inválida, por gentileza entre com uma data válida.\n' + '='*55)
        return ler_registros()

      chave = 'data'
      print(filtro(chave, data))
      return ler_registros()


    if escolha == '2':
      operacao = input('\nDigite a operação que você deseja consultar: (Receita, Despesa, Investimento)')
      chave = 'tipo'
      print(filtro(chave, operacao))
      return ler_registros()

    if escolha == '3':
      valor = float(input('\nDigite o valor que você deseja consultar: '))
      if converte_valor(valor):
        pass
      else:
        return ler_registros()
      chave = 'valor'
      print(filtro(chave, valor))
      return ler_registros()


def atualizar_registros():
  while True:
    escolha = '''\n
    ================ Atualizando registros... ================
    [1] Modificar registro
    [2] Deletar registro
    [3] Sair
    ==========================================================
    O que você deseja? '''
    menu = ['1', '2', '3', '4']
    escolha = input(escolha)
    if escolha == '3':
      break
    elif escolha not in menu:
      print('\nPor favor escolha uma opção válida.')
      return atualizar_registros()

    if escolha == '1':
      modificar_registros()
    elif escolha == '2':
      deletar_registro()


def modificar_registros():
  print(registros)
  try:
    id_para_modificar = int(input("Digite o ID do registro que deseja modificar: "))
  except ValueError:
    print("Por favor, digite um número válido.")
    modificar_registros()

  registro_encontrado = None

  for registro in registros:
    if registro['ID'] == id_para_modificar:
      registro_encontrado = registro
      break

  if registro_encontrado:
    pass
    print(f"Registro com ID {id_para_modificar} modificado com sucesso!")
  else:
    print(f"Nenhum registro encontrado com o ID {id_para_modificar}.")


def deletar_registro():
  print(registros)
  try:
    id_para_remover = int(input("Digite o ID do registro que deseja remover: "))
  except ValueError:
    print("Por favor, digite um número válido.")
    deletar_registro()

  registro_encontrado = None

  for registro in registros:
    if registro['ID'] == id_para_remover:
      registro_encontrado = registro
      break

  if registro_encontrado:
    registros.remove(registro_encontrado)
    registros_removidos.append(registro_encontrado)
    print(f"Registro com ID {id_para_remover} removido com sucesso!")
  else:
    print(f"Nenhum registro encontrado com o ID {id_para_remover}.")


def atualizar_investimentos():
  pass


def filtro(chave, valor):
    filtros = lambda registro : registro[chave] == valor
    registros_filtrados = list(filter(filtros, registros))
    return registros_filtrados

def exporta_registros():
    if not registros:
        print("Não há registros para exportar.")
        return
    with open('registros_ativos.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['ID', 'tipo', 'data', 'valor', 'juros'])
        writer.writeheader()
        for registro in registros:
            writer.writerow(registro)
    print("\nRegistros exportados com sucesso para 'registros_ativos.csv'.")


menu()