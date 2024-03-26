def leer_numero_mes():
    while True:
        try:
            numero_mes = int(input("Introduce el numero del mes (ej. 4 para abril): "))
            if 1 <= numero_mes <= 12:
                return numero_mes
            else:
                print("Introduce un numero entre 1 y 12.")
        except ValueError:
            print("Introduce un numero valido.")

def imprimir_info_mes(numero_mes, nombres_meses, dias_meses):
    nombre_mes = nombres_meses[numero_mes - 1]
    dias_del_mes = dias_meses[numero_mes - 1]
    print(f"Mes: {nombre_mes}, Dias: {dias_del_mes}")

def main():
    nombres_meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
                     "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    numero_mes = leer_numero_mes()
    imprimir_info_mes(numero_mes, nombres_meses, dias_meses)

if __name__ == "__main__":
    main()
