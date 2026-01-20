# Criando dicionarios

meu_dicionario = {
    "nome":"Igor",
    "idade": 30,
    "cidade": "Curitiba"
}

# Acessando valores
print(meu_dicionario["nome"])
print(meu_dicionario.get("idade"))
print(meu_dicionario["cidade"])

# Removendo valores
meu_dicionario.pop("cidade")
print(meu_dicionario)

# Atualizando valores
meu_dicionario["idade"] = 50
print(meu_dicionario["idade"])

# Adicionando novos valores
meu_dicionario["pais"] = "Brasil"
print(meu_dicionario)

# Acessando todas chaves
print(meu_dicionario.keys())
# Acessando todos valores
print(meu_dicionario.values())