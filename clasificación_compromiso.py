# Función para clasificar el nivel de compromiso
def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"

# Datos iniciales: matriz con 6 sesiones de clientes
datos_sesiones = [
    [101, 220, 12],
    [102, 45, 5],
    [103, 150, 6],
    [104, 200, 7],
    [105, 30, 2],
    [106, 190, 10]
]

# Generar y mostrar el informe final
print("===== INFORME DE NIVEL DE COMPROMISO =====")
print("ID Cliente | Nivel de Compromiso")
print("--------------------------------------")
for sesion in datos_sesiones:
    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]
    nivel = clasificar_compromiso(duracion, clics)
    print(f"{id_cliente:>10} | {nivel}")