preco = float(input("Informe o preço do produto: "))
media = float(input("Informe a venda mensal média: "))

if media < 500 or preco < 30:
    porcent = 1.1

elif (media >= 500 and media <1200) or (preco >= 30 and preco < 80):
    porcent = 1.15

else:
    porcent = 0.8
print(porcent)
print (f"Novo preço: {preco*porcent:.2f}")
