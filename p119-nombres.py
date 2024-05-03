"""
Une dos listas de nombres
Invierte la lista completa
Convierte los nombres a mayúsculas
"""
def procesa(n1, n2):
     res = []
     res.extend(n1)
     res.extend(n2)
     res.sort(reverse=True)
     for i in range(len(res)):
         res[i] = res[i].upper()
     return res

def entrada():
     datos = []
     while True:
         n = input('Nombre :')
         if n=='**': break
         datos.append(n)
     return datos

# Principal
nombres1 = ['Juan', 'Pedro', 'Luis', 'Jose', 'Maria']
#nombres2 = ['Lucia', 'Angelica', 'Miguel']
nombres2 = entrada()
todos = procesa(nombres1, nombres2)
print(todos)