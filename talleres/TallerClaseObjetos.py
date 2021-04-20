#####punto 1 #####
class Torta ():
    def __init__(self,saborentrada,formaentrada,alturaentrada):

        self.sabor = saborentrada
        self.forma = formaentrada
        self.altura = alturaentrada
    def atributos (self):
        print(f'hola,mi sabor es {self.sabor} y mi forma es {self.forma} y por ultimo tengo una altura de {self.altura}cm')

torta1 = Torta('vainilla','circular',10)
torta1.atributos()


#####punto 2 #######
class Estudiante ():
    def __init__(self,edadentrda,nombreentrada,identrada,carreraentrada,semestreentrada):
        self.edad = edadentrda
        self.nombre = nombreentrada
        self.id = identrada
        self.carrera = carreraentrada
        self.semestre = semestreentrada
    def queestudiara (self,materiaentrada,tiempoentrada):
        self.materia = materiaentrada
        self.tiempo = tiempoentrada
        print(f'hola mi nombre es {self.nombre} y estudiare {self.materia} por {self.tiempo} meses')

estudiante1 = Estudiante(18, 'david', 1000412167, 'ingenieria mecanica', 5)
estudiante1.queestudiara('quimica',10)

####punto3 ######
class Nutricionista ():
    def __init__(self,edadentrada,nombreentrada,uegresadaentrada):
        self.edad = edadentrada
        self.nombre = nombreentrada
        self.uegresada = uegresadaentrada
    def calcularimc (self,pesoentrada,alturaentrada):
        self.peso = pesoentrada
        self.altura = alturaentrada
        imc = self.peso/self.altura**2
        print(f'hola con tu peso de {self.peso} kg y con estatura de {self.altura} cm tu imc es',imc)

nutricionista1 = Nutricionista(18, 'camilo', 'ces')
nutricionista1.calcularimc(75, 180)