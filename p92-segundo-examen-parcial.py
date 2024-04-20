#Muebleria Muebles Dico
#Sistema de Procesamiento de Empledos
empleados = []
while True:
    nombre = input("introduce el nombre del empleado: ")
    edad = int(input("introduce la edad del empleado: "))
    sexo = input("introduce el sexo del empleado (h/m): ")
    sueldo = float(input("introduce el sueldo del empleado: "))

    
    empleado = {
        "nombre": nombre,
        "edad": edad,
        "sexo": sexo,
        "sueldo": sueldo
    }
    empleados.append(empleado)

    continuar = input("Deseas agregar otro empleado? (s/n): ")
    if continuar.lower() != 's':
        break

print("\nlista de Empleados:")
print(empleados)

print("\nTabla de datos:")
print("Nombre\tEdad\tSexo\tSueldo")
for emp in empleados:
    print(f"{emp['nombre']}\t{emp['edad']}\t{emp['sexo']}\t{emp['sueldo']}")

total_empleados = len(empleados)
total_hombres = sum(1 for x in empleados if x['sexo'] == 'h')
total_mujeres = sum(1 for x in empleados if x['sexo'] == 'm')
suma_edad = sum(x['edad'] for x in empleados)
promedio_edad = suma_edad / total_empleados
suma_sueldo = sum(x['sueldo'] for x in empleados)
promedio_sueldo = suma_sueldo / total_empleados

print("\nresumen:")
print(f"total de empleados: {total_empleados}")
print(f"hombres: {total_hombres}")
print(f"mujeres: {total_mujeres}")
print(f"suma de edades: {suma_edad}")
print(f"promedio de edad: {promedio_edad:.2f}")
print(f"suma de sueldos: {suma_sueldo}")
print(f"pjromedio de sueldo: {promedio_sueldo:.2f}")
