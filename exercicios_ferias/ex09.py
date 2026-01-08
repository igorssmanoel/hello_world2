entrada = input().split(", ")
valor_conta = float(entrada[0])
gorjeta_porcentagem = float(entrada[1])

gorjeta = valor_conta * gorjeta_porcentagem/100
total =  gorjeta + valor_conta

print(f"Gorjeta: {gorjeta:.2f}, Total: {total:.2f}")

# conta   gorjeta
# 130       10

# 130  -  100 %
#  x       10%

# x*100 = 130*10
# x = 130*10/100 + 130