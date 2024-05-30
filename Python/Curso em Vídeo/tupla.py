lanche = ("hamburger","suco","pizza","pudim")
#tuplas são IMUTÁVEIS!

#mostra o valor que eu mencionar (lembrando que sempre começa com 0, ou seja: hamburger =0, suco =1)
print(lanche[1])
print("----------")

#escreve do elemento 1 ao 3, lembrando que sempre ignora o último, ou seja: suco, pizza
print(lanche[1:3])
print("----------")

#para mostrar os itens listados
for c in lanche:
    print(c)
print("----------")

#outra forma de mostrar
for c in range(0,len(lanche)):
    print(lanche[c])
