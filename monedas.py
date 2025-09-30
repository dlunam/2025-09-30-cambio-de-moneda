def cambio_minimo(cantidad):
    denominaciones = [100, 50, 20, 10, 5, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
    resultado = {}

    for d in denominaciones:
        cantidad = round(cantidad, 2)  # Evita errores de punto flotante
        if cantidad >= d:
            num = int(cantidad // d)
            resultado[d] = num
            cantidad -= num * d

    return resultado

# Ejemplo de uso
cantidad = 286.73
cambio = cambio_minimo(cantidad)
print("Cambio mínimo para", cantidad, ":")
for denom, cantidad in cambio.items():
    print(f"{cantidad} x {denom}")
