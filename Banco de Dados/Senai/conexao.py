import mysql.connector  # importando biblioteca


def conectar():
    try:  # tratar excessões e erros do programa, traz exatamente os erros
        conexao = mysql.connector.connect(host='localhost', user='root', password='',database='senai_saude')  # Conectar no banco
        return conexao

    except Exception as e: # Assim como o If e Else, o Exception é o "Else", se algo der ruim no try, ele pula pro Exception.
        print("Erro: ", e)