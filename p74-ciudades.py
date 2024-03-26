def leer_ciudades():
    ciudades = []
    print("Introduce nombres de ciudades. Escribe '$' para terminar:")
    while True:
        ciudad = input("> ")
        if ciudad == "$":
            break
        ciudades.append(ciudad)
    return ciudades

def imprimir_ciudades_y_contar(ciudades):
    print(f"\nHas introducido {len(ciudades)} ciudades.")
    print("Lista de ciudades:")
    for ciudad in ciudades:
        print(ciudad)

def ordenar_y_mostrar_descendente(ciudades):
    ciudades.sort(reverse=True)
    print("\nCiudades ordenadas en orden descendente:")
    for ciudad in ciudades:
        print(ciudad)

def contar_y_mostrar_consonantes(ciudades):
    ciudades_con_consonante = [ciudad for ciudad in ciudades if ciudad[0].lower() not in 'aeiou']
    print(f"\nCantidad de ciudades que inician con una consonante: {len(ciudades_con_consonante)}")
    print("Ciudades que inician con una consonante:")
    for ciudad in ciudades_con_consonante:
        print(ciudad)

def main():
    ciudades = leer_ciudades()
    imprimir_ciudades_y_contar(ciudades)
    ordenar_y_mostrar_descendente(ciudades)
    contar_y_mostrar_consonantes(ciudades)

if __name__ == "__main__":
    main()
