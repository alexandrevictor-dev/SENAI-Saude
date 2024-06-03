#Diferença entre receber listas e ligar listas
a = [1, 3, 5]
b = a
b[2] = 8
print(f"Lista A: {a}")
print(f"Lista B: {b}") #repare que o valor 8 mudou nas duas listas, pois foi feito uma ligação! nesse caso, tudo que mudar em uma lista mudará na outra.
print("-=-=-=-=-=-=-=-=-=-=-=-=-=")
#para se fazer uma cópia de uma lista, usa-se o fatiamento assim:
c = [1, 3, 5]
d = c[:]
d[2] = 8
print(f"Lista C: {c}")
print(f"Lista D: {d}") #agora sim, ele copiou a lista C e modificou o elemento apenas em uma lista



