#####punto 1 aplicacion de canciones ######

class ElementosDigitales ():
    def __init__(self,Nombreentrada,creadorentrada,fechaentrada):
        self.nombre = Nombreentrada
        self.creador = creadorentrada
        self.fecha = fechaentrada
    def atributos (self):
        print(f'hola,como estas?el nombre de la cancion es {self.nombre} esta cancion fue creada por {self.creador} en la fecha{self.fecha}')

elementos = ElementosDigitales('losing it', 'fisher', 18-10-2015)
elementos.atributos()
print('#'*30)

class Ususario ():
    def __init__(self,nombreentrada,edadentrada,sexoentrada,nacionalidadentrada):
        self.nombre = nombreentrada
        self.edad = edadentrada
        self.sexo = sexoentrada
        self.nacionalidad = nacionalidadentrada
    def atributos (self):
        print(f'hola mi nombre es {self.nombre} tengo {self.edad} años, soy de sexo {self.sexo} y soy del pais de {self.nacionalidad}')
    def cancion (self,cancionentrada):
        self.cancion = cancionentrada
        print(f'hola soy {self.nombre} y estoy esuchando esta cancion {self.cancion}')

usuario1 = Ususario('camilo', 18, 'masculino','peru')
usuario1.atributos()
usuario1.cancion('prende la fiesta')
print('#'*30)

class Pagina ():
    def __init__(self,entradacontenido,entradaformato,entradafecha):
        self.contenido = entradacontenido
        self.formato = entradaformato
        self.fecha = entradafecha
    def atributos (self):
        print(f'el contenido es {self.contenido} con formato {self.formato} y su fecha de publicacion es {self.fecha}')

pagina1 = Pagina('guaracha', 'wav', 'febrero 2019')
pagina1.atributos()
print('#'*30)

class Cancion (ElementosDigitales):
    def __init__(self, Nombreentrada, creadorentrada, fechaentrada,generoentrada,duracionentrada):
        ElementosDigitales.__init__(self, Nombreentrada, creadorentrada, fechaentrada)
        self.genero = generoentrada
        self.duracion = duracionentrada
    def cancion (self,cancionentrada):
        self.cancion = cancionentrada
        print(f'esta cancion nueva {self.cancion} fue creada en abril de este año')
    def numreproducciones (self,numreproduccionesentrada):
        for i in range(numreproduccionesentrada):
            print(f'{self.nombre} sonando {i+1} vez')

cancion1 = Cancion('periodico de ayer', 'hector lavoe', '1980', 'salsa', 560)
cancion1.cancion('me elevas')
cancion1.numreproducciones(3)

print('#'*30)



class Artista (Ususario):
    def __init__(self, nombreentrada, edadentrada, sexoentrada, nacionalidadentrada,generoentrada,cancionpublicadaentrada,numalbumentrada):
        Ususario.__init__(self, nombreentrada, edadentrada, sexoentrada, nacionalidadentrada)
        self.genero = generoentrada
        self.numcanciones = cancionpublicadaentrada
        self.numalbums = numalbumentrada
    def concierto (self,ciudadentrada):
        self.ciudad = ciudadentrada
        print(f'hola como estas?en esta ciudad {self.ciudad} dare un concierto el proximo viernes,te esperooo')

artista1 = Artista('ariana grande', 24, 'femenino', 'usa', 'pop', 200, 15)
artista1.concierto('medallo')

listafavs = ['hola bebe','te estoy llamando','ayayai','sobelo']
class Favoritos (Pagina):
    def __init__(self,entradacontenido, entradaformato, entradafecha,favoritoscomunidadentrada,ultimaactualizacionentrada):
        Pagina.__init__(self, entradacontenido, entradaformato, entradafecha)
        self.favoritos = favoritoscomunidadentrada
        self.actualizacion = ultimaactualizacionentrada
    def agregar (self,nombrecancionentrada,fechaactualizacionentrada):
        self.cancionnueva = nombrecancionentrada
        self.fechanueva = fechaactualizacionentrada
        listafavs.append(self.cancionnueva)
        print(f'la lista de las canciones favoritas de la comunidad quedo asi {listafavs} y esta es la fecha de la ultima actualizacion {self.fechanueva}')
    def eliminar (self,posicioneliminarentrada):
        print(listafavs)
        poseliminada=int(input('elige posicion que quieres eliminar'))
        self.posicioneliminada = posicioneliminarentrada
        listafavs.pop(self.posicioneliminada+1)


favorito1 = Favoritos('techhouse', 'mp3', '8 de junio', listafavs,'2 de febrero')
favorito1.agregar('aflojele', '28 de marzo')
favorito1.eliminar(poseliminada)



