# Operaciones sobre conjuntos
import os; os.system('clear')
municipios = {'Zacatecas', 'Guadalupe','Jerez','Fresnillo',
'Fresnillo'}
print('Conjuntos y operaciones sobre ellos :\n')
print(f'\nLa colección es del tipo : {type(municipios)}')
print(f'Longitud del conjunto : {len(municipios)}')
print(f'El conjunto original : \n{municipios}\n')
print("\nLista de municipios usando un ciclo: ")
for mun in municipios:
 print(mun,end=' ')

print(f'\n\nEsta Zacatecas en el conjunto: {"Zacatecas" in
municipios}')
print('\nAgregra elementos a un conjunto:\n')
municipios.add("Teul")
print(f'Agregar con Add() a Teul : \n{municipios}\n')
otrosmunicipios = {"Luis Moya","Ojocaliente","Tepetongo"}
municipios.update(otrosmunicipios)
print(f'Agregrar con Update() Luis Moya, Ojocaliente,
Tepetongo: \n{municipios}\n')
otrosmunicipios = {"Luis Moya","Ojocaliente","Tepetongo"}
municipios.update(otrosmunicipios)
print(f'Agregrar con Update() Luis Moya, Ojocaliente,
Tepetongo: \n{municipios}\n')
print(f'Eliminar con Remove() a Zacatecas: \n{municipios}\n')
municipios.discard("Ojocaliente")
print(f'Eliminar con Discard() Ojocaliene: \n{municipios}\n')
mun=municipios.pop()
print(f'Eliminar con Pop() (al primero): \n{municipios} \n
{mun}\n')
municipios.clear()
print(f'Eliminar con Clear() : \n{municipios}\n')
 