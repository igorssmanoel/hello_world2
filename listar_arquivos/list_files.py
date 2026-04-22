import os

todos_arquivos = os.listdir("/workspaces/hello_world2/listar_arquivos/")



#print(todos_arquivos)

for arquivo in todos_arquivos:
    if (arquivo.endswith(".txt")): # arquivo1.txt
        f = open(arquivo, "w")
        if int(arquivo[7:8]) % 2 == 0:
            f.write("Vanessa")
        else:
            f.write("Ricardo")
        f.close()


