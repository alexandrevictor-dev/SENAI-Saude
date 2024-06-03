#listas são mutáveis! posso mudar seus valores
#tupla()  x  lista[]
num = [2, 5, 9, 1]


#para adicionar elementos, deve-se usar o comando .append
num.append(7)
print(num)


#para coloca-los em ordem crescente, usa-se o comando .sort
num.sort()
print(num)
#para colocar em ordem decrescente, usa-se o comando .sort(reverse=True)
num.sort(reverse=True)
print(num)


#para saber quantos elementos tem na lista, usa-se o comando len
print(len(num))


#para adicionar um elemento em um local específico, usa se o comando .insert(x, y) x=posição que vc quer inserir, y= elemento que vc quer inserir
num.insert(0, 1)
print(num)


#para remover um elemento, usa-se o comando .pop() (se não tiver uma posição dentro, ira remover da última posição)
num.pop(2)
print(num)


#Para remover um elemento, usa-se o comando.remove(X), no caso de elementos repetidos em posições diferentes, ele irá remover o primeiro que encontrar
num.remove(1)
print(num)
#Se você tentar remover um valor que não está na lista, dará erro, porém, você pode usar o comando IF e IN para verificar se o número está na lista
if 5 in num:
    num.remove(5)
else:
    print("Não há numero 5")
print(num)


#como mostrar lista de uma forma mais bonita
for c in num:
    print(f"{c}")
#Para usar indice, usa-se enumerate
for v, c in enumerate(num):
    print(f"Na posição {v} há o valor {c}")
print("Fim da lista")
#usuário adiciona valores
for cont in range(0,3):
    num.append(int(input("Digite o valor")))

for v, c in enumerate(num):
    print(f"Na posição {v} há o valor {c}")
print("Fim da lista")

