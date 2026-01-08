lista_a = [] # lista vazia
lista_a = ["goiaba", "maçã", "uva"]
#             0         1      2 
print(lista_a[2])
print(lista_a)

# Atualizar
lista_a[0] = "banana"
print(lista_a)

# Adicionar item
lista_a.append("laranja")
print(lista_a)

# Remover item
lista_a.remove("uva")
print(lista_a)

lista_a.pop(0)
print(lista_a)