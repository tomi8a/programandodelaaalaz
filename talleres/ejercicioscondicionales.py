mensaje_bienvenida = "que mas mor por que tan perdido"
mensaje_a = "digita por fa un numero"
mensaje_b = "digita otro por fa"
mensaje_final = "a es mayor que b"
mensaje_final2 = "b es mayor que a"

######codigo######
print (mensaje_bienvenida)
A = int(input(mensaje_a))
B = int(input(mensaje_b))
ismayorA = A>B
ismayorB = B>A
if (ismayorA):
    print (mensaje_final)
elif (ismayorB):
    print (mensaje_final2)
else:
    print ("son iguales")