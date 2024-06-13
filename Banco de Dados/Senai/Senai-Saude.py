import mysql.connector  # importando biblioteca
import os  # Biblioteca de limpar dela
try:  # tratar excessões e erros do programa, traz exatamente os erros
    conexao = mysql.connector.connect(
        host='localhost', user='root', password='', database='senai_saude')
    cursor = conexao.cursor()

# if conexao.is_connected():
# print("Conexão Realizada")

# Assim como o If e Else, o Exception é o "Else", se algo der ruim no try, ele pula pro Exception.
except Exception as e:
    print("Erro: ", e)

print("-=-= SENAI SAÚDE =-=-")
op_menu = int(input(
    "1. Cadastrar Paciente\n2. Cadastrar Médico\n3. Cadastrar Consulta\n0. Encerrar\n\nEscolha uma opção: "))
os.system("cls")  # Limpa tela

match op_menu:  # match= aponta pra uma variável, igual Escolha/Caso
    case 1:
        print("-=-= CADASTRO DE PACIENTE =-=-\n")
        cpf = input("CPF: ")

        sql = "SELECT ID FROM PACIENTE WHERE CPF = %s"
        cursor.execute(sql, (cpf,))
        # retorna para resultado; todas as linhas retornadas pela execução da query
        resultado = cursor.fetchall()

        # se o tamanho da lista retornada para o banco for diferente de 0:
        if len(resultado) != 0:
            print("CPF já cadastrado para outro paciente.")

        else:
            rg = input("RG: ")

            sql = "SELECT ID FROM PACIENTE WHERE RG = %s"
            cursor.execute(sql, (rg,))
            resultado = cursor.fetchall()

            if len(resultado) != 0:
                print("RG já cadastrado para outr paciente.")

            else:

                nome = input("Nome: ")
                endereco = input("Endereço: ")
                cep = input("CEP: ")
                dt_nasc = input("Data de Nascimento: ")
                genero = int(input("Gênero: "))
                telefone = input("Telefone: ")
                email = input("E-mail: ")
                responsavel = input(
                    "O paciente necessita de um responsável(S/N)? ")
                if responsavel.upper() == 'S':
                    responsavel = input("Digite o nome do responsável: ")
                else:
                    responsavel = None

                sql = '''INSERT INTO paciente (CPF, RG, NOME, ENDERECO, CEP, DT_NASC, GENERO, TELEFONE, EMAIL, RESPONSAVEL) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
                valores = (cpf, rg, nome, endereco, cep, dt_nasc,
                           genero, telefone, email, responsavel)

                try:
                    cursor.execute(sql, valores)
                    conexao.commit()  # confirma a transação no SGBD
                    print(f"Paciente  {nome} cadastrado com sucesso!")

                except Exception as e:
                    print(f"Erro: {e}")

    case 2:
        print("-=-= CADASTRO DE MÉDICO =-=-\n")
        crm = input("CRM: ")
        nome = input("Nome: ")
        rg = input("RG: ")
        cpf = input("CPF: ")
        email = input("E-mail: ")
        endereco = input("Endereço: ")
        cep = input("CEP: ")
        esp_medica = int(input("Especialidade Médica: "))
        dt_nasc = input("Data de nascimento: ")
        dt_admissao = input("Data de admissão: ")

        dt_desligamento = input("O Médico continua ativo?(S/N): ")
        if dt_desligamento.upper() == "S":
            dt_desligamento = None
        else:
            dt_desligamento = input("Informe a data de desligamento: 2")

        sql = '''INSERT INTO medico (CRM, NOME, RG, CPF, EMAIL, ENDERECO, CEP, ESP_MEDICA, DT_NASC, DT_ADMISSAO)   
                               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        valores = (crm, nome, rg, cpf, email, endereco,
                   cep, esp_medica, dt_nasc, dt_admissao)

        try:
            cursor.execute(sql, valores)
            conexao.commit()  # Confirmar a transação no SGBD
            print(f"Médico {nome} cadastrado com sucesso!")

        except Exception as e:
            print(f"Erro: {e}")

    case _:  # DEFAULT = ELSE
        print("Opção Inválida")
