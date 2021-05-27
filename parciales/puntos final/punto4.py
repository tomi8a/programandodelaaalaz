def ValidarArchivo (nombrearchivo):
    try:
        archivo =open(nombrearchivo)
        return True
    except FileNotFoundError:
        archivo = open(nombrearchivo,'w',encoding='UTF-8')
        return False

def guardarlinea (nombrearchivo,lineaIn):
    archivo = open(nombrearchivo,'a')
    archivo.writelines(lineaIn)

nombreArchivo = 'ManejoClientes.txt'
isvalidate = ValidarArchivo(nombreArchivo)
if(isvalidate):
    nombre = input('ingresa tu nombre por favor :')
    descEnfermedad = input('ingrese la descripcion de la enfermedad :')
    precioConsulta = float(input('ingrese precio de la consulta :'))
    linea = '\ndescripcion :' + descEnfermedad + 'nombre del paciente :' + nombre + 'precio acordado :' + str(precioConsulta)
    guardarlinea(nombreArchivo,linea)
else:
    print('se creo el archivo')
