import classeConexaoBanco as conexao
from flask import Flask, make_response, jsonify, request
#pip install Flask
conexao = conexao.ConexaoBanco(host='localhost', user='root', password='', database='senai_saude')#exatamente o nome do banco
conexao.conectar()

cursor = conexao.conexao.cursor()

api = Flask('Senai Saúde') #instanciandoo Flask

#GET: RECUPERA DADOS
@api.route('/pacientes', methods=['GET']) #decorator indicando uma funçãoespecífica: GET no endpoint '/paciente'
def get_pacientes():
    sql = '''SELECT CPF, RG, NOME, ENDERECO, CEP, DT_NASC, GENERO, TELEFONE, EMAIL, RESPONSAVEL
                FROM PACIENTE'''

    cursor.execute(sql)
    resultado = cursor.fetchall()

    pacientes = []
    for paciente in resultado:
        pacientes.append(
            {
                'cpf': paciente[0],
                'rg': paciente[1],
                'nome': paciente[2],
                'endereco': paciente[3],
                'cep': paciente[4],
                'data_nascimento': paciente[5],
                'genero': paciente[6],
                'telefone': paciente[7],
                'email': paciente[8],
                'responsavel': paciente[9]
            }
        )
    return make_response(jsonify(dados=pacientes)) #retorna pro ponto de origem, nesse caso, dentro do postman
             #pacientes é a lista que percorremos logo acima

#POST: ENVIA DADOS/CRIA/CADASTRA
@api.route('/pacientes', methods=['POST']) #outro decorator, pesquisar dps o que é um decorator
def post_pacientes():
    pacientes = request.json

    for paciente in pacientes: #paciente: individuo / pacientes: a lista de pacientes
        sql = '''SELECT NOME FROM PACIENTE WHERE CPF = %s'''

        try:
            cursor.execute(sql, (paciente['cpf'],))
            resultado = cursor.fetchall()

            if len(resultado) != 0:
                print(f"O CPF {paciente['cpf']} já está cadastrado para o paciente {resultado[0][0]}.")

            else:
                sql = "SELECT NOME FROM PACIENTE WHERE RG = %s"
                cursor.execute(sql, (paciente['rg'],))
                resultado = cursor.fetchall()

                if len(resultado) != 0:
                    print(f"O CPF {paciente['cpf']} já está cadastrado para o paciente {resultado[0][0]}.")

                else:
                    sql = f'''INSERT INTO PACIENTE(CPF, RG, NOME, ENDERECO, CEP, DT_NASC, GENERO, TELEFONE, EMAIL, RESPONSAVEL)
                            VALUES 
                                ('{paciente['cpf']}', '{paciente['rg']}', '{paciente['nome']}', '{paciente['endereco']}', 
                                '{paciente['cep']}', '{paciente['dt_nasc']}', '{paciente['genero']}', '{paciente['telefone']}', 
                                '{paciente['email']}', '{paciente['responsavel']}')'''
                    cursor.execute(sql)
                    conexao.conexao.commit() #acessa conexao pelo arquivo que esta na classeConexaoBanco
                    #primeiro acesso o arquivo e o segundo acessa a conexao atraves do arquivo

        except Exception as e:
            print(f"Erro: {e}")
            input()

    return make_response((jsonify(mensagem= 'Procedimento concluído')))

#DELETE: EXCLUI
@api.route('/pacientes', methods=['DELETE'])
def delete_pacientes():
    pacientes = request.json # requisição enviada e coloca em pacientes já vai em formato de lista
    try:
        for paciente in pacientes:
            sql = '''SELECT ID, NOME 
            FROM PACIENTE
            WHERE CPF = %s'''
            cursor.execute(sql, (paciente['cpf'],))
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                print(f"O CPF {paciente['cpf']} não está cadastrado no banco.")

            else:
                id_paciente = resultado[0][0]
                nome_paciente = resultado[0][1]
                sql = '''DELETE FROM PACIENTE WHERE ID = %s'''
                cursor.execute(sql, (id_paciente,))
                conexao.conexao.commit()

                print(f"O paciente {nome_paciente} foi excluído.")

    except Exception as e:

        print("Erro: ", e)

    return make_response(jsonify(mensagem='Procedimento de exclusão concluído com sucesso!'))


#PUT: UPDATE/ATUALIZA
@api.route('/pacientes', methods=['PUT'])
def put_pacientes():
    pacientes = request.json

    for paciente in pacientes:
        try:
            sql = 'SELECT ID, RG FROM PACIENTE WHERE CPF = %s'
            cursor.execute(sql, (paciente['cpf_atual'],))
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                print(f"O CPF {paciente['cpf']} não está cadastrado no banco.")

            else:
                id_paciente = resultado[0][0]
                cursor.execute(sql, (paciente['novo_cpf'],))
                resultado = cursor.fetchall()

                if len(resultado) != 0 and resultado[0][0] != id_paciente:
                    print(f"O CPF {paciente['novo_cpf']} já está cadastrado para outro paciente.")

                else:
                    sql = "SELECT ID FROM PACIENTE WHERE RG = %s"
                    cursor.execute(sql, (paciente['rg'],))
                    resultado = cursor.fetchall()

                    if len(resultado) != 0 and id_paciente != resultado[0][0]:
                        print(f"O RG {paciente['rg']} já está cadastrado para outro paciente.")

                    else:
                        if paciente['genero'] not in range(1, 7):
                            print(f"Valor informado para a chave 'gênero' é inválido.")

                        else:
                            sql = f'''UPDATE PACIENTE SET CPF = %s, RG = %s, NOME = %s, ENDERECO = %s,
                            CEP = %s, DT_NASC = %s, GENERO = %s, TELEFONE = %s, EMAIL = %s, RESPONSAVEL = %s
    
                            WHERE ID = %s'''

                            cursor.execute(sql, (paciente['novo_cpf'], paciente['rg'], paciente['nome'],
                                                 paciente['endereco'], paciente['cep'], paciente['dt_nasc'],
                                                 paciente['genero'], paciente['telefone'], paciente['email'],
                                                 paciente['responsavel'], id_paciente))

                            conexao.conexao.commit()
                            print(f"Paciente {paciente['nome']} alterado com sucesso!")

        except Exception as e:
            print("Erro: ", e)

    return make_response(jsonify(mensagem="Procedimento realizado"))


#-------------------------------- MÉDICOS --------------------------------



@api.route('/medicos', methods=['GET'])
def get_medicos():
    sql = '''SELECT CRM, NOME, RG, CPF, EMAIL, ENDERECO, CEP, ESP_MEDICA, DT_NASC, DT_ADMISSAO, DT_DESLIGAMENTO, STATUS_MEDICO 
                        FROM MEDICO'''

    cursor.execute(sql)
    resultado = cursor.fetchall()

    if len(resultado) == 0:
        print("Não existem médicos cadastrados no banco.")

        return make_response(jsonify(mensagem="Não há médicos cadastrados no banco."))

    else:
        medicos = []
        for medico in resultado:
            medicos.append(
                {
                    'crm': medico[0],
                    'nome': medico[1],
                    'rg': medico[2],
                    'cpf': medico[3],
                    'email': medico[4],
                    'endereco': medico[5],
                    'cep': medico[6],
                    'esp_medica': medico[7],
                    'dt_nasc': medico[8],
                    'dt_admissao': medico[9],
                    'dt_desligamento': medico[10],
                    'status_medico': medico[11]
                }
            )
        return make_response(jsonify(dados=medicos)) #retorna pro ponto de origem, nesse caso, dentro do postman
                 #pacientes é a lista que percorremos logo acima


@api.route('/medicos', methods=['POST'])
def post_medicos():
    medicos = request.json

    for medico in medicos:
        try:

            sql = "SELECT NOME FROM MEDICO WHERE CPF = %s"
            cursor.execute(sql, (medico['cpf'],))
            resultado = cursor.fetchall()

            if len(resultado) != 0:
                print(f"O CPF {medico['cpf']} já está cadastrado para o médico {resultado[0][0]}.")
            else:

                sql = "SELECT NOME FROM MEDICO WHERE RG = %s"
                cursor.execute(sql, (medico['rg'],))
                resultado = cursor.fetchall()

                if len(resultado) != 0:
                    print(f"O RG {medico['rg']} já está cadastrado para o médico {resultado[0][0]}.")
                else:

                    sql = '''
                        INSERT INTO MEDICO (CPF, RG, NOME, ENDERECO, EMAIL, CEP, CRM, ESP_MEDICA, DT_NASC, DT_ADMISSAO)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    '''
                    cursor.execute(sql, (
                        medico['cpf'], medico['rg'], medico['nome'], medico['endereco'],
                        medico['email'], medico['cep'], medico['crm'], medico['esp_medica'],
                        medico['dt_nasc'], medico['dt_admissao']
                    ))
                    conexao.conexao.commit()
                    print(f"Médico {medico['nome']} foi cadastrado com sucesso.")

        except Exception as e:
            print(f"Erro: {e}")

    return make_response(jsonify(mensagem='Procedimento concluído'))


@api.route('/medicos', methods=['DELETE'])
def delete_medicos():
    medicos = request.json

    try:
        for medico in medicos:
            sql = "SELECT ID, NOME FROM MEDICO WHERE CRM = %s"
            cursor.execute(sql, (medico['crm'],))
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                print(f"O CRM {medico['crm']} não está cadastrado no banco.")

            else:
                id_medico = resultado[0][0]
                nome_medico = resultado[0][1]

                sql = 'SELECT DT_CONSULTA FROM CONSULTA WHERE ID_MEDICO = %s'
                cursor.execute(sql, (id_medico,))
                resultado = cursor.fetchall()

                if len(resultado) != 0:
                    print("Não é possível excluir o médico pois há consultas marcadas.")

                else:
                    sql = 'DELETE FROM MEDICO WHERE ID = %s'
                    cursor.execute(sql, (id_medico,))
                    conexao.conexao.commit()
                    print(f"Médico {nome_medico} foi excluído com sucesso.")

    except Exception as e:
        print(f"Erro: {e}")

    return make_response(jsonify(mensagem='Procedimento de exclusão concluído'))


@api.route('/medicos', methods=['PUT'])
def put_medicos():
    medicos = request.json

    for medico in medicos:
        try:
            sql = 'SELECT ID FROM MEDICO WHERE CRM = %s'
            cursor.execute(sql, (medico['crm_atual'],))
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                print(f"O CRM {medico['crm_atual']} não está cadastrado no banco.")

            else:
                id_medico = resultado[0][0]
                cursor.execute(sql, (medico['novo_crm'],))
                resultado = cursor.fetchall()

                if len(resultado) != 0 and resultado[0][0] != id_medico:
                    print(f"O CRM {medico['novo_crm']} já está cadastrado para outro médico.")

                else:
                    sql = 'SELECT ID FROM MEDICO WHERE RG = %s'
                    cursor.execute(sql, (medico['rg'],))
                    resultado = cursor.fetchall()

                    if len(resultado) != 0 and resultado[0][0] != id_medico:
                        print(f"O RG {medico['rg']} já está cadastrado para outro Médico.")

                    else:
                        sql = 'SELECT ID FROM MEDICO WHERE CPF = %s'
                        cursor.execute(sql, (medico['cpf'],))
                        resultado = cursor.fetchall()

                        if len(resultado) != 0 and resultado[0][0] != id_medico:
                            print(f"O CPF {medico['cpf']} já está cadastrado para outro Médico.")

                        else:
                            if medico['esp_medica'] not in range(1, 7):
                                print("Valor de Especialidade Médica inválido.")

                            else:
                                sql = '''UPDATE MEDICO SET 
                                         CRM = %s, NOME = %s, RG = %s,
                                         CPF = %s, EMAIL = %s, ENDERECO = %s, 
                                         CEP = %s, ESP_MEDICA = %s, DT_NASC = %s, 
                                         DT_ADMISSAO = %s, DT_DESLIGAMENTO = NULL 
                                         WHERE ID = %s'''

                                cursor.execute(sql, (medico['novo_crm'], medico['nome'], medico['rg'],
                                                     medico['cpf'], medico['email'], medico['endereco'],
                                                     medico['cep'], medico['esp_medica'], medico['dt_nasc'],
                                                     medico['dt_admissao'], id_medico))
                                conexao.conexao.commit()
                                print("Médico alterado com Sucesso.")
        except Exception as e:
            print(f"Erro: {e}")

        return make_response(jsonify(mensagem='Procedimento de alteração concluído'))




api.run() #starta o serviço, sempre no final do codigo