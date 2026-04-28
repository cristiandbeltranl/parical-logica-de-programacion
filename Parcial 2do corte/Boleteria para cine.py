# Cristian Beltran - Parcial 2do corte - 28/04/26

# Diccionario de peliculas (id: nombre, precio)
peliculas = {
    1: ("Avengers : End Game", 12000),
    2: ("Spider - Man: No Way Home", 11000)
    3: ("Batman", 10000)
    4:("Intensamente 2", 9000)
}

# Lista para almacenar compras

compras = []

# Funcion para mostrar peliculas

def mostrar_peliculas():
    print("CARTELERA")
    for id_pelicula, datos in 
peliculas.items()
    nombre, precio = datos  # tupla
    print (f"{id_pelicula}. {nombre} - ${precio}")

# Funcion para seleccionar pelicula
def seleccionar_pelicula():
    try:
        opcion = int(input("Seleccione el numero de la pelicula: "))
        if opcion not in peliculas:
            raise VauleError("Pelicula no valida")
            return opcion
        except VauleError as e:
            print(f"Error: {e}")
            return None

# Funcion para seleccionar cantidad de boletas
def seleccionar_cantidad():
    try:
        cantidad = int(input("Ingrese la cantidad de boletas: "))
        if cantidad <= 0
         raise VauleError("La Cantidad debe ser mayor a 0")
        return cantidad
    except VauleError as e:
        print(f"Error: {e}")
        return None

# funcion para procesar compra
def procesar_compra(id_pelicula, cantidad):
    nombre, precio = 
peliculas[id_pelicula]
    total = precio * cantidad

# Guardar en lista como diccionario
compra = {
    "pelicula": nombre,
    "cantidad": cantidad,
    "total": total
}

compras.append(compra)

print("Compra Realizada")
print(f"Pelicula: {nombre}")
print(f"Boletas: {Cantidad}")
print(f"Total a pagar: ${total}")

#Funcion principal
def main():
    while True:
        mostrar_peliculas

        id_pelicula=
seleccionar_pelicula()
        if id_pelicula is None:
            continue

        cantidad = seleccionar_cantidad()
        if cantidad is None:
            continue

        procesar_compra(id_pelicula, cantidad)

        continuar = input ("¿Desea hacer otra compra? (s/n: )").lower()
        if continuar != 's':
            break

print("Resumen de compras: ")
for compra in compras:
    print(compra)

if __name == "__main__":
    main()