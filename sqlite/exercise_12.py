import sqlite3 
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    while True:
        print('COLEGIO "EL COLEGIO":')
        print('1. Ingresar Alumno')
        print('2. Buscar Alumno')
        op = input('Ingrese su opcion (0 = salir): ')
        if op == '1':
            ingresar_alumno()
        elif op == '2':
            buscar_alumno()
        elif op == '0':
            print('Hasta luego!')
            print('Gracias!')
            break
        else:
            print('Opcion no valida...')


def ingresar_alumno():
    seguir = True
    alumnos = []
    while seguir:
        nombre = input('Ingrese el nombre del alumno: ')
        apellido = input('Ingrese el apellido del alumno: ')
        if nombre == '' and apellido == '':
            seguir = False
        else:
            alumnos.append((nombre, apellido))

    conn = sqlite3.connect(BASE_DIR + '\\colegio.db')
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO alumnos (nombre, apellido) VALUES (?, ?);', alumnos)
    conn.commit()
    cursor.close()
    conn.close()
    print(f'\n\nSe ingresaron {len(alumnos)} alumnos...\n\n')


def buscar_alumno():
    seguir = True
    alumnos = []
    while seguir:
        nombre = input('Ingrese el nombre del alumno: ')
        apellido = input('Ingrese el apellido del alumno: ')
        if nombre == '' and apellido == '':
            seguir = False
        else:
            conn = sqlite3.connect(BASE_DIR + '\\colegio.db')
            c = conn.cursor()
            c.execute(f'SELECT * FROM alumnos WHERE nombre = "{nombre}" AND apellido = "{apellido}"')
            encontrado = c.fetchone()
            if encontrado is None:
                print('\n')
                print('No se encontró el alumno...')
                print('\n')
            else:
                print('\n')
                print('Alumno buscado:')
                print('---------------')
                print(f'Nº Registro: {encontrado[0]}')
                print(f'     Nombre: {encontrado[1]}')
                print(f'   Apellido: {encontrado[2]}')
                print('\n')

            c.close()
            conn.close()


if __name__ == '__main__':
    main()
