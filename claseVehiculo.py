class Vehiculo:
    color="rojo"
    ruedas=4
    puertas=4
class Coche (Vehiculo):
    velocidad = 200
    cilindrada = 4

carro = Coche()
print (dir(carro))
