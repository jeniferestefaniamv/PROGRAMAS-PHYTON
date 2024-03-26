import random

def lista_aleatoria():
    return [random.randint(1, 100) for _ in range(10)]

def sumar_si_ambos_impares(lista1, lista2):
    return [x + y if x % 2 != 0 and y % 2 != 0 else 0 for x, y in zip(lista1, lista2)]

def imprimir_listas(lista1, lista2, suma):
    print("Lista 1:", lista1)
    print("Lista 2:", lista2)
    print("Suma de elementos impares:", suma)

def main():
    lista1 = lista_aleatoria()
    lista2 = lista_aleatoria()
    suma = sumar_si_ambos_impares(lista1, lista2)
    imprimir_listas(lista1, lista2, suma)

if __name__ == "__main__":
    main()
