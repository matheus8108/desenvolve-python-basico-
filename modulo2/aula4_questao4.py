valor=int(input("Digiter o valor:"))
notas_100=valor//100
valor=valor%100

notas_50=valor//50
valor=valor%50

notas_20=valor//20
valor=valor%20

notas_10=valor//10
valor=valor%10

notas_5=valor//5
valor=valor%5

notas_2=valor//2
valor=valor%2

notas_1=valor//1
valor=valor%1

print("São",notas_100,"Notas de 100")
print("São",notas_50,"Notas de 50")
print("São",notas_20,"Notas de 20")
print("São",notas_10,"Notas de 10")
print("São",notas_5,"Notas de 5")
print("São",notas_2,"Notas de 2")
print("São",notas_1,"Notas de 1")

