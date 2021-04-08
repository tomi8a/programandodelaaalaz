numerolista = [1,2,3,4,5,6]

######punto 1######
def mostrarlalista (lista):
    for elemento in lista:
        print(elemento)
mostrarlalista(numerolista)
print('#'*20)
########punto 2 ########
def mostrarvalores (lista):
    mayor= max(lista)
    menor = min(lista)
    acumulador=0
    for elemento in lista:
        acumulador+=elemento
    total = len(lista)
    promedio=acumulador/total
mostrarvalores(numerolista)

######punto 3#######
def saludo (cantidad=2):
    print('saludo'*cantidad)
saludo(12)

#####punto 4######

def numerosparess (lista):
    pares=[]
    for elemento in lista:
        if elemento %2==0:
            pares.append(elemento)
    return pares
listaedades =[12,13,14,15,17,18,19,10]
edadespares = numerosparess(listaedades)
print((edadespares))

#####punto 5######
def listamayores (lista):
    mayores = []
    for elemento in lista:
        if elemento > 24:
            mayores.append(elemento)
    return mayores
edades = [12,20,24,25,28,30,45]
edadesmayores= listamayores(edades)
print(edadesmayores)

######## punto 6 ######
def calcular_el_imc (peso,altura):
    return peso/altura**2
IMC=calcular_el_imc(80, 1.86)
print(IMC)

######punto 7 #######
def hastaluego ():
    print('muchas gracias por tu comportamiento, te extrañare,cuidate')
