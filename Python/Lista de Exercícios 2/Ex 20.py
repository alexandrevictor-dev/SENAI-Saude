codProd= int(input("Informe o código do produto (1-10): "))
peso= float(input("Informe o peso em KG: "))
codPais= int(input("Informe o código do país (1-3): "))

imposto = 1
preco = 1

if codPais == 1:
    imposto = imposto*0
elif codPais == 2:
    imposto = imposto*0.15
elif codPais == 3:
    imposto = imposto*0.25
else:
    print("CÓDIGO INVÁLIDO")

if codProd >=1 and codProd <=4:
    preco = 10
elif codProd >=5 and codProd <=7:
    preco = 25
elif codProd >=8 and codProd <=10:
    preco = 35
else:
    print("CÓDIGO INVÁLIDO")

grama = peso*1000
print (f"Peso em gramas: {grama:.2f}")

precoTot = grama*preco
print(f"Valor total: R${precoTot:.2f}")

impostoVal = imposto*precoTot
print(f"Imposto: R${impostoVal:.2f}")

print(f"Preço total: R${precoTot+impostoVal:.2f}")

