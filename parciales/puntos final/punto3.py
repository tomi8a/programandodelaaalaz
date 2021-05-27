def validateFloat(pregunta):
    isCorrectData = False
    while (isCorrectData == False):
        try:
            valor = float (input(pregunta))
            isCorrectData = True
        except ValueError:
            print('datos incorrectos ingrese nuevamente')
    return valor 

def validateString(pregunta):
    isCorrectData = False
    while (isCorrectData == False):
        try:
            valor = input(pregunta)
            assert(valor.isalpha())
            isCorrectData = True
        except AssertionError:
            print('datos incorrectos ingrese nuevamente')
    return valor 

def pedirdatos():
    preguntanombre= 'por favor digita tu nombre :'
    preguntadolar='por favor, ingresa la cantidad de dolares que quieres convertir a euros :'
    nombre=validateString(preguntanombre)
    dolares = validateFloat(preguntadolar)
    return nombre,dolares


def calculareuros():
    nombreIn,dolaresIn = pedirdatos()
    euros = dolaresIn*0.82
    print(f'hola {nombreIn} como estas?  elvalor de tus dolares en euros es de :{euros}')
    return euros
calculareuros()
