from functools import reduce 

lista = []
i = True
while i == True:
    numero = input('Igrese los números para la lista ("ENTER" para terminar"): ')
    if numero == '':
        i = False
    else:
        lista.append(int(numero))
if len(lista): 
    impares = list(filter(lambda x: x % 2 != 0, lista))
    print('impares:', impares)

    sumatoria = reduce(lambda x, y: x + y, impares)
    print('sumatoria de impares:', sumatoria)

