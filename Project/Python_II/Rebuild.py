import datetime
import csv
import os
import logging
from tabulate import tabulate

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Função para conferir se a data está no formato correto
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
            return None
    except ValueError:
        print('Valor inválido. Por favor, digite um número.')
        return None

# Função auxiliar para exibir o menu e capturar escolhas
def exibir_menu(opcoes, mensagem):
    while True:
        escolha = input(mensagem)
        if escolha in opcoes:
            return escolha
        else:
            logging.warning('Escolha inválida. Por favor, escolha uma opção válida.')

# Variáveis globais
id_registro = 0
registros = []
registros_removidos = []

# Função de carregamento de registros
def carregar_registros():
    global id_registro
    caminho_arquivo = 'registros.csv'
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['ID'] = int(row['ID'])
                row['valor'] = float(row['valor'])
                row['juros'] = float(row['juros']) if row['juros'] else None
                registros.append(row)
                id_registro = row['ID'] + 1  # Atualiza o ID para o próximo registro
        print("Registros carregados com sucesso!")
        print(tabulate(registros, headers="keys", tablefmt="pretty"))
    else:
        print("Nenhum arquivo de registros encontrado. Um novo arquivo será criado ao salvar.")

# Função principal de menu
def menu():
    while True:
        escolha = input('''
    ============== REGISTROS ==============
    [1] Criar cadastro
    [2] Atualizar registros
    [3] Consultar registros
    [4] Ver investimentos
    [5] Sair
    =======================================
    O que você deseja? ''')

        if escolha == '5':
            exporta_registros()
            break
        elif escolha == '1':
            criar_cadastro()
        elif escolha == '2':
            atualizar_registros()
        elif escolha == '3':
            ler_registros()
        elif escolha == '4':
            atualizar_investimentos()
        else:
            print('\nPor favor escolha uma opção válida.')

# Função para criar um novo cadastro
def criar_cadastro():
    global id_registro
    while True:
        escolha = input('''
    ============== CRIANDO CADASTRO ==============
    [1] Receita
    [2] Despesa
    [3] Investimento
    [4] Sair
    ==============================================
    O que você deseja? ''')

        if escolha == '4':
            break
        elif escolha not in ['1', '2', '3']:
            print('\nPor favor escolha uma opção válida.')
            continue

        data = input('\nPrimeiro insira a data (digite no formato dd/mm/aaaa): ')
        if not confere_data(data):
            print('\nData inválida, por gentileza entre com uma data válida.')
            continue

        valor = converte_valor(input('Digite o valor do registro (Exemplo: 1234.56): '))
        if valor is None:
            continue

        if escolha == '1':
            tipo = 'Receita'
            juros = None
        elif escolha == '2':
            tipo = 'Despesa'
            valor = -valor
            juros = None
        elif escolha == '3':
            tipo = 'Investimento'
            juros = converte_valor(input('Digite o valor da taxa de juros (apenas números): '))
            if juros is not None:
                juros /= 100
            else:
                continue

        registros.append({'ID': id_registro, 'tipo': tipo, 'data': data, 'valor': valor, 'juros': juros})
        print('\nRegistro criado com sucesso!\n')
        print(tabulate(registros, headers="keys", tablefmt="pretty"))
        id_registro += 1

# Função para ler registros
# Função para ler registros
def ler_registros():
    while True:
        mensagem_consulta = '''
        ============== REGISTROS ==============
        [1] Consultar por data
        [2] Consultar por operação
        [3] Consultar por valor
        [4] Ver estatísticas
        [5] Sair
        =======================================
        O que você deseja? '''

        escolha = exibir_menu(['1', '2', '3', '4', '5'], mensagem_consulta)

        if escolha == '5':
            break

        if escolha == '1':
            data = input('\nInsira a data (digite no formato dd/mm/aaaa): ')
            if not confere_data(data):
                logging.warning('Data inválida.')
                continue
            chave = 'data'
            registros_filtrados = filtro(chave, data)
        elif escolha == '2':
            operacao = input('\nDigite a operação (Receita, Despesa, Investimento): ')
            chave = 'tipo'
            registros_filtrados = filtro(chave, operacao)
        elif escolha == '3':
            valor = input('\nDigite o valor: ')
            valor_convertido = converte_valor(valor)
            if valor_convertido is None:
                continue
            chave = 'valor'
            registros_filtrados = filtro(chave, valor_convertido)
        elif escolha == '4':
            estatisticas()

        if escolha in ['1', '2', '3'] and registros_filtrados:
            # Exibindo os registros filtrados usando tabulate
            print(tabulate(registros_filtrados, headers="keys", tablefmt="pretty"))
        elif escolha in ['1', '2', '3']:
            logging.info("Nenhum registro encontrado.")

# Função para atualizar registros
def atualizar_registros():
    while True:
        mensagem_atualizar = '''\n
        ================ Atualizando registros... ================
        [1] Modificar registro
        [2] Deletar registro
        [3] Sair
        ==========================================================
        O que você deseja? '''
        
        escolha = exibir_menu(['1', '2', '3'], mensagem_atualizar)
        
        if escolha == '3':
            break
        elif escolha == '1':
            modificar_registros()
        elif escolha == '2':
            deletar_registro()

# Função para modificar registros
def modificar_registros():
    print(tabulate(registros, headers="keys", tablefmt="pretty"))
    try:
        id_para_modificar = int(input("Digite o ID do registro que deseja modificar: "))
    except ValueError:
        logging.error("Por favor, digite um número válido.")
        return

    registro_encontrado = next((reg for reg in registros if reg['ID'] == id_para_modificar), None)

    if registro_encontrado:
        while True:
            mensagem_modificar = '''
            ============== MODIFICANDO REGISTRO ==============
            [1] Modificar valor
            [2] Modificar tipo
            [3] Sair
            ==================================================
            O que você deseja? '''
            
            escolha = exibir_menu(['1', '2', '3'], mensagem_modificar)
            
            if escolha == '3':
                break
            elif escolha == '1':
                novo_valor = input("Digite o novo valor: ")
                valor_convertido = converte_valor(novo_valor)
                if valor_convertido is not None:
                    registro_encontrado['valor'] = valor_convertido
                    logging.info(f"Valor do registro modificado com sucesso: {registro_encontrado}")
            elif escolha == '2':
                novo_tipo = exibir_menu(['Receita', 'Despesa', 'Investimento'], "Digite o novo tipo: ")
                registro_encontrado['tipo'] = novo_tipo
                logging.info(f"Tipo do registro modificado com sucesso: {registro_encontrado}")

            # Atualiza a data do registro para a data atual
            registro_encontrado['data'] = datetime.datetime.now().strftime("%d/%m/%Y")
            logging.info(f"Data do registro atualizada para: {registro_encontrado['data']}")
            
    else:
        logging.warning(f"Nenhum registro encontrado com o ID {id_para_modificar}.")

# Função para deletar registros
def deletar_registro():
    print(tabulate(registros, headers="keys", tablefmt="pretty"))
    try:
        id_para_remover = int(input("Digite o ID do registro que deseja remover: "))
    except ValueError:
        logging.error("Por favor, digite um número válido.")
        return

    registro_encontrado = next((reg for reg in registros if reg['ID'] == id_para_remover), None)

    if registro_encontrado:
        registros.remove(registro_encontrado)
        registros_removidos.append(registro_encontrado)
        logging.info(f"Registro removido com sucesso: {registro_encontrado}")
    else:
        logging.warning(f"Nenhum registro encontrado com o ID {id_para_remover}.")

# Função para calcular juros compostos
def calcular_juros_compostos(valor_inicial, taxa_juros, dias):
    anos = dias / 365
    montante = valor_inicial * (1 + taxa_juros) ** anos
    return round(montante, 2)

# Função para atualizar investimentos
def atualizar_investimentos():
    investimentos = [reg for reg in registros if reg['tipo'] == 'Investimento']

    if not investimentos:
        logging.info("Não há registros de investimentos para atualizar.")
        return

    logging.info("Investimentos disponíveis:")
    print(tabulate(investimentos, headers="keys", tablefmt="pretty"))

    try:
        id_para_modificar = int(input("Digite o ID do investimento que deseja consultar: "))
    except ValueError:
        logging.error("Por favor, digite um número válido.")
        return

    registro_encontrado = next((reg for reg in registros if reg['ID'] == id_para_modificar and reg['tipo'] == 'Investimento'), None)

    if registro_encontrado:
        data_registro = datetime.datetime.strptime(registro_encontrado['data'], "%d/%m/%Y")
        data_atual = datetime.datetime.now()
        dias = (data_atual - data_registro).days

        montante_atual = calcular_juros_compostos(registro_encontrado['valor'], registro_encontrado['juros'], dias)

        registro_encontrado['valor'] = montante_atual
        registro_encontrado['data'] = data_atual.strftime("%d/%m/%Y")
        logging.info(f"Registro de investimento atualizado.")
        print()
        print(tabulate(registros, headers="keys", tablefmt="pretty"))
    else:
        logging.warning(f"Nenhum registro de investimento encontrado com o ID {id_para_modificar}.")

# Função para exportar registros
def exporta_registros():
    nome_arquivo = 'registros.csv'
    
    if os.path.exists(nome_arquivo):
        while True:
            sobrescrever = input("O arquivo já existe. Deseja sobrescrever? (s/n): ").lower()
            if sobrescrever == 'n':
                nome_arquivo = input("Digite o novo nome para o arquivo (sem extensão): ") + '.csv'
                break
            elif sobrescrever == 's':
                break
            else:
                logging.warning("Opção inválida, tente novamente.")
    
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        campos = ['ID', 'tipo', 'data', 'valor', 'juros']
        escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(registros)
    
    logging.info(f"Registros exportados com sucesso para {nome_arquivo}")

# Função para filtrar registros com base em uma chave e valor
def filtro(chave, valor):
    return [registro for registro in registros if registro[chave] == valor]

# Função para calcular estatísticas
def estatisticas():
    tipos = ['Receita', 'Despesa', 'Investimento']
    for tipo in tipos:
        registros_tipo = [reg['valor'] for reg in registros if reg['tipo'] == tipo]
        if registros_tipo:
            valor_max = max(registros_tipo)
            valor_min = min(registros_tipo)
            media = sum(registros_tipo) / len(registros_tipo)
            quantidade = len(registros_tipo)
            print(f"\nEstatísticas para {tipo}:")
            print(f"Valor máximo de {tipo}(s): {valor_max}")
            print(f"Valor mínimo de {tipo}(s): {valor_min}")
            print(f"Média de {tipo}(s): {round(media, 2)}")
            print(f"Quantidade de {tipo}(s): {quantidade}")
            print('='*50)
        else:
            print(f"\nNenhum registro encontrado para {tipo}.")

# Execução do programa
carregar_registros()
menu()