# I=1 J=7
# I=1 J=6
# I=1 J=5
# I=3 J=7
# I=3 J=6
# I=3 J=5
# ...
# I=9 J=7
# I=9 J=6
# I=9 J=5

# I=1
# I=3
# I=5
# I=7
# I=9

# for i in range(1,10,2):
#     print(f"I={i} J=7")
#     print(f"I={i} J=6")
#     print(f"I={i} J=5")
offset = 5
for i in range(1,10,2):
    # print(f"I={i} J=7")
    # print(f"I={i} J=6")
    # print(f"I={i} J=5")
    
    for j in range(2,-1,-1):
        print(f"I={i} J={j+offset}")
    offset+=2