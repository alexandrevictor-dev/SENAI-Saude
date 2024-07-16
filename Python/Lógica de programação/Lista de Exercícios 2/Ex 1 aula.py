#Constantes
vrpesonota1 = 2
vrpesonota2 = 3
vrpesonota3 = 5
vrsomapesos = vrpesonota1 + vrpesonota2 + vrpesonota3

#Entrada de dados
nota1 = float(input("Digite a 1º nota: "))
nota2 = float(input("Digite a 2º nota: "))
nota3 = float(input("Digite a 3º nota: "))

#Processamento
media = ((nota1*vrpesonota1) + (nota2*vrpesonota2) + (nota3*vrpesonota3))/vrsomapesos

print(f"A média é: {media:.1f}")

if  media >=8 and media<=10:
    print("A")

elif media >=7 and media<8:
    print("B")

elif media >=6 and media<7:
    print("C")

elif media>=5 and media<6:
    print("D")

else:
    print("D")
