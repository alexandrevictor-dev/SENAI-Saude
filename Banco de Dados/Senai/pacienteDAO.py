from dic import generos
from nav_padrao import limpar_tela, delay, converter_data, converter_data_banco
from tabulate import tabulate
from IPython.core.display_functions import display

def cadastrar_paciente(conexao, cursor):
    print("-=-= CADASTRO DE PACIENTE =-=-\n")
    cpf = input("CPF: ")

    sql = "SELECT ID FROM PACIENTE WHERE CPF = %s"
    cursor.execute(sql, (cpf,))
    resultado = cursor.fetchall()  # retorna para resultado; todas as linhas retornadas pela execução da query

    if len(resultado) != 0:  # se o tamanho da lista retornada para o banco for diferente de 0:
        print("CPF já cadastrado para outro paciente.")

    else:
        rg = input("RG: ")

        sql = "SELECT ID FROM PACIENTE WHERE RG = %s"
        cursor.execute(sql, (rg,))
        resultado = cursor.fetchall()

        if len(resultado) != 0:
            print("RG já cadastrado para outro paciente.")

        else:

            nome = input("Nome: ")
            endereco = input("Endereço: ")
            cep = input("CEP: ")
            dt_nasc = converter_data_banco(input("Data de Nascimento(DD/MM/YYYY): "))


            while True:
                print("\nGênero: ")
                for chave, valor in generos.items():
                    print(f"{chave} - {valor}")

                chave_genero = int(input("\nEscolha uma opção: "))

                if chave_genero not in generos:
                    print("Opção Inválida!")
                    delay()
                    limpar_tela()

                else:
                    break

            telefone = input("Telefone: ")
            email = input("E-mail: ")
            responsavel = input("O paciente necessita de um responsável(S/N)? ")
            if responsavel.upper() == 'S':
                responsavel = input("Digite o nome do responsável: ")
            else:
                responsavel = None

            sql = '''INSERT INTO paciente (CPF, RG, NOME, ENDERECO, CEP, DT_NASC, GENERO, TELEFONE, EMAIL, RESPONSAVEL) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            valores = (cpf, rg, nome, endereco, cep, dt_nasc,
                       chave_genero, telefone, email, responsavel)

            try:
                cursor.execute(sql, valores)
                conexao.commit()  # confirma a transação no SGBD
                print(f"Paciente  {nome} cadastrado com sucesso!")

            except Exception as e:
                print(f"Erro: {e}")

def excluir_paciente(conexao, cursor):
    print("-=-= EXCLUSÃO DE PACIENTE =-=-\n")
    cpf = input("CPF: ")

    try:
        sql = "SELECT ID, NOME FROM PACIENTE WHERE CPF = %s"
        cursor.execute(sql, (cpf,))
        resultado = cursor.fetchall()  # retorna para resultado; todas as linhas retornadas pela execução da query

        if len(resultado) == 0:
            print("Paciente não encontrado.")
            delay()

        else:
            id_paciente = resultado[0][0]
            nome_paciente = resultado[0][1]

            op_exclusao = int(
                input(f"\nDeseja excluir o paciente {nome_paciente}?\n1. Sim\n2. Não\n\nEscolha uma opção: "))

            if op_exclusao == 1:
                sql = "DELETE FROM PACIENTE WHERE ID = %s"
                cursor.execute(sql, (id_paciente,))
                conexao.commit()
                input(f"\nPciente {nome_paciente} excluído\nPressione enter para continuar.")

            elif op_exclusao == 2:
                print("Retornando ao menu principal")
                delay()

            else:
                print("Opção inválida.")
                delay()
    except Exception as e:
        print("Erro ", e)

def consultar_todos_pacientes(cursor):
    try:
        sql = '''SELECT CPF, RG, NOME, ENDERECO, CEP, DT_NASC, GENERO, TELEFONE, EMAIL, RESPONSAVEL FROM PACIENTE
        ORDER BY NOME ASC'''
        cursor.execute(sql)
        resultado = cursor.fetchall()

        if len(resultado) == 0:
            print("Não há pacientes cadastrados no Sistema!")
            delay()

        else:
            resultados = []

            for item in resultado:
                item = list(item)

                item[5] = converter_data(item[5])

                chave_genero = item[6]
                item[6] = generos.get(chave_genero)

                resultados.append(item)

            colunas = ['CPF','RG', 'NOME', 'ENDEREÇO', 'CEP', 'DT NASCIMENTO', 'GÊNERO', 'TELEFONE', 'E-MAIL', 'RESPONSÁVEL']
            tabela = tabulate(resultados, headers=colunas, tablefmt='grid')
            display(tabela)
            input("\nPressione Enter para continuar...")

    except Exception as e:
        print("Erro: ", e)

def consultar_por_cpf(cursor):
    cpf_procurado = input("CPF: ")
    try:
        sql = '''SELECT 
            CPF, RG, NOME, ENDERECO, CEP, DT_NASC, GENERO, TELEFONE, EMAIL, RESPONSAVEL
            FROM PACIENTE
            WHERE CPF = %s'''
        cursor.execute(sql,(cpf_procurado,))
        resultado = cursor.fetchall()

        if len(resultado) == 0:
            print("Paciente não encontrado!")
            delay()

        else:
            resultados = []

            for item in resultado:
                item = list(item)
                resultados.append(item)

                item[5] = converter_data(item[5])

                chave_genero = item[6]
                item[6] = generos.get(chave_genero)


            colunas = ['CPF', 'RG', 'NOME', 'ENDEREÇO', 'CEP', 'DATA DE NASCIMENTO','GENERO','TELEFONE','E-MAIL','RESPONSÁVEL']
            tabela = tabulate(resultados, headers=colunas, tablefmt='grid')
            display(tabela)
            input("\nPressione Enter para continuar...")

    except Exception as e:
        print("Erro: ", e)

def editar_paciente(conexao, cursor):
    print(" -=-=EDIÇÃO DE PACIENTE=-=- ")
    cpf = input("CPF: ")

    try:
        sql = "SELECT ID, CPF, RG FROM PACIENTE WHERE CPF = %s"
        cursor.execute(sql, (cpf,))
        resultado = cursor.fetchall()
        limpar_tela()
        if len(resultado) == 0:
            print("Paciente não  encontrado!")
            delay()

        else:
            id_paciente = resultado [0][0]
            cpf_atual = resultado[0][1]
            rg_atual = resultado[0][2]
            novo_cpf = input("Novo CPF: ")
            cursor.execute(sql, (novo_cpf,))
            resultado = cursor.fetchall()

            '''O sistema deverá permitir a edição se o novo CPF digitado foi igual ao CPF
            já cadastrado para esse paciente ou se o novo CPF não estiver vinculado a nenhum
            outro paciente no banco de dados.'''

            if len(resultado) != 0 and cpf_atual != novo_cpf:
                limpar_tela()
                print("CPF já cadastrado para outro paciente!")
                delay()

            else:
                novo_rg = input("Novo RG: ")
                '''O sistema deverá permitir a edição se o novo RG digitado for igual ao RG já
                cadastrado para este paciente ou se o novo RG não estiver vinculado a nenhum outro 
                paciente no banco de dados'''

                sql = "SELECT RG FROM PACIENTE WHERE RG = %s"
                cursor.execute(sql, (novo_rg,))
                resultado = cursor.fetchall()

                if len(resultado) != 0 and novo_rg != rg_atual:
                    limpar_tela()
                    print("RG já cadastrado para outro paciente!")
                    delay()

                else:
                    nome = input("Nome: ")
                    endereco = input("Endereço: ")
                    cep = input("CEP: ")
                    dt_nasc = converter_data_banco(input("Data de Nascimento(DD/MM/YYYY): "))

                    while True:
                        print("\nGênero: ")
                        for chave, valor in generos.items():
                            print(f"{chave} - {valor}")

                        chave_genero = int(input("\nEscolha uma opção: "))

                        if chave_genero not in generos:
                            print("Opção Inválida!")
                            delay()
                            limpar_tela()

                        else:
                            break

                    telefone = input("Telefone: ")
                    email = input("E-mail: ")
                    responsavel = input("O paciente necessita de um responsável(S/N)? ")
                    if responsavel.upper() == 'S':
                        responsavel = input("Digite o nome do responsável: ")
                    else:
                        responsavel = None

                sql = '''UPDATE PACIENTE
                        SET CPF = %s, RG = %s, NOME = %s, ENDERECO = %s, CEP = %s, DT_NASC = %s, GENERO = %s,
                        TELEFONE = %s, EMAIL = %s, RESPONSAVEL = %s
                        WHERE ID = %s'''

                valores = (novo_cpf, novo_rg, nome, endereco, cep, dt_nasc, chave_genero, telefone, email, responsavel, id_paciente)

                cursor.execute(sql, valores)
                conexao.commit()
                limpar_tela()
                print(cursor.rowcount, "registro alterado.")
    except Exception as e:
        print("Erro: ", e)

def relatorio_paciente(cursor):
    try:
        sql = '''SELECT DISTINCT
            
            PACIENTE.NOME AS PACIENTE, 
            PACIENTE.DT_NASC,
            PACIENTE.CPF,
            COUNT(CONSULTA.ID)
            
            FROM CONSULTA

            INNER JOIN PACIENTE ON CONSULTA.ID_PACIENTE = PACIENTE.ID 

            ORDER BY PACIENTE.NOME ASC'''
        # Inner join: COMPARA 2 TABELAS
        cursor.execute(sql)
        resultado = cursor.fetchall()

        if len(resultado) == 0:
            print("Não há consultas cadastradas no Sistema!")
            delay()

        else:
            resultados = []

            for item in resultado:
                item = list(item)
                resultados.append(item)
                item[1] = converter_data(item[1])

            colunas = ['Nome', 'DT Nascimento', 'CPF', 'QTD. Consultas']
            tabela = tabulate(resultados, headers=colunas, tablefmt='grid')
            display(tabela)
            input("\nPressione Enter para continuar...")

    except Exception as e:
        print("Erro: ", e)


'''relatório de pacientes que possuem consultas marcadas
Relatório deverá trazer na tela:
 - Nome do Paciente
 - Data de Nascimento
 - Código da Consulta
 - Data da Consulta
 - Hora da Consulta
 
 Em ordem alfabética'''

