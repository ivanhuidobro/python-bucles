# 1. Actualizar valores en diccionarios y listas

matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# Cambios solicitados:
matriz[1][0] = 6
cantantes[0]["nombre"] = "Enrique Martin Morales"
ciudades["México"][2] = "Monterrey"
coordenadas[0]["latitud"] = 9.9355431

# 2. Iterar a través de una lista de diccionarios
def iterarDiccionario(lista):
    for diccionario in lista:
        salida = ""
        for clave, valor in diccionario.items():
            salida += f"{clave} - {valor}, "
        print(salida.strip(", "))

# 3. Obtener valores de una lista de diccionarios
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])

# 4. Iterar a través de un diccionario con valores de lista
def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for valor in lista:
            print(valor)

# Pruebas
if __name__ == "__main__":
    cantantes = [
        {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
        {"nombre": "Chayanne", "pais": "Puerto Rico"},
        {"nombre": "José José", "pais": "México"},
        {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
    ]

    costa_rica = {
        "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
        "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
    }

    print("\n--- iterarDiccionario ---")
    iterarDiccionario(cantantes)

    print("\n--- iterarDiccionario2 (nombres) ---")
    iterarDiccionario2("nombre", cantantes)

    print("\n--- iterarDiccionario2 (países) ---")
    iterarDiccionario2("pais", cantantes)

    print("\n--- imprimirInformacion ---")
    imprimirInformacion(costa_rica)
