class Alumno:
    '''
    clase Alumno 
    Atributos: su apellido, nombre y su nota. 
    Imprime un mensaje con el nombre completo, resultado de la nota y si ha aprobado o no.
    '''
    def __init__(self, apellido, nombre, nota):
        self.nombre = nombre
        self.apellido = apellido
        self.nota = nota

    def __str__(self):
        return f"El alumno {(self.apellido).upper()}, {(self.nombre).capitalize()} tiene una nota de {self.nota}" + " y por lo tanto " + ("ha aprobado." if self.aprobado() else "no ha aprobado.")

    def aprobado(self):
        if self.nota >= 5:
            return True
        else:
            return False
