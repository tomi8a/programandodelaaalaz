for i in range(10):
    print(i)
#######
for i in range(1,11):
    print(i)
########
print('#'*60)
for i in range(1,11,2):
    print(i)
print('#'*60)
rango = int(input('ingrese el rango maximo'))
opcion =int(input('''
    -1 ver solo impares
    -2 ver solo pares
    -3 ver las dos clasificacions
    -n ver cualquier numero para mostrar nada
'''))

if(opcion==1):
    for i in range(1,rango+1):
        if(i%2!=0):
            print(i)
elif(opcion==2):
    for i in range(1,rango+1):
        if(i%2==0):
            print(i)
elif(opcion==3):
    for i in range(1,rango+1):
        if(i%2!=0):
            print(i,'es numero par' )
        else:
            print(i,'es numero impar')
