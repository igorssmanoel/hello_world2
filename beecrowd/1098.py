# I=0 J=1
# I=0 J=2
# I=0 J=3
# I=0.2 J=1.2
# I=0.2 J=2.2
# I=0.2 J=3.2
# .....
# I=2 J=?
# I=2 J=?
# I=2 J=?

a = 0
while (a <=10):
    res = round(a * 0.2, 1)

    if (res == int(res)):
        i = int(res)
    else:
        i = res

    b = 1
    while b <= 3:
        j = round(i + b, 1)
        print(f"I={i} J={j}")
        b+=1 
    a+=1