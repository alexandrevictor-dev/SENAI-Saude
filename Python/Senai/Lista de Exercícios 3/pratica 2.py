tipoCombustivel = str(input("A - ÁLCOOL\nG - GASOLINA\nInforme o tipo de combustível: "))
litro = float(input("Informe a quantidade desejada em litros: "))

#PREÇOS
gasolinaPreco = 5.79 * litro
alcoolPreco = 4.08 * litro


if tipoCombustivel.upper()=="A":
    if litro <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    precoFinal = alcoolPreco - (alcoolPreco*desconto)
    print(f"Valor a pagar: R${precoFinal:.2f}")  



elif tipoCombustivel.upper()=="G":
    if litro <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    precoFinal = gasolinaPreco- (gasolinaPreco*desconto)
    print(f"Valor a pagar: R${precoFinal:.2f}")  

else:
    print("TIPO DE COMBUSTÍVEL INVÁLIDO!")


