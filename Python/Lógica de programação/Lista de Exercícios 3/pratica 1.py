#ENTRADA DE DADOS
nome = str(input("Digite seu nome: "))
cpf = int(input("Digite seu CPF: "))
salario = float(input("Digite seu salário: "))
dependentes = int(input("Informe a quantidade de dependentes de IR: "))
dependentes14 = int(input("Informe a quantidade de filhos menores de 14 anos: "))


#SALÁRIO FAMÍLIA
if salario <=500:
    salarioFamilia = 12*dependentes14
else:
    salarioFamilia = 0


#IMPOSTO DE RENDA
if salario <= 1000:
    imposto = 0
elif salario > 1000 and salario <= 2000:
    aliq = 0.15
    imposto = (aliq*salario) - 150
else:
    aliq = 0.275
    imposto = (aliq*salario) - 400



#INSS
if salario <=500:
    inss = salario*0.0765
elif salario > 500 and salario <= 600:
    inss = salario*0.0865
elif salario > 600 and salario <= 800:
    inss = salario*0.0865
elif salario > 800 and salario <= 1600:
    inss = salario*0.11
else:
    inss = 176


#SALÁRIO LÍQUIDO
salarioLiq = salario - inss - imposto + salarioFamilia

#SAÍDA
print("----------DADOS----------")
print(f"Salário Família: R${salarioFamilia:.2f}")
print(f"Imposto de Renda: R${imposto:.2f}")
print(f"INSS: R${inss:.2f}")
print(f"Salário Líquido: R${salarioLiq:.2f}")
print("-------------------------")