morangoKg = float(input("Informe o peso do morango em KG: "))
mangaKg = float(input("Informe o peso da manga em KG: "))

if morangoKg <= 5:
    morangoPreco = 8.5
else:
    morangoPreco = 8.2

if mangaKg <= 5:
    mangaPreco = 9.97
else:
    mangaPreco = 9.91

#PREÇO FINAL
morangoPrecoFinal = morangoKg*morangoPreco
mangaPrecoFinal = mangaKg*mangaPreco

#DESCONTO 10%
if (morangoKg + mangaKg > 7) or (morangoPrecoFinal + mangaPrecoFinal > 25):
    morangoPrecoFinal = morangoPrecoFinal*0.9
    mangaPrecoFinal = mangaPrecoFinal*0.9


print(f"Valor total do morango: R${morangoPrecoFinal:.2f}")
print(f"Valor total do manga: R${mangaPrecoFinal:.2f}")
