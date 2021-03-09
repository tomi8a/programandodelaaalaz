nombres = ['santi','samuel','aleja','elsa']
print(nombres[2])
nombres.append('mauricio')
print(nombres)
edades = [18,19,20,17]
#al ultimo
print(edades[-1])
#rangos primmero a un numero
print(edades[0:2])
#contar cuantos elementos hay
largolistaedades = len(edades)
print(largolistaedades)
#como sumamos
sumaredades = sum(edades)
#calcular el promedio
promedioedades= sumaredades/largolistaedades
print(promedioedades)
#eliminarelementolista
edades.pop()
##ciclo for y las listas
largolistaedades=len(edades)
for indice in range(largolistaedades):
    print(edades[indice])

largolistadonombres=len(nombres)
for i in range(largolistadonombres):
    print(nombres[i])

posicionespares = []
largolistaedades=len(edades)
for posicion in range(largolistaedades):
    if(edades[indice]%2 == 0):
        posicionespares.append(posicion)

print(posicionespares)


