idade=int(input("Digite sua idade:"))
jogou=input("Já jogou pelo menos 3 jogos de tabuleiro?")                        
quantidade=int(input("Quantos jogos já venceu?"))
jogos=jogou=="True"
x=idade<19 and idade>15 and jogos and quantidade>0

print(x)
