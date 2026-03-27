def price():
    precio_base = 100

    impuesto = precio_base * 0.21
    subtotal = precio_base + impuesto
    propina = subtotal * 0.10

    print(impuesto)
    print(subtotal)
    print(propina)
    print(subtotal + propina)