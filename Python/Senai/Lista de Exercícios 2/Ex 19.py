altura = float(input("Informe a altura em M: "))
peso = float(input("Informe o peso em KG: "))

if altura < 1.2:
    if peso <= 60:
        print("A")
    elif peso >60 and peso <=90:
        print("D")
    else:
        print("G")

elif altura >= 1.2 and altura <= 1.7:
    if peso <= 60:
        print("B")
    elif peso >60 and peso <=90:
        print("E")
    else:
        print("H")
else:
    if peso <= 60:
        print("C")
    elif peso >60 and peso <=90:
        print("F")
    else:
        print("I")

    
