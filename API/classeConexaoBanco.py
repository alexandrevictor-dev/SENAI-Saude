import mysql.connector

class ConexaoBanco: #classe começa com Letra maiúscula (boa prática)
    def __init__(self, host, user, password, database): #método construtor
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexao = None


    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(host = self.host,
                                                   user= self.user,
                                                   password= self.password,
                                                   database= self.database)
            print("Conexão Realizada com Sucesso!")

        except Exception as e:
            print(f"Erro: {e}")