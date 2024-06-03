num = []
maior = 0
menor = 1000000000000000000000000000000000000000000000000000

for c in range(0, 5):
    num.append(int(input(f"Digite um valor para a posição {c}: ")))
    if num[c] > maior:
        maior = num[c]
        posicaomaior = c
    if num[c] < menor:
        menor = num[c]
        posicaomenor = c

print(f"o Maior número é {maior}, encontrado na posição {posicaomaior}")
print(f"o Menor número é {menor}, encontrado na posição {posicaomenor}")
