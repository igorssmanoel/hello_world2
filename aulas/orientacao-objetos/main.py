#import minhas_classes
from minhas_classes import Carro

carro1 = Carro("Fiat", "Uno", "branco", 2010)

carro1.buzinar()
carro1.mostra_velocidade()

carro1.acelerar()
carro1.mostra_velocidade()

carro1.acelerar()
carro1.mostra_velocidade()

carro2 = Carro("Volkswagen", "Gol", "Preto", 2005)
carro2.mostra_velocidade()

carro2.acelerar()
carro2.mostra_velocidade()
