mnesaje_bienvenida= "bienvenido,juguemos"
pregunta_numero='debes acertar un numero del 1-10,tienes los intentos que quieras,buena suerte,ingresa tu numero :'
pregunta_fallaste = 'ahhh fallaste/:, ingresa otro numero'
mensaje_despedida= 'felicidades,ganaste'
mensaje_perdiste = 'perdiste,vuelve a intentarlo'
#####entradacodigo######
numeroOculto= 7
vidas= 5
print(mnesaje_bienvenida)
numeroingresado = int(input(pregunta_numero))
if(numeroingresado !=numeroOculto):
    vidas -=1
while(numeroingresado!=numeroOculto and vidas>0):
    numeroingresado = int(input(pregunta_fallaste))
    vidas -=1   

if(vidas>0 and numeroOculto==numeroingresado):
    print(mensaje_despedida)
    print(vidas)
else:
    print(mensaje_perdiste,'el numero era',numeroOculto)

