linha = input().split()
a = int(linha[0])
b = int(linha[1])

if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a

if (maior % menor) == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")