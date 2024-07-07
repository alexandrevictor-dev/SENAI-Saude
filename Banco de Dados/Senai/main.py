import conexao
from nav_padrao import limpar_tela, delay
from pacienteDAO import cadastrar_paciente, excluir_paciente, consultar_todos_pacientes, consultar_por_cpf, editar_paciente, relatorio_paciente, relatorio_paciente_consultas_marcadas
from medicoDAO import cadastrar_medico, excluir_medico, consultar_todos_medicos, consultar_por_crm, inativar_medico, ativar_medico, editar_medico, relatorio_especialidades, relatorio_status
from consultaDAO import  cadastrar_consulta, excluir_consulta, visualizar_todas_consultas, consultar_por_codigo, editar_consulta,relatorio_data_unica, relatorio_faixa_data

conexao = conexao.conectar()
cursor = conexao.cursor()


print("-=-= SENAI SAÚDE =-=-")
op_menu = int(input("1. Área de Pacientes\n2. Área de Médicos\n3. Área de Consultas\n0. Encerrar\n\nEscolha uma opção: "))
limpar_tela()  # Limpa tela

if op_menu == 1:
    print("-=-= ÁREA DE PACIENTES =-=-")
    op_menu_sec = int(input(("1. Cadastrar\n2. Editar\n3. Consultar\n4. Excluir\n5. Relatório\n6. Pacientes por idade\n\nEscolha uma opção: ")))

    match op_menu_sec:  # match= aponta pra uma variável, igual Escolha/Caso
        case 1:
            cadastrar_paciente(conexao, cursor)

        case 2:
            editar_paciente(conexao, cursor)

        case 3:
            op_consulta = int(input("-=-= CONSULTA DE PACIENTES =-=-\n\n1.Consulta única por CPF\n2.Consultar todos os pacientes\n\nEcolha uma opção: "))

            if op_consulta == 1:
                consultar_por_cpf(cursor)

            elif op_consulta == 2:
                consultar_todos_pacientes(cursor)

            else:
                print("Opção Inválida!")
                delay()

        case 4:
            excluir_paciente(conexao, cursor)

        case 5:
            relatorio_paciente(cursor)
        case 6:
            relatorio_paciente_consultas_marcadas(cursor)

elif op_menu == 2:
    print("-=-= ÁREA DE MÉDICOS =-=-")
    op_menu_sec = int(input(("1. Cadastrar\n2. Editar\n3. Consultar\n4. Excluir\n5. Inativar médico\n6. Ativar médico\n7. Relatório\n\nEscolha uma opção: ")))
    limpar_tela()

    match op_menu_sec:
        case 1:
            cadastrar_medico(conexao,cursor)

        case 2:
            editar_medico(conexao,cursor)

        case 3:
            op_consulta = int(input(
                "-=-= CONSULTA DE MÉDICOS =-=-\n\n1.Consulta única por CRM\n2.Consultar todos os médicos\n\nEcolha uma opção: "))

            if op_consulta == 1:
                consultar_por_crm(cursor)

            elif op_consulta == 2:
                consultar_todos_medicos(cursor)

            else:
                print("Opção Inválida!")
                delay()

        case 4:
            excluir_medico(conexao, cursor)

        case 5:
            inativar_medico(conexao, cursor)

        case 6:
            ativar_medico(conexao, cursor)

        case 7:
            op_relatorio = int(input("-=-=RELATÓRIO DE MÉDICOS=-=-\n\n1. Consulta por Especialidade\n2. Consultar por Status\n\nEscolha uma opção"))

            if op_relatorio == 1:
                relatorio_especialidades(cursor)

            elif op_relatorio == 2:
                relatorio_status(cursor)

            else:
                print("Código inválido.")


elif op_menu == 3:
    print("-=-= ÁREA DE CONSULTAS =-=-")
    op_menu_sec = int(input(("1. Cadastrar\n2. Editar\n3. Visualizar\n4. Excluir\n5. Relatório\n\nEscolha uma opção: ")))
    limpar_tela()

    match op_menu_sec:
        case 1:
            cadastrar_consulta(conexao, cursor)

        case 2:
            editar_consulta(conexao, cursor)

        case 3:
            op_consulta = int(input("-=-= VISUALIZAÇÃO DE CONSULTAS=-=-\n\n1.Visualização única por Código\n2.Visualizar todas as Consultas\n\nEscolha uma opção: "))

            if op_consulta ==1:
                consultar_por_codigo(cursor)

            elif op_consulta ==2:
                visualizar_todas_consultas(cursor)

            else:
                print("Opção Inválida!")
                delay()

        case 4:
            excluir_consulta(conexao, cursor)

        case 5:
            op_relatorio = int(input("-=-= RELATÓRIO DE CONSULTAS =-=-\n\n1. Consulta por Data única\n2. Consultar por Faixa de Data\n\nEscolha uma opção"))

            if op_relatorio == 1:
                relatorio_data_unica(cursor)

            elif op_relatorio == 2:
                relatorio_faixa_data(cursor)


            else:
                print("Código inválido.")


'''relatorio geral = trazer quantidade de pessoas com idade menor que X anos, quantidade de pessoas entre 18 e 70, quantidade de pessoas maior de 70'''

