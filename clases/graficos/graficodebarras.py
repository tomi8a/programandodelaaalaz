import matplotlib.pyplot as plt
lenguajes = ['python','java','dart','ts','elixir']
encuesta = [50,10,20,10,10]
plt.bar(lenguajes,encuesta,width=0.6,color='r')
plt.title('lenguajes mas usados')
plt.xlabel('lenguajes de programacion')
plt.ylabel('porcentaje de uso de lenguajes')
plt.savefig('grafico lenguajes.png')
plt.show()

######
#width# = #numero# #para volver mas delgado o gordo las barras####
