preco = float(input("Informe o valor do produto: "))
tipoProd = input(
    "A- Alimentação\nL- Limpeza\nV- Vestuário\nInforme o tipo do produto: ")
print("-------------------------------------")
refrig = input("S- Sim\nN- Não\nO produto necessita de regrigeração?")

if refrig.upper() == "N":
    if tipoProd.upper() == "A":
        if preco < 15:
            adicional = 2
        else:
            adicional = 5
    elif tipoProd.upper() == "L":
        if preco < 10:
            adicional = 1.5
        else:
            adicional = 2.5
    elif tipoProd.upper() == "V":
        if preco < 30:
            adicional = 3
        else:
            adicional = 2.5
    else:
        print("CÓDIGO DO PRODUTO INCORRETO")

elif refrig.upper() == "S":
    if tipoProd.upper() == "A":
        adicional = 8
    elif tipoProd.upper() == "L" or tipoProd.upper() == "V":
        adicional = 0
    else:
        print("CÓDIGO DO PRODUTO INCORRETO")

else:
    print("CÓDIGO DE REGRIGERAÇÃO INCORRETO")

print("[----------------------------------]")
print(f"  Valor adicional: R${adicional:.2f}")

if preco < 25:
    imposto = 0.05
else:
    imposto = 0.08

precoCusto =  preco + (preco*imposto)

print(f"  Imposto: R${preco*imposto:.2f}")
print(f"  Preço de custo: R${precoCusto:.2f}")

if (tipoProd.upper() == "A") or (refrig.upper() == "S"):
    desconto = 0
else:
    desconto = 0.03
print(f"  Desconto: R${precoCusto*desconto:.2f}")

novoPreco = precoCusto - (precoCusto*desconto)
print(f"  Novo preço: R${novoPreco:.2f}")

if novoPreco <= 50:
    classificacao = "Barato"
elif novoPreco > 50 and novoPreco < 100:
    classificacao = "Normal"
else:
    classificacao = "Caro"

print(f"  Classificação do Produto: {classificacao}")
print("[----------------------------------]")
