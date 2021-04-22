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

#####punto 4######
class Canguro ():
    def __init__(self,nombrenetrada,edadentrada,identrada):
        self.nombre = nombrenetrada
        self.edad = edadentrada
        self.id = identrada
    def saltos(self,saltosentrada):
        for i in range(saltosentrada):
            print(f'mi nombre es {self.nombre} y he saltado {i+1} saltos')

canguro1 



##### punto 5######
class Guitarra ():
    def __init__(self,tiempoentradas,tipoentrada,colorentrada):
        self.tiempo = tiempoentradas
        self.tipo = tipoentrada
        self.color = colorentrada
    def cancion (self,cancionentrada):
        self.cancion = cancionentrada
        print(f'esta es la cancion{self.cancion}')

guitarra1 = Guitarra(6, acustica, negra)
guitarra1.cancion(toast)