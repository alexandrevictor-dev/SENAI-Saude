from nav_padrao import limpar_tela, delay, converter_data, converter_data_banco
from tabulate import tabulate
from IPython.core.display_functions import display

def cadastrar_consulta(conexao, cursor):
    print("-=-= CADASTRO DE CONSULTA =-=-\n")

    while True:
        crm_medico = input("CRM do Médico: ")

        sql = "SELECT ID FROM MEDICO WHERE CRM = %s"
        cursor.execute(sql, (crm_medico,))
        resultado = cursor.fetchall()

        if len(resultado) == 0:
            print("Médico não encontrado!")
            delay()

        else:
            id_medico = resultado[0][0]

            sql = "SELECT STATUS_MEDICO FROM MEDICO WHERE ID = %s"
            cursor.execute(sql, (id_medico,))
            resultado = cursor.fetchall()
            status_medico = resultado[0][0]

            if status_medico == 'Inativo':
                print("Não é possível marcar consulta para este médico, pois ele possui status Inativo!")
                delay()

            else:
                cpf_paciente = input("CPF do paciente: ")

                sql = "SELECT ID FROM PACIENTE WHERE CPF = %s"
                cursor.execute(sql, (cpf_paciente,))
                resultado = cursor.fetchall()

                if len(resultado) == 0:
                    limpar_tela()
                    print("Paciente não encontrado!")
                    delay()
                    limpar_tela()

                else:
                    id_paciente = resultado[0][0]
                    cod_consulta = input("Código da Consulta: ")

                    sql = "SELECT ID FROM CONSULTA WHERE COD_CONSULTA = %s"
                    cursor.execute(sql, (cod_consulta,))
                    resultado = cursor.fetchall()

                    if len(resultado) != 0:
                        limpar_tela()
                        print("Já existe consulta cadastrada com este código! Tente novamente...")
                        delay()

                    else:
                        dt_consulta = converter_data_banco(input("Data da Consulta (DD/MM/YYYY): "))
                        hr_consulta = input("Hora da Consulta (HH:MM:SS): ")
                        # Adicionar tratamento para inserção de DATA e HORA
                        # Adicionar validação para DATA E HORA disponíveis (medico e paciente)

                        vr_consulta = float(input("Valor da Consulta: "))

                        sql = '''INSERT INTO CONSULTA(COD_CONSULTA, DT_CONSULTA, HR_CONSULTA, 
                                                VR_CONSULTA, ID_MEDICO, ID_PACIENTE) VALUES (%s, %s, %s, %s, %s, %s)'''
                        valores = (cod_consulta, dt_consulta, hr_consulta, vr_consulta, id_medico, id_paciente)

                        cursor.execute(sql, valores)
                        conexao.commit()
                        print("Consulta cadastrada com sucesso!")

                        # INSERIR ESTRUTURA TRY-EXCEPT

def excluir_consulta(conexao, cursor):
    print("-=-= EXCLUSÃO DE CONSULTA =-=-\n")
    cod_consulta = input("Código da Consulta: ")

    try:
        sql = "SELECT ID, NOME FROM CONSULTA WHERE COD_CONSULTA = %s"
        cursor.execute(sql, (cod_consulta,))
        resultado = cursor.fetchall()  # retorna para resultado; todas as linhas retornadas pela execução da query

        if len(resultado) == 0:
            print("Consulta não encontrado.")
            delay()

        else:
            id_consulta = resultado[0][0]

            op_exclusao = int(input(f"\nDeseja excluir a consulta {cod_consulta}?\n1. Sim\n2. Não\n\nEscolha uma opção: "))

            if op_exclusao == 1:
                sql = "DELETE FROM CONSULTA WHERE ID = %s"
                cursor.execute(sql, (id_consulta,))
                conexao.commit()
                print(f"Consulta {cod_consulta} excluída com sucesso!")
                delay()

            elif op_exclusao == 2:
                print("Consulta não excluída. Retornando ao menu...")
                delay()

            else:
                print("Opção inválida.")
                delay()

    except Exception as e:
        print("Erro ", e)

def visualizar_todas_consultas(cursor):
    try:
        sql = '''SELECT 
            CONSULTA.COD_CONSULTA, 
            CONSULTA.DT_CONSULTA, 
            CONSULTA.HR_CONSULTA, 
            CONSULTA.VR_CONSULTA, 
            MEDICO.NOME AS MEDICO,
            PACIENTE.NOME AS PACIENTE
            
            FROM CONSULTA
            
            INNER JOIN MEDICO ON CONSULTA.ID_MEDICO = MEDICO.ID
            INNER JOIN PACIENTE ON CONSULTA.ID_PACIENTE = PACIENTE.ID
            
            ORDER BY DT_CONSULTA, HR_CONSULTA'''
        cursor.execute(sql)
        resultado = cursor.fetchall()

        if len(resultado) == 0:
            print("Não há consultas cadastradas no Sistema!")
            delay()

        else:
            resultados = []

            for item in resultado:
                item = list(item)

                item[1] = converter_data(item[1])

                resultados.append(item)

            colunas = ['Cód. Consulta', 'DT Consulta', 'Hr Consulta', 'Vr Consulta', 'Médico', 'Paciente']
            tabela = tabulate(resultados, headers=colunas, tablefmt='grid')
            display(tabela)
            input("\nPressione Enter para continuar...")

    except Exception as e:
        print("Erro: ", e)

def consultar_por_codigo(cursor):
    codigo_procurado = input("Código da Consulta: ")
    try:
        sql = '''SELECT 
                    CONSULTA.COD_CONSULTA, 
                    CONSULTA.DT_CONSULTA, 
                    CONSULTA.HR_CONSULTA, 
                    CONSULTA.VR_CONSULTA, 
                    MEDICO.NOME AS MEDICO,
                    PACIENTE.NOME AS PACIENTE


                    FROM CONSULTA
                    
                    INNER JOIN MEDICO ON CONSULTA.ID_MEDICO = MEDICO.ID
                    INNER JOIN PACIENTE ON CONSULTA.ID_PACIENTE = PACIENTE.ID
                    
                    WHERE CONSULTA.COD_CONSULTA = %s'''
        cursor.execute(sql,(codigo_procurado,))
        resultado = cursor.fetchall()

        if len(resultado) == 0:
            print("Consulta não encontrada!")
            delay()

        else:
            resultados = []

            for item in resultado:
                item = list(item)

                item[1] = converter_data(item[1])

                resultados.append(item)

            colunas = ['Cód. Consulta', 'DT Consulta', 'Hr Consulta', 'Vr Consulta', 'Médico', 'Paciente']
            tabela = tabulate(resultados, headers=colunas, tablefmt='grid')
            display(tabela)
            input("\nPressione Enter para continuar...")

    except Exception as e:
        print("Erro: ", e)