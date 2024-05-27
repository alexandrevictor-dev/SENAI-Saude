menor = 50
maior = 0
mediaMulher = 0
numMulher = 0
numHomens = 0

for c in range (1,16):
    sexo = str(input("Informe o sexo (M/F): "))
    altura = float(input("Informe a altura em METROS: "))
    if altura > maior:
        maior = altura
        sexoMaisAlto = sexo.upper()
    if altura < menor:
        menor = altura
    
    if sexo.upper() == "F":
        mediaMulher = mediaMulher+altura
        numMulher = numMulher+1
    else:
        numHomens = numHomens+1

print("-----------------------")
print(f"Maior altura: {maior}")
print(f"Menor altura: {menor}")
print(f"Média de altura das mulheres: {mediaMulher/numMulher:.2f}")
print(f"Número de homens: {numHomens}")
print(f"Sexo da pessoa mais alta: {sexoMaisAlto}")
print("-----------------------")