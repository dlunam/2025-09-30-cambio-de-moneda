def cambio_minimo(dinero):
    efectivo = [100, 50, 20, 10, 5, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
    resultado = {}

    for tipo in efectivo:
        dinero = round(dinero, 2)
        if dinero >= tipo:
            num = int(dinero // tipo)
            resultado[tipo] = num
            dinero -= num * tipo

    return resultado

# Preguntar al usuario cuánto dinero tiene
dinero = float(input("¿Cuánto dinero tienes? "))

cambio = cambio_minimo(dinero)
print("Cambio mínimo para", dinero, ":")
for tipo, cantidad_tipo in cambio.items():
    print(f"{cantidad_tipo} x {tipo}")
