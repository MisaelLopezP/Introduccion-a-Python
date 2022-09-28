class Vehiculo:
    color="rojo"
    ruedas=4
    puertas=4
class Coche (Vehiculo):
    velocidad = 200
    cilindrada = 4
    def print(self):
        print("color= " + self.color)
        print("ruedas= " + str(self.ruedas))
        print("puertas= " + str(self.puertas))
        print("velocidad= " + str(self.velocidad))
        print("cilindrada= " + str(self.cilindrada))

carro = Coche()
carro.print()
