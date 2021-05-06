import matplotlib.pyplot as plt
meses = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septembre','octubre','novimebre','diciembre']
ingresos = [987,567,897,456,999,879,897,956,342,550,342,888]
plt.bar(meses,ingresos,width=0.6,color='r')
plt.title('ingresos anuales de trabajador independiente')
plt.xlabel('meses')
plt.ylabel('ingresos X1000 en pesos')
plt.show()

#punto 2###3
pielabels = ['medellin','bogota','cali','barranquilla']
size = [30,40,20,10]
explodepie = [0,0.1,0,0]
plt.pie(size,labels=pielabels,explode=explodepie)
plt.title('ciudades de colombia')
plt.show()

#### punto 3 #####
import pandas as pd
ecgData = pd.read_csv('ppg.csv',encoding='UTF-8',header=0,delimiter=';').to_dict()
muestras = list(ecgData['muestra'].values())
voltaje = list(ecgData['valor'].values())
plt.plot(muestras,voltaje)
plt.title('fotopletismografia')
plt.xlabel('tiempo en seg')
plt.ylabel('voltaje en mv')
plt.show()


