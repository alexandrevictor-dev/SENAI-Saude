# instalar o msql: pip install mysql-connector-python
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
    "1. Cadastrar Paciente\n2.Cadastrar Médico\n3. Cadastrar Consulta\n0. Encerrar\n\nEscolha uma opção: "))
os.system("cls")  # Limpa tela

match op_menu:  # match= aponta pra uma variável, igual Escolha/Caso
    case 1:
        print("-=-= CADASTRO DE PACIENTE =-=-\n")
        cpf = input("CPF: ")
        rg = input("RG: ")
        nome = input("Nome: ")
        endereco = input("Endereço: ")
        cep = input("CEP: ")
        dt_nasc = input("Data de Nascimento: ")
        genero = int(input("Gênero: "))
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        responsavel = input("O paciente necessita de um responsável(S/N)? ")
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

    case _:  # DEFAULT = ELSE
        print("Opção Inválida")
