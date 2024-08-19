import streamlit as st
import datetime
import csv
import os

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
            st.error('Número inválido. Insira um número com até duas casas decimais.')
    except ValueError:
        st.error('Valor inválido. Por favor, digite um número.')

id_registro = 0
registros = []
registros_removidos = []

def criar_cadastro():
    global id_registro

    escolha = st.selectbox('O que você deseja?', ['Receita', 'Despesa', 'Investimento'])

    data = st.text_input('Insira a data (dd/mm/aaaa):')
    if confere_data(data):
        valor = st.text_input('Digite o valor do registro (Exemplo: 1234.56):')
        valor = converte_valor(valor)

        if valor is not None:
            if escolha == 'Receita':
                tipo = 'Receita'
                juros = None
            elif escolha == 'Despesa':
                tipo = 'Despesa'
                valor = -valor
                juros = None
            elif escolha == 'Investimento':
                tipo = 'Investimento'
                juros = st.text_input('Digite o valor da taxa de juros (apenas números):')
                try:
                    juros = float(juros) / 100
                except ValueError:
                    st.error('O valor digitado não é um número válido.')

            registros.append({'ID': id_registro, 'tipo': tipo, 'data': data, 'valor': valor, 'juros': juros})
            st.success('Registro criado com sucesso!')
            id_registro += 1
            st.write(registros)
    else:
        st.error('Data inválida, por gentileza entre com uma data válida.')

def ler_registros():
    escolha = st.selectbox('Consultar por', ['Data', 'Operação', 'Valor'])
    
    if escolha == 'Data':
        data = st.text_input('Insira a data (dd/mm/aaaa):')
        if confere_data(data):
            chave = 'data'
            st.write(filtro(chave, data))
        else:
            st.error('Data inválida, por gentileza entre com uma data válida.')

    elif escolha == 'Operação':
        operacao = st.text_input('Digite a operação que você deseja consultar: (Receita, Despesa, Investimento)')
        chave = 'tipo'
        st.write(filtro(chave, operacao))

    elif escolha == 'Valor':
        valor = st.text_input('Digite o valor que você deseja consultar:')
        valor = converte_valor(valor)
        if valor is not None:
            chave = 'valor'
            st.write(filtro(chave, valor))

def atualizar_registros():
    escolha = st.selectbox('O que você deseja?', ['Modificar registro', 'Deletar registro'])

    if escolha == 'Modificar registro':
        modificar_registros()
    elif escolha == 'Deletar registro':
        deletar_registro()

def modificar_registros():
    st.write(registros)
    id_para_modificar = st.text_input("Digite o ID do registro que deseja modificar:")
    
    if id_para_modificar:
        try:
            id_para_modificar = int(id_para_modificar)
        except ValueError:
            st.error("Por favor, digite um número válido.")
            return

        registro_encontrado = next((registro for registro in registros if registro['ID'] == id_para_modificar), None)

        if registro_encontrado:
            novo_valor = st.text_input("Digite o novo valor:")
            if novo_valor:
                novo_valor = converte_valor(novo_valor)
                if novo_valor is not None:
                    registro_encontrado['valor'] = novo_valor
                    st.success(f"Registro com ID {id_para_modificar} modificado com sucesso!")
                    st.write(registro_encontrado)

            novo_tipo = st.selectbox("Digite o novo tipo:", ['Receita', 'Despesa', 'Investimento'])
            if novo_tipo:
                registro_encontrado['tipo'] = novo_tipo
                if novo_tipo == 'Investimento':
                    novo_juros = st.text_input('Digite o novo valor da taxa de juros (apenas números):')
                    if novo_juros:
                        try:
                            novo_juros = float(novo_juros) / 100
                            registro_encontrado['juros'] = novo_juros
                        except ValueError:
                            st.error('O valor digitado não é um número válido.')
            st.success(f"Registro com ID {id_para_modificar} modificado com sucesso!")
        else:
            st.error(f"Nenhum registro encontrado com o ID {id_para_modificar}.")

def deletar_registro():
    st.write(registros)
    id_para_remover = st.text_input("Digite o ID do registro que deseja remover:")

    if id_para_remover:
        try:
            id_para_remover = int(id_para_remover)
        except ValueError:
            st.error("Por favor, digite um número válido.")
            return

        registro_encontrado = next((registro for registro in registros if registro['ID'] == id_para_remover), None)

        if registro_encontrado:
            registros.remove(registro_encontrado)
            registros_removidos.append(registro_encontrado)
            st.success(f"Registro com ID {id_para_remover} removido com sucesso!")
        else:
            st.error(f"Nenhum registro encontrado com o ID {id_para_remover}.")

def calcular_juros_compostos(valor_inicial, taxa_juros, dias):
    anos = dias / 365
    montante = valor_inicial * (1 + taxa_juros) ** anos
    return round(montante, 2)

def atualizar_investimentos():
    investimentos = [reg for reg in registros if reg['tipo'] == 'Investimento']

    if not investimentos:
        st.info("Não há registros de investimentos para atualizar.")
        return

    st.write("\nInvestimentos disponíveis:\n")
    st.write(investimentos)

    id_para_modificar = st.text_input("Digite o ID do investimento que deseja consultar:")

    if id_para_modificar:
        try:
            id_para_modificar = int(id_para_modificar)
        except ValueError:
            st.error("Por favor, digite um número válido.")
            return

        registro_encontrado = next((registro for registro in registros if registro['ID'] == id_para_modificar and registro['tipo'] == 'Investimento'), None)

        if registro_encontrado:
            st.write(f"\nRegistro encontrado: {registro_encontrado}")

            data_registro = datetime.datetime.strptime(registro_encontrado['data'], "%d/%m/%Y")
            data_atual = datetime.datetime.now()
            dias = (data_atual - data_registro).days

            montante_atual = calcular_juros_compostos(registro_encontrado['valor'], registro_encontrado['juros'], dias)

            st.write(f"Valor atual do investimento: {montante_atual}")

            registro_encontrado['valor'] = montante_atual
            registro_encontrado['data'] = data_atual.strftime("%d/%m/%Y")

            st.success(f"\nRegistro de investimento com ID {id_para_modificar} atualizado com sucesso!")
            st.write(f"Novo valor: {registro_encontrado['valor']}\nNova data: {registro_encontrado['data']}")
        else:
            st.error(f"Nenhum registro de investimento encontrado com o ID {id_para_modificar}.")

def filtro(chave, valor):
    registros_filtrados = [registro for registro in registros if registro[chave] == valor]
    return registros_filtrados

def exporta_registros():
    if not registros:
        st.info("Não há registros para exportar.")
        return
    with open('registros_ativos.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['ID', 'tipo', 'data', 'valor', 'juros'])
        writer.writeheader()
        for registro in registros:
            writer.writerow(registro)
    st.success("Registros exportados com sucesso para 'registros_ativos.csv'.")

def carregar_registros():
    global id_registro
    caminho_arquivo = 'registros_ativos.csv'
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['ID'] = int(row['ID'])
                row['valor'] = float(row['valor'])
                if row['juros']:
                    row['juros'] = float(row['juros'])
                else:
                    row['juros'] = None
                id_registro = row['ID'] + 1
                registros.append(row)
            st.success("Registros carregados com sucesso!")
    else:
        st.info("Nenhum arquivo de registros encontrado. Um novo arquivo será criado ao colocar dados.")

def main():
    carregar_registros()

    menu = st.sidebar.selectbox("Menu", ["Criar Cadastro", "Consultar Registros", "Atualizar Registros", "Atualizar Investimentos", "Exportar Registros", "Sair"])

    if menu == "Criar Cadastro":
        criar_cadastro()

    elif menu == "Consultar Registros":
        ler_registros()

    elif menu == "Atualizar Registros":
        atualizar_registros()

    elif menu == "Atualizar Investimentos":
        atualizar_investimentos()

    elif menu == "Exportar Registros":
        exporta_registros()

    elif menu == "Sair":
        st.write("Obrigado por utilizar o sistema financeiro!")

if __name__ == "__main__":
    main()