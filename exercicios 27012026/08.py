turno = input("Digite em qual turno voce estuda\nM (matutino)\nV (vespertino)\nN (noturno)\n")

if (turno == "M" or turno == "m"):
    print("Bom Dia!")
elif (turno == "V" or turno == "v"):
    print("Boa Tarde")
elif (turno == "N" or turno == "n"):
    print("Boa Noite!")
else:
    print("Valor inválido")