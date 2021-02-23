pregunta_actual = "digite año actual "
preguntaotro = "digite otro año"
actual= int(input(pregunta_actual))
otro= int(input(preguntaotro))
ismayor= actual>otro
ismenor= actual<otro
resta= actual- otro
otraresta= otro-actual
if(ismayor):
    print("han pasado",resta)
elif(ismenor):
    print("faltan estos años:",otraresta)