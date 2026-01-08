entrada = input().split()
p = entrada[0]
r = entrada[1]

if (p == '0'):
    print("C")
elif (p == '1') and (r == '0'):
    print("B")
else:
    print("A")

# p r saida
# 0 0 C
# 0 1 C
# 1 0 B
# 1 1 A
