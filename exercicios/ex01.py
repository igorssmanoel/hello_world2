# Criar 5 variaveis
# nome
# rua
# numero
# cep
# cidade

# E com valores lidos do input() para cada item, exibir a seguinte mensagem
# ENVIAR PARA: Maria
# ENDEREÇO: Rua das Flores, 15 | CEP: 1200-001
# CIDADE: Lisboa

nome = input("Digite seu nome: ")
rua = input("Digite a rua: ")
numero = input("Digite o numero: ")
cep = input("Digite o cep: ")
cidade = input("Digite a cidade: ")

print(f"ENVIAR PARA: {nome}")
print(f"ENDEREÇO: {rua}, {numero} | CEP: {cep}")
print(f"CIDADE: {cidade}")
