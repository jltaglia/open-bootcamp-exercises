def es_bisiesto(n: int) -> bool:
    """
    Determina si un año es bisiesto.
    """
    return n % 4 == 0 and (n % 100 != 0 or n % 400 == 0)
