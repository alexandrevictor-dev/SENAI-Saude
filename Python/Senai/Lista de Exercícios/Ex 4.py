n1 = float(input("Informe a 1º nota: "))
n2 = float(input("Informe a 2º nota: "))

peso1 = 2
peso2 = 3
somapeso = peso1 + peso2

media = ((n1*peso1) + (n2*peso2))/somapeso

print(f'Média ponderada: {media:.2f}')