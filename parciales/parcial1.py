#######punto 1 #######
valor1= int(input('ingrese valor 1: '))
valor2= int(input('ingrese valor 2: '))
valor3= int(input('ingrese valor 3: '))

def sumar (valor1=1,valor2=1,valor3=0):
    return valor1+valor2+valor3
def restar(valor1=1,valor2=1,valor3=1):
    return valor1-valor2-valor3
def multiplicar (valor1=1,valor2=1,valor3=1):
    return valor1*valor2*valor3
def dividir (valor1=1,valor2=1,valor3=1):
    return valor1/valor2/valor3
def potencia (valor1,valor2,valor3):
    return valor1**valor2**valor3
def calculadora (accion,valor1,valor2,valor3):
    print(accion(valor1,valor2,valor3))
print('la suma')
calculadora(sumar, valor2, valor1, valor3)
print('la resta')
calculadora(restar, valor1, valor2, valor3)
print('la multiplicacion')
calculadora(multiplicar, valor1, valor2, valor3)
print('la division')
calculadora(dividir, valor1, valor2, valor3)
print('la potencia')
calculadora(potencia, valor1, valor2, valor3)
print('#'*12)
######punto 2########
lista1=[3,5,7,9,11]
lista2=[2,4,6,8,10]
lista3=[1,2,3,4,5]
def mostrar_lista (lista):
    for elemento in lista:
        print(elemento)
print('lista1')
mostrar_lista(lista1)
print('lista2')
mostrar_lista(lista2)
print('lista3')
mostrar_lista(lista3)
print('#'*12)
#######punto 3 #######
def calcular_el_area (base,altura):
    return base*altura/2
area=calcular_el_area(10, 15)
print('el area es',area)
print('#'*12)
#######punto 4 #######
listapunto4 = [1,2,3,4,5,6,7,8,9,10]
def mostrarvalores (lista):
    mayor= max(lista)
    menor = min(lista)
    Prom=sum(lista)/len(lista)
    return mayor,menor,Prom
valores = mostrarvalores(listapunto4)
print(valores)


######punto 5 #######
def sucesiondefibonacci (posicion):
    variable1=0
    variable2=1
    for elemento in range(posicion-1):
        patron =variable1+variable2
        variable1=variable2
        variable2=patron
    return (variable1)
posicionpedida= sucesiondefibonacci(4)
print(posicionpedida)
