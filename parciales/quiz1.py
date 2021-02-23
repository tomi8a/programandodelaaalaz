mnesaje_bienvenida = "bienvenido doctor, me alegra mucho volver a verte"
mnesaje_trigliceridos = "si desea consultar los parametros de los trigliceridos,digite numero :"
mensaje_homocisteina = "si desea consultar los parametros de la homocisteina,digite numero :"
mensaje_optimo = "los niveles estan optimos"
mensaje_casioptimo = "estan bien llegando a mal los niveles"
mensaje_alto = "estan bastante altos los niveles,ojo con eso"
mensaje_muy_alto = "estan demasiado altos los niveles"
mensaje_tri = "de trigliceridos"
mensaje_homo = "de homocisteina"
######codificacion######
print(mnesaje_bienvenida)
triglicerridos = int(input(mnesaje_trigliceridos))
homocisteina = int(input(mensaje_homocisteina))
isoptimotri = triglicerridos<150
iscasioptimotri = triglicerridos>=150 and triglicerridos<200
isaltotri = triglicerridos>=200 and triglicerridos<500
ismuyaltotri = triglicerridos>=500
isoptimohomo = homocisteina>=2 and homocisteina<=15
iscasioptimohomo = homocisteina>15 and homocisteina<=30
isaltohomo = homocisteina>30 and homocisteina<=100
ismuyaltohomo = homocisteina>100
#####condicionales######
if(isoptimotri):
    print(mensaje_optimo,mensaje_tri)
elif(iscasioptimotri):
    print(mensaje_casioptimo,mensaje_tri)
elif(isaltotri):
    print(mensaje_alto,mensaje_tri)
else:
    print(mensaje_muy_alto,mensaje_tri)
#####condicionales_homocisteina#######
if(isoptimohomo):
    print(mensaje_optimo,mensaje_homo)
elif(iscasioptimohomo):
    print(mensaje_casioptimo,mensaje_homo)
elif(isaltohomo):
    print(mensaje_alto,mensaje_homo)
elif(ismuyaltohomo):
    print(mensaje_muy_alto,mensaje_homo)
