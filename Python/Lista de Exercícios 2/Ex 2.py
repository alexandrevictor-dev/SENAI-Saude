nota1 = float(input("Digite a 1º nota: "))
nota2 = float(input("Digite a 2º nota: "))
nota3 = float(input("Digite a 3º nota: "))

media = ((nota1+nota2+nota3)/3)
print(f"Média: {media:.2f}")

if media <=3:
    print("REPROVADO")
elif media>3  and  media<=7:
    print("EXAME\n Para ser aprovado deve ter média acima de 7")
elif media>7 and media <=10:
    print("APROVADO")
else:
    print("NOTA DIGITADA INCORRETA")