
# print(list(range(6)))
palavra = "igor"
tamanhoPalavra = len(palavra)

#range(fim)
#range(inicio,fim)
#range(inicio, fim, deslocamento/direcao)
for item in range(tamanhoPalavra-1,-1, -2):
    print(palavra[item])

for i in range(0,10):
    print(i)

lista = [0,1,2,3]
index = 0
while (index < len(lista)):
    print(lista[index])
    index+=1

