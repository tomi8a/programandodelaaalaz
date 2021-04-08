import operacionesmat as opm
import operacionstrings as ops
mensajeoperacion='{} las dos entradas'
ops.linedesignc(12)
valor1= int(input('ingrese valor 1: '))
valor2= int(input('ingrese valor 2: '))
ops.linedesignc(12)
print(mensajeoperacion.format('sumando'))
opm.calculadora(opm.sumar, valor1, valor2)
ops.linedesignc(12)
print(mensajeoperacion.format('restando'))
opm.calculadora(opm.restar, valor1, valor2)
ops.linedesignc(12)
print(mensajeoperacion.format('multiplicando'))
opm.calculadora(opm.multiplicar, valor1, valor2)
ops.linedesignc(12)
print(mensajeoperacion.format('dividiendo'))
opm.calculadora(opm.dividir, valor1, valor2)
ops.linedesignc(12) 