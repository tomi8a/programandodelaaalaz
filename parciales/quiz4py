######punto 1 ######
import matplotlib.pyplot as plt
Listasnacks = []
listaprecios = []
for i in range(5):
    elemento = input('ingrese 5 snacks :')
    Listasnacks.append(elemento)
for i in range(5):
    elemento= float(input('ingrese los precios respectivos :'))
    listaprecios.append(elemento)
plt.bar(Listasnacks,listaprecios,width=0.6,color='r')
plt.title('snacks favoritos')
plt.xlabel('snacks')
plt.ylabel('precios')
plt.savefig('snacks.png')
plt.show()

#####punto 2 #######
listacuidades = []
listapoblacion = []

for i in range(5):
    elemento = input('ingreses 5 cuidades :')
    listacuidades.append(elemento)
for i in range(5):
    elemento = float(input('ingrese la poblacion respectiva :'))
plt.pie(listacuidades,listapoblacion)
plt.title('poblacion de las cuidades')
plt.savefig('cuidades.png')
plt.show()



######punto 3 ######

ecg = 'un ecg es  la representacion visual de la act.electirca del corazon en funcion del tiempo'
ppg = 'un ppg es una tecnica para descubrir cambios volumetricos de la sangre  en circulacion periferica'
print('el ecg es',ecg)
print('el ppg es',ppg)

import pandas as pd
ecgData = pd.read_csv('ppgquiz.csv',encoding='UTF-8',header=0,delimiter=';').to_dict()
muestras = list(ecgData['muestra'].values())
voltaje = list(ecgData['valor'].values())
plt.plot(muestras,voltaje)
plt.title('fotopletismografia')
plt.xlabel('tiempo en seg')
plt.ylabel('voltaje en mv')
plt.savefig('pgg.png')
plt.show()

ecgData = pd.read_csv('ecgquiz.csv',encoding='UTF-8',header=0,delimiter=';').to_dict()
muestras = list(ecgData['muestra'].values())
voltaje = list(ecgData['valor'].values())
plt.plot(muestras,voltaje)
plt.title('electrocardiograma')
plt.xlabel('tiempo en seg')
plt.ylabel('voltaje en mv')
plt.savefig('ecg.png')
plt.show()










