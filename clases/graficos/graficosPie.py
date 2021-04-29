import matplotlib.pyplot as plt
pielabels = ['python','java','dart','js']
size = [30,20,40,10]
explodepie = [0,0,0.1,0]
plt.pie(size,labels=pielabels,explode=explodepie,shadow=True,startangle=90)
acumulador = 0
for elemento in size:
    acumulador+=elemento
for i in range(len(pielabels)):
    pielabels+='-'+str(size[i]/acumulador*100 +'%')



plt.title('uso de lenguajes de programacion 2021')
plt.savefig('tortaslenguajes.png')
plt.show()

###explode es alejar del origen un dato
###startangle es para dar el angulo de inicio
