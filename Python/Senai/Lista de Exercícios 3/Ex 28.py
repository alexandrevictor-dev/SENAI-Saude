cardapio = {
100: {"especificacao": "Cachorro quente", "preco": 1.20},
101: {"especificacao": "Bauru Simples", "preco": 1.30},
102: {"especificacao": "Bauru com Ovo", "preco": 1.50},
103: {"especificacao": "Hambúrguer", "preco": 1.20},
104: {"especificacao": "Cheeseburguer", "preco": 1.30},
105: {"especificacao": "Refrigerante", "preco": 1.00}
}
print("*** Cardápio ***")
for codigo, item in cardapio.items():
    print(f"Código: {codigo} \t {item['especificacao']} \t R${item['preco']:.2f}")

while True:  # looping infinito de algo até que seja encerrado ou o looping quebrado por alguma ação
    codigo_lanche = int(input("\n Digite o código do lanche (ou 0 para finalizar o seu pedido)"))

    if codigo_lanche == 0:
        break

    if codigo_lanche in cardapio:
        quantidade = int(input(f"Digite a quantidade desejada de {cardapio[codigo_lanche]['especificacao']}: "))
        valor_soma_items = cardapio[codigo_lanche]['preco'] * quantidade
        vt_pedido += valor_soma_items

        print(f"{cardapio[codigo_lanche]['especificacao']}: {quantidade} x R$ {cardapio[codigo_lanche]['preco']:.2f} = "
              f"R$ {valor_soma_items}")

    else:
        print("Código invalido! Tente novamente.")

print(f"Valor total do pedido: R$ {vt_pedido:.2f}")