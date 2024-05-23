salario = float(input("Informe o seu salário: "))
divida  = float(input("Informe o valor da sua dívida: "))

divida_acrescimo = (divida*1.02)*2 #Multiplicado por 2 pois são duas dívidas.
resto = salario - divida_acrescimo

print(f"Valor restante após pagar a dívida: {resto}")