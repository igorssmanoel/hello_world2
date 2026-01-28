qtd = int(input())
i = 0
while i < qtd:
    ##
    # Se a letra for maiuscula subtrair o primeiro do segundo
    # Se a letra fo minuscula deve se somar ambos os digitos
    # Se os digitos forem  iguais deve mostrar o produto dos digitos
    linha = input()
    n1 = int(linha[0])
    letra = linha[1]
    n2 = int(linha[2])

    if (n1 == n2):
        print(n1 * n2)
    elif (letra.upper() == letra):
        print(n2 - n1)
    elif (letra.lower() == letra):
        print(n1 + n2)
    i+=1