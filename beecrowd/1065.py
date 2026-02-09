i = 0
contadorPar = 0

while (i < 5):
    valor = int(input())
    if (valor % 2 == 0):
        contadorPar +=1
    i+=1
print(f"{contadorPar} valores pares")