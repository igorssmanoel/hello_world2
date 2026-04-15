entrada = int(input())

a = 0
b = 1
atual = a + b
resultado = f"{a} {b} {atual}"

for i in range(entrada - 3):    
    a = b
    b = atual
    atual = a + b
    resultado = f"{resultado} {atual}"

print(resultado)
