class Persona ():
    def __init__(self,nombreentrada,identrada,edadentrada):
        self.nombre = nombreentrada
        self.id = identrada
        self.edad = edadentrada
    def hablar (self,mensaje):
        print(f'hola, te tengo que decir algo muy importante',mensaje)
    def caminar (self,pasoentrada):
        for i in range(pasoentrada):
            print(f'hola,he caminado {i+1} pasos')
persona1= Persona('tomas', 1000412167, 18)
persona1.hablar('eres hermoso')
persona1.caminar(10)

####doctor####
class Doctor (Persona):
    def __init__(self, nombreentrada, identrada, edadentrada,especialidadentrada):
        Persona.__init__(self,nombreentrada,identrada,edadentrada)
        self.especialidad = especialidadentrada
    
    def tratamiento (self,enfermedad):
        print(f'hola soy el doctor {self.nombre} y voy a tratar de curarte de la enfermedad {enfermedad}')

doctor1 = Doctor('camilo', 1000412167, 18, 'oftafmologo')
doctor1.tratamiento('apendicitis')

#####nutricionista######
class Nutricionista (Persona):
    def __init__(self, nombreentrada, identrada, edadentrada,universidadentrada):
        Persona.__init__(self,nombreentrada,identrada,edadentrada)
        self.universidad = universidadentrada
    
    def calculoimc (self,entradapeso,entradaaltura):
        self.peso = entradapeso
        self.altura = entradaaltura
        imc = self.peso/self.altura**2
        print(f'hola mi nombre es {self.nombre} soy egresada de {self.universidad} y tu imc es {imc}')

nutricionista1 = Nutricionista('mario', 1000412167, 18, 'ces')
nutricionista1.calculoimc(80, 170)
