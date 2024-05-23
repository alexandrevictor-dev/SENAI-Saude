salario = float(input("Informe o seu salario: "))

if salario <= 500:
    salario = salario*1.05
elif salario > 500 and salario <=1200:
    salario = salario*1.12
else:
    print("Sem bonificação.")

if salario <=600:
    salario = salario+150
else:
    salario = salario+100

print(f"Novo salário: {salario:.2f}")