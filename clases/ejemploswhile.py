mnesaje_bienvenida = "despierte pues dormilon"
mensaje_menu = '''ingrese
    1-para mostrar los numeros del 1-5
    2-Para preguntar tu nombre
    3-para mostrar el año en que estamos
    4-salir
'''
pregunta_nombre = "ingrese nombre"
mensaje_error = 'ingrese opcion valida'
entrada = 1
while(entrada>=1 and entrada<=3):
    entrada = int(input(mensaje_menu))
    if(entrada==1):
        print(1,2,3,4,5)
    elif(entrada==2):
        nombre= input(pregunta_nombre)
        print ('bienvenido',nombre)
    elif(entrada==3):
        print('estamos en el 2021')
    elif(entrada==4):
        print('hasta luego,espero que vuelvas pronto')
    else:
        entrada= 1
        print(mensaje_error)
