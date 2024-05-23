salarioMin = float(input("Informe o salário mínimo: "))
horasTrab = float(input("Inofrme as horas trabalhadas: "))
horasExtra = float(input("Inofrme as horas extras trabalhadas: "))
dependentes = int(input("Informe a quantidade de dependentes: "))

vrhorasTrab = salarioMin/5
salario = horasTrab*vrhorasTrab
vrdependentes = dependentes*32
vrhorasExtra = vrhorasTrab + (vrhorasTrab*0.5)
salarioBruto = salario + vrdependentes + vrhorasExtra

if salarioBruto < 200:
    print("Isento do IRRF.")
elif salarioBruto >= 200 and salarioBruto <= 500:
    imposto = salarioBruto*0.10
    print(f"IRRF: {imposto:.2f}")
else:
    imposto = salarioBruto*0.20
    print(f"IRRF: {imposto:.2f}")

salarioLiq = salarioBruto - imposto

if salarioLiq <= 350:
    salarioLiq = salarioLiq + 100
else:
    salarioLiq = salarioLiq + 50

print(f"Salário a receber: {salarioLiq:.2f}")


                  
                  
                   