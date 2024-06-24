from dic import especialidades
from nav_padrao import limpar_tela, delay, converter_data, converter_data_banco
from tabulate import tabulate
from IPython.core.display_functions import display


def cadastrar_medico(conexao, cursor):
    print("-=-= CADASTRO DE MÉDICOS =-=-")

    crm = input("CRM: ")

    sql = "SELECT ID FROM MEDICO WHERE CRM = %s"
    cursor.execute(sql, (crm,))
    resultado = cursor.fetchall()

    if len(resultado) != 0:
        print("CRM já cadastrado em outro médico!")
        delay()

    else:
        rg = input("RG: ")

        sql = "SELECT ID FROM MEDICO WHERE RG = %s"
        cursor.execute(sql, (rg,))
        resultado = cursor.fetchall()

        if len(resultado) != 0:
            print("RG já cadastrado em outro médico!")
            delay()

        else:

            cpf = input("CPF: ")

            sql = "SELECT ID FROM MEDICO WHERE CPF = %s"
            cursor.execute(sql, (cpf,))
            resultado = cursor.fetchall()

            if len(resultado) != 0:
                print("CPF já cadastrado em outro médico!")
                delay()

            else:

                nome = input("Nome: ")
                email = input("E-mail: ")
                endereco = input("Endereço: ")
                cep = input("CEP: ")

                while True:
                    print("\nEspecialidade Médica: ")
                    for chave, valor in especialidades.items():
                        print(f"{chave} - {valor}")

                    chave_esp_medica = int(input("\nEscolha uma opção: "))

                    if chave_esp_medica not in especialidades:
                        print("Opção Inválida!")
                        delay()
                        limpar_tela()

                    else:
                        break

                dt_nasc = converter_data_banco(input("Data de nascimento (DD/MM/YYYYY): "))
                dt_admissao = converter_data_banco(input("Data de admissão (DD/MM/YYYYY): "))
                dt_desligamento = None

                sql = '''INSERT INTO medico (CRM, NOME, RG, CPF, EMAIL, ENDERECO, CEP, ESP_MEDICA, DT_NASC, DT_ADMISSAO)   
                                                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
                valores = (crm, nome, rg, cpf, email, endereco, cep, chave_esp_medica, dt_nasc, dt_admissao)

                try:
                    cursor.execute(sql, valores)
                    conexao.commit()  # Confirmar a transação no SGBD
                    print(f"Médico {nome} cadastrado com sucesso!")

                except Exception as e:
                    print(f"Erro: {e}")


def excluir_medico(conexao, cursor):
    print("-=-= EXCLUSÃO DE MÉDICO =-=-\n")
    cpf = input("CRM: ")

    try:
        sql = "SELECT ID, NOME FROM MEDICO WHERE CRM = %s"
        cursor.execute(sql, (cpf,))
        resultado = cursor.fetchall()  # retorna para resultado; todas as linhas retornadas pela execução da query

        if len(resultado) == 0:
            print("Médico não encontrado.")
            delay()

        else:
            id_medico = resultado[0][0]
            nome_medico = resultado[0][1]

            op_exclusao = int(
                input(f"\nDeseja excluir o médico {nome_medico}?\n1. Sim\n2. Não\n\nEscolha uma opção: "))

            if op_exclusao == 1:
                sql = "DELETE FROM MEDICO WHERE ID = %s"
                cursor.execute(sql, (id_medico,))
                conexao.commit()
                input(f"\nPaciente {nome_medico} excluído\nPressione enter para continuar.")

            elif op_exclusao == 2:
                print("Retornando ao menu principal")
                delay()

            else:
                print("Opção inválida.")
                delay()
    except Exception as e:
        print("Erro ", e)


def consultar_todos_medicos(cursor):
    try:
        sql = '''SELECT CRM, NOME, RG, CPF, EMAIL, ENDERECO, CEP, ESP_MEDICA, DT_NASC, DT_ADMISSAO, DT_DESLIGAMENTO, STATUS_MEDICO 
        FROM MEDICO
        ORDER BY NOME ASC'''
        cursor.execute(sql)
        resultado = cursor.fetchall()

        if len(resultado) == 0:
            print("Não há médicos cadastrados no Sistema!")
            delay()

        else:
            resultados = []

            for item in resultado:
                item = list(item)

                item[8] = converter_data(item[8])
                item[9] = converter_data(item[9])
                item[10] = converter_data(item[10])

                chave_esp = item[7]
                item[7] = especialidades.get(chave_esp)   #GET -> Pega os valores do dic (dicionário)

                resultados.append(item)

            colunas = ['CRM', 'NOME', 'RG', 'CPF', 'E-MAIL', 'ENDEREÇO', 'CEP', 'ESPECIALIDADE', 'DATA NASCIMENTO','DATA ADMISSÃO','DATA DESLIGAMENTO', 'STATUS MÉDICO']
            tabela = tabulate(resultados, headers=colunas, tablefmt='grid')
            display(tabela)
            input("\nPressione Enter para continuar...")

    except Exception as e:
        print("Erro: ", e)


def consultar_por_crm(cursor):
    crm_procurado = input("CRM: ")
    try:
        sql = '''SELECT CRM, NOME, RG, CPF, EMAIL, ENDERECO, CEP, ESP_MEDICA, DT_NASC, DT_ADMISSAO, DT_DESLIGAMENTO, STATUS_MEDICO 
                        FROM MEDICO
                    WHERE CRM = %s'''
        cursor.execute(sql,(crm_procurado,))
        resultado = cursor.fetchall()

        if len(resultado) == 0:
            print("Médico não encontrado!")
            delay()

        else:
            resultados = []

            for item in resultado:
                item = list(item)

                item[8] = converter_data(item[8])
                item[9] = converter_data(item[9])
                item[10] = converter_data(item[10])

                chave_esp = item[7]
                item[7] = especialidades.get(chave_esp)

                resultados.append(item)


            colunas = ['CRM', 'NOME', 'RG', 'CPF', 'E-MAIL', 'ENDEREÇO', 'CEP', 'ESPECIALIDADE', 'DATA NASCIMENTO','DATA ADMISSÃO','DATA DESLIGAMENTO', 'STATUS MÉDICO']
            tabela = tabulate(resultados, headers=colunas, tablefmt='grid')
            display(tabela)
            input("\nPressione Enter para continuar...")

    except Exception as e:
        print("Erro: ", e)


def inativar_medico(conexao, cursor):
    def inativar_medico(conexao, cursor):
        print(" -=-=INATIVAR MÉDICO=-=- \n")

        crm = input("CRM: ")

        try:
            sql = "SELECT ID, NOME FROM MEDICO WHERE CRM = %s"
            cursor.execute(sql, (crm,))
            resultado = cursor.fetchall()  # vai gravar nos resultado todas as linhas retornadas pela execução da query
            if len(resultado) == 0:
                print("Médico não encontrado!")
                delay()

            else:
                id_medico = resultado[0][0]
                nome_medico = resultado[0][1]
                sql = "SELECT STATUS_MEDICO FROM MEDICO WHERE ID = %s;"
                cursor.execute(sql, (id_medico,))
                resultado = cursor.fetchall()
                status_medico = resultado[0][0]

                if status_medico == 'Inativo':
                    limpar_tela()
                    input("Médico já está Inativo no Sistema.\n\n Pressione entrer para continuar...")

                else:
                    op_desligamento = int(
                        input(f"Deseja desligar o Médico {nome_medico}?\n1.Sim 2.Não\n\n Escolha uma opção: "))

                    if op_desligamento == 1:
                        data_desligamento = converter_data_banco(input("Data Desligamento (DD/MM/AAAA): "))
                        sql = "SELECT DATA_CONSULTA FROM CONSULTA WHERE ID_MEDICO = %s AND DATA_CONSULTA >=%s;"
                        cursor.execute(sql, (id_medico, data_desligamento))
                        resultado = cursor.fetchall()

                        if len(resultado) != 0:
                            print("Médico não poderá ser desligado, pois possui consultas vinculadas ao seu cadastro "
                                  "com data igual ou maior à data inserida para o desligamento.\n\n"
                                  "Pressione enter para retornar...")

                        else:
                            sql = "UPDATE MEDICO SET DATA_DESLIGAMENTO = %s WHERE ID = %s;"
                            cursor.execute(sql, (data_desligamento, id_medico))
                            conexao.commit()
                            limpar_tela()
                            print(f"O médico{nome_medico} foi inativo!")
                            delay()

                    elif op_desligamento == 2:
                        limpar_tela()
                        print("Retornando...")
                        delay()

                    else:
                        limpar_tela()
                        print("Opção inválida!")
                        delay()

        except Exception as e:
            print("Erro:", e)

    # definir reativar medico #igual o inativar mas com algumas diferenças
