iscorrectinfo = False
while(iscorrectinfo==False):
    try:
        edad = int(input('ingrese edad'))
        iscorrectinfo= True
    except ValueError:
        print('ingresaste dato no valido')
try:
    archivo = open('hola.txt')
except FileNotFoundError:
    print('archivo no existe')

nombre = '232'
print(nombre.isalpha())
assert (nombre.isalpha())