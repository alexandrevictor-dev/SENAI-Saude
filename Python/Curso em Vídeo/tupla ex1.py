numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez")

escolha = int(input("Digite um número de 0 a 10: "))
#Incompleto, esse if deveria estar dentro de uma repetição, mas eu só sei <for> até o momento
if escolha < 0 and escolha > 10:
    print("Número inválido, tente novamente")
print(f"Você digitou o número {numeros[escolha]}")