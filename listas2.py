lista_vazia = [] #Lista vazia
print(lista_vazia)
lista = ["banana", "maçã", "laranja"]
#           0        1        2
print(lista[0]) # Pegar o primeiro item
print(lista[1]) # Pegar o segundo item
print(lista[2]) # Pegar o terceiro item
print(lista[-1]) # Pegar o ultimo item

lista.append("acerola") # Adiciona um novo item na lista
print(lista)

lista[0] = "manga"  #Atualiza um item na lista
print(lista)

lista.remove("laranja") #Remove item da lista pelo valor
print(lista)

lista.pop(1) #Remove o ultimo item da lista
print(lista)
