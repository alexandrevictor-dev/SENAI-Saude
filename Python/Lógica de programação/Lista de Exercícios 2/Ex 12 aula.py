print("-----LISTA DE CÓDIGOS-----")
print("1 - Escrituário")
print("2 - Secretário")
print("3 - Caixa")
print("4 - Gerente")
print("5 - Diretor")
print("--------------------------")

codigo = int(input("Informe o código do seu cargo: "))

salario = float(input("Informe seu salário: "))

print("")
print("--------------------------")
print("")

aumento = 1

if codigo == 1:
    print(f"Salário atual: {salario}")
    print(f"Cargo: Escrituário")
    aumento = salario*1.5
    print(f"Valor do aumento:{aumento-salario}")
    print(f"Novo salário: {aumento:.2f}")
    

elif codigo == 2:
    print(f"Salário atual: {salario}")
    print(f"Cargo: Secretário")
    aumento = salario*1.35
    print(f"Valor do aumento:{aumento-salario}")
    print(f"Novo salário: {aumento:.2f}")

elif codigo == 3:
    print(f"Salário atual: {salario}")
    print(f"Cargo: Caixa")
    aumento = salario*1.2
    print(f"Valor do aumento:{aumento-salario}")
    print(f"Novo salário: {aumento:.2f}")

elif codigo == 4:
    print(f"Salário atual: {salario}")
    print(f"Cargo: Gerente")
    aumento = salario*1.1
    print(f"Valor do aumento:{aumento-salario}")
    print(f"Novo salário: {aumento:.2f}")

elif codigo == 5:
    print(f"Salário atual: {salario}")
    print(f"Cargo: Diretor")
    aumento = salario*1
    print(f"Valor do aumento:{aumento-salario}")
    print(f"Novo salário: {aumento:.2f}")
    
else:
    print("Código invalido.")

