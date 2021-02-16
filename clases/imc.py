preguntaestatura = "cuanto mides? : "
preguntapeso = "cuanto pesas? : "
mensajedeimc = "tu imc es ="
peso = float(input(preguntapeso))
estatura= float(input(preguntaestatura))
imc = peso/estatura**2
print (mensajedeimc,imc)