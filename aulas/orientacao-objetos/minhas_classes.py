class Carro:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.velocidade = 0

    def buzinar(self):
        print("Bazingaaaa!")
    
    def acelerar(self):
        self.velocidade += 10

    def mostra_velocidade(self):
        print(f"A velocidade do {self.marca} {self.modelo} é {self.velocidade}")


