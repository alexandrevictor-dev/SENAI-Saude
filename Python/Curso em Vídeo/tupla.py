lanche = ("hamburger","suco","pizza","pudim")
#tuplas são IMUTÁVEIS! ou seja, não pode ter seus valores substituídos

#mostra o valor que eu mencionar (lembrando que sempre começa com 0, ou seja: hamburger =0, suco =1)
print(lanche[1])
print("----------")

#escreve do elemento 1 ao 3, lembrando que sempre ignora o último, ou seja: suco, pizza
print(lanche[1:3])
print("----------")

#mostra do elemento escolhido até o final
lanche[2:]

#mostra do início até o elemento escolhido
lanche[:2]

#mostra os elementos começando pelo final
lanche[-2]

#em ordem alfabética
print(sorted(lanche))

#para mostrar os itens listados
for c in lanche:
    print(c)
print("----------")

#outra forma de mostrar
for c in range(0,len(lanche)):
    print(lanche[c])
