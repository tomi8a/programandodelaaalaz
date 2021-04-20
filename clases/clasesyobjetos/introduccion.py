class humano ():
    def __init__(self,nombreentrada,edadentrada):
        print('hola soy humano nuevo')
        self.raza = 'humano'
        self.nombre = nombreentrada
    
    def hablar(self,mensaje):
        print('hola,tengo un mensaje que decir...',mensaje)

humano1 = humano('daniel',27)
humano2 = humano('mafer',27)

humano1.hablar('espero que esten muy bien')
humano2.hablar('chao')

print(humano1.nombre)