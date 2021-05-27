class Persona ():
    def __init__(self,nombreentrada,sexoentrada,edadentrada):
        self.nombre = nombreentrada
        self.id = sexoentrada
        self.edad = edadentrada
    def hablar (self,mensaje):
        print(f'hola, te tengo que decir algo muy importante',{mensaje})
persona1 = Persona('tomas','masculino',18)
persona1.hablar('''profe muchisimas gracias por todo, me siento muy agradecido con usted, he aprendido
demasiado en esta materia,por que al principio mis conocimientos eran muy pocos,solo me quedan buenos 
recuerdos de esta materia, que fue la mejor de este semestre,solo me queda agradecerle a usted por todos
los esfuerzos quw hizo.muchisimas gracias.
''')

class Doctor (Persona):
    def __init__(self, nombreentrada, sexoentrada, edadentrada,):
        Persona.__init__(self,nombreentrada,sexoentrada,edadentrada)
        
    
    def calculoimc (self,entradapeso,entradaaltura):
        self.peso = entradapeso
        self.altura = entradaaltura
        imc = self.peso/self.altura**2
        print(f'hola mi nombre es {self.nombre}  y tu imc es {imc}')

doctor1 = Doctor('camilo','masculino',56)
doctor1.calculoimc(84,1.78)