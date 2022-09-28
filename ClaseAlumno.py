class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    def print(self):
        print ("Nombre del alumno : "+ self.nombre)
        print ("Calificacion      : " + str(self.nota))
        if self.nota > 70:
            print ("El alumno         : " + self.nombre + " esta APROBADO")
        else:
            print ("El alumno         : " + self.nombre + " esta REPROBADO")

alumno1 = Alumno("Juan Perez",90)
alumno1.print()