# lista con 2 diccionarios
autos = [
{ 'marca':'Ford', 'modelo':'Mustang', 'año': 1964 },
{ 'marca':'VW', 'modelo':'Jetta', 'año': 2015 }
]
# agregar elemento al diccionario
autos.append({ 'marca':'Ford', 'modelo':'Focus', 'año': 2000 })

print('\Todos los autos :', autos, len(autos))

print('\nCada auto dentro de los autos:\n')
for auto in autos:
    print(auto)

print('\nDatos en forma de Tabla:\n')
for k in autos[0].keys(): # titulos de la tabla
    print(f'{k}\t', end='')
print('\r')
for auto in autos: # para cada auto
    for v in auto.values(): # imprime sus valores
        print(f'{v}\t', end='')
    print('\r')
print('\nDatos en forma de Registro\n')
for auto in autos: # para cada auto
    for k,v in auto.items(): # imprime sus llaves/valores
        print(f'{k:<12} : {v}')
print('')
    
   

