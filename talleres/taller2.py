mensajesaludo="buenas tardes,un gusto tenerte en frente de mi"
preguntanumero1="puedes hacerme el favor de regalarme un numero que quieras A : "
preguntanumero2="por favor regalame otro numero B : "
mensaje_suma="la suma es igual a"
mensaje_resta="la resta es igual a"
mensaje_x="la multiplicacion es igual a"
mensajedividision="la division es igual a"
mensajeigual= "A es igual a B"
mnesajediferente= "a es diferente de B"
A=int(input(preguntanumero1))
B=int(input(preguntanumero2))
sumar= (A+B)
restar= (A-B)
multiplicar= (A*B)
dividir= (A/B)
isigual = A==B
isdiferente = A!=B
print (mensaje_suma,sumar)
print (mensaje_resta,restar)
print (mensaje_x,multiplicar)
print (mensajedividision,dividir)
print (mensajeigual,isigual)