def grades():
    nota1 = 8
    nota2 = 7
    nota3 = 9

    promedio = (nota1 + nota2 + nota3) / 3
    maximo = max(nota1, nota2, nota3)
    minimo = min(nota1, nota2, nota3)
    faltante = 10 - promedio

    print(promedio)
    print(maximo)
    print(minimo)
    print(faltante)