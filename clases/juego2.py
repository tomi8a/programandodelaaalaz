import random
mnesaje_bienvenida= "bienvenido,juguemos"
pregunta_numero='debes acertar un numero del 1-10,tienes los intentos que quieras,buena suerte,ingresa tu numero :'
pregunta_fallaste = 'ahhh fallaste/:, ingresa otro numero'
mensaje_despedida= 'felicidades,ganaste'
mensaje_perdiste = 'perdiste,vuelve a intentarlo'
pregunta_dificultad = '''elige
    1-facil
    2-moderado
    3-dificil
    '''
#####entradacodigo######
numeroOculto = random.randint(1,10)
vidas=None

dificultad= int(input(pregunta_dificultad))
while(dificultad!=1 and dificultad!=2 and dificultad!=3):
    print('ingresa una opcion valida')
if(dificultad==1):
    vidas=5
elif(dificultad==2):
    vidas=3
else:
    vidas = 1
numero_ingresado = int(input(pregunta_numero))
while(numero_ingresado!= numeroOculto and vidas>=1):
    vidas-=1
    numero_ingresado = int(input(pregunta_fallaste))
    print('te quedadn estas vidas',vidas)


if(vidas>=0 and numero_ingresado== numeroOculto):
    print(mensaje_despedida)
else:
    print(mensaje_perdiste,'el numero era el',numeroOculto)


