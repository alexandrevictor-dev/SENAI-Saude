salMin = float(input("Informe o salário mínimo: "))
turno = str(input("Turno \n M - Matutino\n N - Noturno\n V - Vespertino\n Digite uma opção:  "))
categoria = str(input("Categoria:\n O - Operário\n G - Gerente\n Digite uma opção: "))
numHorasTrab = float(input("\nDigite o número de horas trabalhadas: "))

if turno.upper() == "M":  #upper() transforma em maiúsculo
    vr_coef = salMin*0.10
elif turno.upper() == "V":
    vr_coef = salMin*0.15
elif turno.upper() == "N":
    vr_coef = salMin*0.12
else:
    print("OPÇÃO INVÁLIDA")

salBruto = numHorasTrab*vr_coef

if categoria.upper() == "O":
    if salBruto >= 300:
        vr_imposto = salBruto*0.05
    else:
        vr_imposto = salBruto*0.03

elif categoria.upper() == "G":
    if salBruto >= 400:
        vr_imposto = salBruto*0.06

else:
    print("CÓDIGO INVÁLIDO")

if turno.upper() == "N" and numHorasTrab > 80:
    vr_gratificacao = 50
else:
    vr_gratificacao = 30

if categoria.upper() == "O" or vr_coef <= 25:
    vr_auxilio = salBruto/3
else:
    vr_auxilio = salBruto/2

salLiq  = salBruto - vr_imposto + vr_gratificacao  + vr_auxilio

print(f"Coeficiente: R${vr_coef:.2f}")
print(f"Salário Bruto: R${salBruto:.2f}")
print(f"Imposto: R${vr_imposto}")
print(f"Gratificação: R${vr_gratificacao:.2f}")
print(f"Auxílio Alimentação: R${vr_auxilio}")
print(f"Salário final: R${salLiq}")
if salLiq < 350:
    print("Mal remunerado")
elif salLiq >= 350 and salLiq <= 600:
    print("Normal")
else:
    print("Bem remunerado")
    

