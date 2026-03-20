def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
    tothoras = total_segundos/60//60
    print(tothoras)
    resto = (3665//60)%60
    print(resto)
    restos = resto/60
    print(restos)
