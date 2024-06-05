salarioIn = 1000
anoIn = 2020
anoFim = 2024
perc = 1.5
salarioAt = salarioIn

print(f"Em 2020 o Salário foi de: R${salarioAt}")

for ano in range(anoIn+1, anoFim+1):
    if ano == 2021:
        aumento = salarioAt * (perc/100)

    else:
        perc = perc*2
        aumento = salarioAt * (perc/100)

    salarioAt += aumento
    print(f"Em {ano} o Salário foi de: R${salarioAt:.2f}")
