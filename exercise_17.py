paises = []
pais = ''
while pais.lower() != 'fin':
    pais = input('Ingrese el nombre de un país (o "fin" para salir): ')
    if pais.lower() != 'fin':
        paises.append(pais)

unicos_y_ord = sorted(set(paises))

print('Los países ingresados son:')
print(unicos_y_ord)