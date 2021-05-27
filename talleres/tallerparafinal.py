####validar un float


def validateFloat(pregunta):
    isCorrectData = False
    while (isCorrectData == False):
        try:
            valor = float (input(pregunta))
            isCorrectData = True
        except ValueError:
            print('datos incorrectos ingrese nuevamente')
    return valor 
#####validar un string #####
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
###### calcular el imc######
def pedirDatosEPN():
    '''
    Se le pide al usuario el peso la estatura 
    y el nombre
    validando que la data este buena
    '''
    preguntaPeso = 'Ingrese su peso en kg :'
    preguntaEstatura = 'Ingrese su estatura en metros : '
    preguntaNombre = 'Ingrese su Nombre :'
    peso = validateFloat(preguntaPeso)
    estatura = validateFloat(preguntaEstatura)
    nombre = validateString (preguntaNombre)
    return peso,estatura, nombre

def calcularIMC ():
    pesoIn, estaturaIn, nombreIn = pedirDatosEPN()
    imc = pesoIn/ (estaturaIn**2)
    return imc, nombreIn

