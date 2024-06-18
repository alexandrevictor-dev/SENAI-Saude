import conexao
from nav_padrao import limpar_tela, delay
from pacienteDAO import cadastrar_paciente, excluir_paciente, consultar_todos_pacientes
from medicoDAO import cadastrar_medico, excluir_medico
from consultaDAO import  cadastrar_consulta, excluir_consulta

conexao = conexao.conectar()
cursor = conexao.cursor()


print("-=-= SENAI SAÚDE =-=-")
op_menu = int(input("1. Área de Pacientes\n2. Área de Médicos\n3. Área de Consultas\n0. Encerrar\n\nEscolha uma opção: "))
limpar_tela()  # Limpa tela

if op_menu == 1:
    print("-=-= ÁREA DE PACIENTES =-=-")
    op_menu_sec = int(input(("1. Cadastrar\n2. Editar\n3. Consultar\n4. Excluir\n\nEscolha uma opção: ")))

    match op_menu_sec:  # match= aponta pra uma variável, igual Escolha/Caso
        case 1:
            cadastrar_paciente(conexao, cursor)

        case 3:
            op_consulta = int(input("-=-= CONSULTA DE PACIENTES =-=-\n\n1.Consulta única por CPF\n2.Consultar todos os pacientes\n\nEcolha uma opção: "))

            if op_consulta == 1:
                pass

            elif op_consulta == 2:
                consultar_todos_pacientes(conexao, cursor)

            else:
                print("Opção Inválida!")
                delay()

        case 4:
            excluir_paciente(conexao, cursor)


elif op_menu == 2:
    print("-=-= ÁREA DE MÉDICOS =-=-")
    op_menu_sec = int(input(("1. Cadastrar\n2. Editar\n3. Consultar\n4. Excluir\n\nEscolha uma opção: ")))
    limpar_tela()

    match op_menu_sec:
        case 1:
            cadastrar_medico(conexao,cursor)

        case 4:
            excluir_medico(conexao, cursor)


    #case _:  # DEFAULT = ELSE
     #   print("Opção Inválida")

elif op_menu == 3:
    print("-=-= ÁREA DE CONSULTAS =-=-")
    op_menu_sec = int(input(("1. Cadastrar\n2. Editar\n3. Visualizar\n4. Excluir\n\nEscolha uma opção: ")))
    limpar_tela()

    match op_menu_sec:
        case 1:
            cadastrar_consulta(conexao, cursor)

        case 3:
            op_consulta = int(input("-=-= CONSULTA DE PACIENTES=-=-\n\n1.Consulta única por CPF\n2.Consultar Todos os Pacientes\n\nEscolha uma opção: "))

            if op_consulta ==1:
                pass

            elif op_consulta ==2:
                consultar_todos_pacientes(cursor)

            else:
                print("Opção Inválida!")
                delay()

        case 4:
            excluir_consulta(conexao, cursor)