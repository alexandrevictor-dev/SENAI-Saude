print("""[--------MENU--------]
  1 - Imposto
  2 - Novo Salário
  3 - Classificação
[--------------------]""")

opcao = int(input("  Selecione a Opção: "))
salario = float(input("  Informe o seu Salário: "))

if opcao == 1: #Calcular imposto
    if salario < 500:
        print(f"Imposto: {salario*0.05:.2f}")
    elif salario >= 500 and salario <=850:
        print(f"Imposto:  {salario*0.10:.2f}")
    else:
        print(f"Imposto: {salario*0.15:.2f}")

elif opcao == 2: #Calcular novo salário
    if salario > 1500:
        print(f"Novo Salário: {salario + 25:.2f}")
    elif salario >= 750 and salario <=1500:
        print(f"Novo Salário: {salario + 50:.2f}")
    elif salario >= 450 and salario <=750:
        print(f"Novo Salário: {salario + 75:.2f}")
    else:
        print(f"Novo Salário: {salario + 100:.2f}")

elif opcao == 3: #Classificar remuneração
    if salario <=700:
        print("Classificação: Mal remunerado")
    else:
        print("Classificação: Bem remunerado")

else:
    print("OPÇÃO INVÁLIDA")   