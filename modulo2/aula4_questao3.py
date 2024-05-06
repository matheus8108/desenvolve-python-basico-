produto1=(input("Digite o nome do produto 1:"))
preço_do_produto1=float(input("Digite o preço do produto 1:"))
quantidade_do_produto1=int(input("Digite a quantidade do produto 1:"))

produto2=(input("Digite o nome do produto 2:"))
preço_do_produto2=float(input("Digite o preço do produto 2:"))
quantidade_do_produto2=int(input("Digite a quantidade do produto 2:"))

produto3=(input("Digite o nome do produto 3:"))
preço_do_produto3=float(input("Digite o preço do produto 3:"))
quantidade_do_produto3=int(input("Digite a quantidade do produto 3:"))

preco_total=(preço_do_produto1*quantidade_do_produto1)+(preço_do_produto2*quantidade_do_produto2)+(preço_do_produto3*quantidade_do_produto3)
print("O preço total será",preco_total)

