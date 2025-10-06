import random

def cambio_minimo(dinero, efectivo_disponible):
    resultado = {}
    restante = dinero

    for tipo, cantidad_disponible in efectivo_disponible.items():
        restante = round(restante, 2)
        max_necesario = int(restante // tipo)
        usar = min(max_necesario, cantidad_disponible)
        if usar > 0:
            resultado[tipo] = usar
            restante -= usar * tipo
            restante = round(restante, 2)

    return resultado, restante

efectivo_tipos = [100, 50, 20, 10, 5, 1, 0.5, 0.25, 0.1, 0.05, 0.01]


import random

def cambio_minimo(dinero, efectivo_disponible):
    resultado = {}
    restante = dinero

    for tipo, cantidad_disponible in efectivo_disponible.items():
        restante = round(restante, 2)
        max_necesario = int(restante // tipo)
        usar = min(max_necesario, cantidad_disponible)
        if usar > 0:
            resultado[tipo] = usar
            restante -= usar * tipo
            restante = round(restante, 2)

    return resultado, restante

efectivo_tipos = [100, 50, 20, 10, 5, 1, 0.5, 0.25, 0.1, 0.05, 0.01]

# Bucle principal: interfaz de usuario para repetir consultas de cambio
while True:
    dinero = float(input("¿Cuánto dinero tienes? "))

    opcion = input("¿Quieres mostrar efectivo normal o disponible? (n/d): ").lower()

    if opcion == 'd':
        efectivo_disponible = {tipo: random.randint(0, 10) for tipo in efectivo_tipos}
    else:
        efectivo_disponible = {tipo: 1000 for tipo in efectivo_tipos}

    print("Efectivo disponible (tipo: cantidad):")
    for tipo, cantidad in efectivo_disponible.items():
        print(f"{cantidad} x {tipo}€")

    cambio, restante = cambio_minimo(dinero, efectivo_disponible)

    print("\nCambio mínimo para", dinero, "€:")
    if cambio:
        for tipo, cantidad_tipo in cambio.items():
            print(f"{cantidad_tipo} x {tipo}€")
    else:
        print("No se pudo dar ningún cambio.")

    if restante > 0:
        print(f"No se pudo dar cambio por {restante}€ debido a la falta de efectivo disponible.")

    repetir = input("\n¿Quieres calcular otro cambio? (s/n): ").lower()
    if repetir != 's':
        print("¡Hasta luego!")
        break
