mensaje_mayor = "a es mayor que b"
mnesaje_menor = "a es menor que b"
mnesaje_igual = "a es igual a b"
preguntaA = "ingrese numero a"
preguntab = "ingrese numero b"
##### codigo ######
numeroA = int(input(preguntaA))
numeroB = int(input(preguntab))
ismayor = numeroA > numeroB
ismenor = numeroA < numeroB
if (ismayor):
    print (mensaje_mayor)
elif (ismenor):
    print (mnesaje_menor)
else:
    print(mnesaje_igual)
