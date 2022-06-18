import pickle

class Vehiculo:
    def __init__(self, tipo, marca, modelo, color):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return f'El Vehículo es un {self.tipo} marca {self.marca} modelo {self.modelo} color {self.color}'

v1 = Vehiculo('Automovil', 'Toyota', 'Corolla', 'Azul')
f = open('./exercise_16.dat', 'wb')
pickle.dump(v1, f)
f.close()

f = open('./exercise_16.dat', 'rb')
v2 = pickle.load(f)
f.close()

print(v2)
print(type(v2))
