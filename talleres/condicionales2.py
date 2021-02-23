mensaje_edad = "digite edad pues papi"
mensaje_menor = "esta muy chiquito pai es menor"
mensaje_joven = "estas grande"
mensaje_adulto = "ya esta muy cucho pai"
mensaje_adulto_mayor = "quedese en la casa mejor por que si le da el virus se lo lleva"
#####codigo@@@@@
edad= int(input(mensaje_edad))
ismenor = edad<18
ismayor = edad>=18 and edad<=25
isadulto = edad>25 and edad<60
if (ismenor):
    print(mensaje_menor)
elif(ismayor):
    print(mensaje_joven)
elif(isadulto):
    print(mensaje_adulto)
else:
    print(mensaje_adulto_mayor)
