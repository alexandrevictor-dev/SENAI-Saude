aprovados = 0
exame = 0
reprovados = 0
mediaTot = 0
for c in range(1, 7):
    n1 = float(input("Informe a 1º nota: "))
    n2 = float(input("Informe a 2º nota: "))
    media = (n1+n2)/2
    if media <= 3:
        print(f"Aluno {c}: REPROVADO")
        reprovados = reprovados+1
    
    elif media > 3 and media <7:
        print(f"Aluno {c}: EXAME")
        exame = exame+1

    else:
        print(f"Aluno {c}: APROVADO")
        aprovados = aprovados+1
    
    mediaTot = mediaTot + media
    print(f"{media:.2f}")
    print("---------------------")
    
print("---------------------")
print(f"APROVADOS: {aprovados}")
print(f"EXAME: {exame}")
print(f"REPROVADOS: {reprovados}")
print("")
print(f"MEDIA DE CLASSE: {mediaTot/6:.2f}")
print("---------------------")
