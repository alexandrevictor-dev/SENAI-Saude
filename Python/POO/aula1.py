class Restaurante:
    nome = ""
    categoria = ""
    regiao = ""
    espaco_kids = ""
    n_funcionarios = int
    ativo = False


pizza = Restaurante()
pizza.nome = "Pizza Place"
pizza.categoria = "FastFood"
pizza.espaco_kids = "Não"
pizza.n_funcionarios = 25
pizza.regiao = "Maricá"
pizza.ativo = False

praca = Restaurante()
praca.nome = "A Galega"
praca.categoria = "Italiana"
praca.regiao = "São Gonçalo"
praca.espaco_kids = "Não"
praca.n_funcionarios = "4"
praca.ativo = True

if pizza.categoria == "FastFood":
    print("A categoria está correta!")

else:
    print("A categoria está incorreta")

if pizza.ativo == True:
    print("O restaurante está ativo")
else:
    print("O restaurante esta desativado")



# print(pizzahut)  # Quando executamos dessa forma, ele mostra o código de onde está alocado na memória.
# Para mostrar o que há de funções e atributos em forma de dicionário, utiliza-se a função "vars"
# print(vars(pizzahut))