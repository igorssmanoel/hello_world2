a = input()
b = input()
c = input()

dicionario = {
    "vertebrado": {
        "ave": {
            "carnivoro" : "aguia",
            "onivoro" : "pomba"
        },
        "mamifero": {
            "onivoro" : "homem",
            "herbivoro" : "vaca"
        }
    },
    "invertebrado" :{
        "inseto": {
            "hematofago" : "pulga",
            "herbivoro" : "lagarta"
        },
        "anelideo": {
            "hematofago" : "sanguessuga",
            "onivoro" : "minhoca"
        }
    }
}

print(dicionario[a][b][c])