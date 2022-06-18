f = open('./exercise_15.txt', 'w+')
f.write('Listado de Clientes\n')
f.write('-------------------\n')
f.close()

f = open('./exercise_15.txt', 'r')
print(f.read())
f.close()

f = open('./exercise_15.txt', 'a')
for i in range(1, 11):
    f.write('Cliente ' + str(i) + '\n')
f.close()

f = open('./exercise_15.txt', 'r')
print(f.read())
f.close()
