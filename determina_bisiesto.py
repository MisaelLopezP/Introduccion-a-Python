print("Introduzca un año (número entero) :")
anio = int(input())
def determinaBisiesto (anio):
    if anio % 4 == 0 :
        print ("El año " + str(anio) + " es bisiesto")
    else:
        print ("El año " + str(anio) + " NO es bisiesto")
determinaBisiesto (anio)