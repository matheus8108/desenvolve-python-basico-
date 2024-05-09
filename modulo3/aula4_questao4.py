distancia = float(input("Insira a distância da entrega em quilômetros: "))
peso = float(input("Insira o peso do pacote em quilogramas: "))

if peso > 10:
    taxa_adicional = 10
else:
    taxa_adicional = 0

if distancia <= 100:
    valor_frete = peso * 1 + taxa_adicional
elif 101 <= distancia <= 300:
    valor_frete = peso * 1.50 + taxa_adicional
else:
    valor_frete = peso * 2 + taxa_adicional

print("O valor do frete é: R$" + str(valor_frete))