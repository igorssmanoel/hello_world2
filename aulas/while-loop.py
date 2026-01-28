# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

idade = int(input("Digite sua idade: "))
while (idade < 18):
    print("Voce nao pode entrar!")
    idade = int(input("Digite sua idade: "))

print("Voce entrou porque eh maior de idade!")
