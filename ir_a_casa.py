import time
from pprint import pprint

def ir_a_casa():
    """
    Función que calcula si ya nos podemos ir a casa (después de las 19 hs) \n
    Si ya nos podemos ir a casa, devuleve el mensaje correspondiente. \n
    En el caso que falte para ello nos devuelve un mensaje con el tiempo restante.
    """
    hora = time.strftime("%H:%M:%S")
    hs = int(hora[:2])
    if hs >= 19:
        return 'Hora de ir a casa..!!!!'
    else:

        tiempo = 19 - hs
        return f'Todavía faltan {tiempo} horas para ir a casa...'

ir_a_casa()