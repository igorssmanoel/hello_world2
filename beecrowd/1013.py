entrada = input().split()

a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

lista = [a,b,c]
lista.sort()

print(lista[-1])