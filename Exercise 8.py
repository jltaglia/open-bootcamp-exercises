inicio = int(input("Ingrese el valor inicial: "))
fin = int(input("Ingrese el valor final: "))

impares = []
for i in range(inicio, fin+1):
    if i % 2 != 0:
        impares.append(i)

print (impares)
