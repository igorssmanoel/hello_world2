# i = 2
# while (i <= 100):
#     print(i)
#     i+=2

# for i in range(2,101, 2):
#     print(i)


i = int(input())

while (i != 10):
    print("Voce digitou errado")
    i = int(input())
    if (i == 0):
        break
    print("Depois do break")

print("Fora do while loop")