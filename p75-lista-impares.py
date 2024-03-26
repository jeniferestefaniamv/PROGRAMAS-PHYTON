def generar_impares(n):
    return [i for i in range(1, n*2, 2)]

def sumar_y_promedio(lista):
    suma = sum(lista)
    promedio = suma / len(lista)
    print(f"Suma: {suma}, Promedio: {promedio}")

def divisibles_entre_tres(lista):
    divisibles = [num for num in lista if num % 3 == 0]
    suma_divisibles = sum(divisibles)
    print("numeros divisibles entre 3:", divisibles)
    print(f"suma de divisibles entre 3: {suma_divisibles}")

def buscar_elemento(lista):
    elemento = int(input("introduce el número a buscar en la lista: "))
    if elemento in lista:
        posicion = lista.index(elemento)
        print(f"el número {elemento} está en la lista, en la posición {posicion}.")
    else:
        print(f"el número {elemento} no está en la lista.")

def main():
    n = int(input("introduce la cantidad de números impares a generar: "))
    lista_impares = generar_impares(n)
    print("lista de números impares:", lista_impares)
    
    sumar_y_promedio(lista_impares)
    divisibles_entre_tres(lista_impares)
    buscar_elemento(lista_impares)

if __name__ == "__main__":
    main()
