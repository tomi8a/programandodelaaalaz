import matplotlib.pyplot as plt
ListaAlimentos = []
listaprecios = []
for i in range(8):
    elemento = input('ingrese sus 8 alimentos favoritos :')
    ListaAlimentos.append(elemento)
for i in range(8):
    elemento= float(input('ingrese los precios respectivos :'))
    listaprecios.append(elemento)
plt.bar(ListaAlimentos,listaprecios,width=0.6,color='r')
plt.title('alimentos  favoritos')
plt.xlabel('alimentos')
plt.ylabel('precios')
plt.savefig('alimentosfav.png')
plt.show()