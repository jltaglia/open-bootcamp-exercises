class Vehiculo:
    def __init__(self, color, ruedas , puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Este coche es de color {self.color}, tiene {self.ruedas} ruedas y {self.puertas} puertas."

bmw = Coche('bordeaux', 4, 2, 300, 2200)
print(bmw)
