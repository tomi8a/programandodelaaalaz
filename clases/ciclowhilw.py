#######mensajes#######
mnensaje_bienvenido = "bienvenido de nuevo ,cuenteme en que le podemos colaborar"
mensaje_valor_pc = "cuanto vale el pc que deseas ? :"
mensaje_ahorrado = "cuanto dinero tienes ahorrado para mercarte eso :"
mensaje_ahorro = "llevas ahorrado :"
######entradas######
print(mnensaje_bienvenido)
ahorrado = float(input(mensaje_ahorrado))
valor = float(input(mensaje_valor_pc))
while (valor>ahorrado):
    print(mensaje_ahorro,ahorrado,"te falta",valor-ahorrado)
    ahorrado +=1000
print(valor == ahorrado)

