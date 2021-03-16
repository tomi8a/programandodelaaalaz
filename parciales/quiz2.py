#####lista#####
lista_Celcius = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33] 
pregunta_menu= ''' por favor ingrese la opcion deseada
    1-convertir de grados celcius a K o F
    2-ver el estado respecto a la temperatura del paciente para cada dato
    3-ver temperatura maxima y minima
    4-salir
: '''
pregunta_conversion= '''por favor ingrese a que sistema de unidades desea convertir
    F-fahrenheit
    K-kelvin
    C-centigrados
: '''

mensaje_error_menu= 'por favor, escoga una opcion valida'
mensaje_error_conversion= 'por favor, escoga un sistema de unidades valido'

opcion_menu = int(input(pregunta_menu))

lista_F = []
lista_K = []
lista_tipo_temperatura = []
#####conversion####
for elemento in lista_Celcius:
    fahrenheit = elemento*1.8+32
    lista_F.append(fahrenheit)
for elemento in lista_Celcius:
    kelvin= elemento+273
    lista_K.append(kelvin)
######detectando estado de la persona por la temperatura
for elemento in lista_Celcius:
    if (elemento<36):
        temperatura= 'sufria de hipotermia'
    elif(elemento>=36 and elemento<37.6):
        temperatura= 'tenia temperatura normal'
    else:
        temperatura= 'tenia fiebre'
    lista_tipo_temperatura.append(temperatura)
######maximo y minimo#####
maximo= max(lista_Celcius)
minimo=min(lista_Celcius)
###### while ######
while(opcion_menu!=4):
    if(opcion_menu==1):
        cambioTemperatura= input(pregunta_conversion)
        if(cambioTemperatura=='F'):
            print(lista_F)
        elif(cambioTemperatura=='K'):
            print(lista_K)
        elif(cambioTemperatura=='C'):
            print('no es necesario la conversion',lista_Celcius)
        else:
            print(mensaje_error_conversion)
    elif(opcion_menu==2):
        print(lista_tipo_temperatura)

    elif(opcion_menu==3):
        print(maximo)
        print(minimo)
    else:
        print(mensaje_error_menu)
    opcion_menu = int(input(pregunta_menu))
print('gracias por utilizar nuestros servicios,vuelva pronto')
