listaDolares = [20000,30000,4000,2500,1000,7600]
menu= '''por favor ingrese la opcion deseada
    1-convertir dolares
    2-mostrar categoria de ingresos
    3-ver maximo,minimo y promedio
    4-salir
: '''
preguntaConversorDolares = '''ingrese la opcion deseada
    C-pasar a pesos colombianos
    D-pasar a dolares
    E-pasar a euros
:'''

####error####
mensaje_error_numero = 'ingrese una opcion valida'
mensaje_error_moneda = 'ingrese una moneda valida'
#####informacion###
mensaje_opcion = 'escogio la opcion{}'
mensaje_salida = 'hasta luego,fue un placer atenderte señor ilustre'
#####iniciocodigo@@@@
opcion= int(input(menu))

listapesos = []
listaeuros = []
listaclasificacion = []
######conversiones#####
for elemento in listaDolares:
    pesos = elemento*3700
    listapesos.append(pesos)
for elemento in listaDolares:
    euros= (elemento*0.84)
    listaeuros.append(euros)
###detectando estados de salud #####
for elemento in  listaDolares:
    if(elemento<1000):
        clasificacion = 'ingresos bajos'
    elif(elemento>=1000 and elemento<7000):
        clasificacion='ingresos medios'
    elif(elemento>=7000 and elemento<20000):
        clasificacion='ingresos altos'
    else:
        clasificacion='ingresos elevados'
    listaclasificacion.append(clasificacion)
#####max y min#####
mayor = max(listaDolares)
minimo = min(listaDolares)
acumulador = 0
for elemento in listaDolares:
    acumulador += elemento

promedio = acumulador/len(listaDolares)
###menu
while(opcion!= 4):
    if(opcion==1):
        print(mensaje_opcion.format(1))
        conversion= input(preguntaConversorDolares)
        if(conversion==E):
            print(listaeuros)
        elif(conversion==C):
            print(listapesos)
        elif(conversion==D):
            print(listaDolares)
        else:
            print(mensaje_error_moneda)
    elif(opcion==2):
        print(mensaje_opcion.format(2))
        print(listaclasificacion)
    elif(opcion==3):
        print(mensaje_opcion.format(3))
        print('el ingreso maximo es',mayor)
        print('el ingreso menor es',minimo)
        print('el promedio es',promedio)
    else:
        print('el promedio es',promedio)
    opcion = int(input(menu))
print(mensaje_salida)
