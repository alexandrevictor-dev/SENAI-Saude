n1 = int(input("Informe o 1º número: "))
n2 = int(input("Informe o 2º número: "))
n3 = int(input("Informe o 3º número: "))

maior = 1
if maior < n1:
    maior = n1
if maior <n2:
    maior = n2
if maior <n3:
    maior = n3

menor = 100000000000000000000000000000
if menor > n1:
    menor = n1
if menor > n2:
    menor = n2
if menor >n3:
    menor = n3

medio = 1
if n1> menor and n1<maior:
    medio = n1
if n2>menor and n2<maior:
    medio = n2
if n3>menor and n3<maior:
    medio = n3
print("---------------")
print(menor,medio,maior)