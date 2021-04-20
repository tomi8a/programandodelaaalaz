class Persona ():
    def __init__(self,nombreentrada,identrada,edadentrada):
        self.nombre = nombreentrada
        self.id = identrada
        self.edad = edadentrada
    def hablar (self,mensaje):
        print(f'hola, te tengo que decir algo muy importante',mensaje)
    def caminar (self,paosentrada):
        self.pasos = pasosentrada
        print(f'hola,he caminado {self.pasos} pasos')
