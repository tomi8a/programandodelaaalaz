preguntaestatura = "cuanto mides? : "
preguntapeso = "cuanto pesas? : "
mensajedeimc = "tu imc es ="
mensaje_bajopeso = "estas pero delgado"
mensaje_normal = "estas en forma"
mensase_sobrepeso = "estas medio gordito"
mensaje_obeso = "esta muy gordo pa"
######codigo#######
peso = float(input(preguntapeso))
estatura= float(input(preguntaestatura))
imc = peso/estatura**2
isbajopeso = imc < 18.5
isnormal = imc >= 18.5 and imc < 25 
issobrepeso = imc >= 25 and imc < 30 
resultado = ""
if (isbajopeso):
    resultado = mensaje_bajopeso
elif (isnormal):
    resultado = mensaje_normal
elif (issobrepeso):
    resultado = mensase_sobrepeso
else:
    resultado = mensaje_obeso
print (resultado)
