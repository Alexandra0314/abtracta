from abc import ABC, abstractmethod

class MiCasa():
    def _init_(self, Nombre, Edad, Genero):
        self.Nombre= Nombre
        self.Edad= Edad
        self.Genero= Genero
        
    @abstractmethod
    def datos(self):
        pass
    
        
class Persona(MiCasa):
    def _init_(self, Nombre, Edad, Genero):
        self.Nombre= Nombre
        self.Edad= Edad
        self.Genero= Genero

    def datos(self):
        return 'El nombre de la primer persona es {} su edad es {} años, y es de género {}'.format(self.Nombre, self.Edad, self.Genero)
    
class Mascota(MiCasa):
    def _init_(self, Nombre, Edad):
        self.Nombre= Nombre
        self.Edad= Edad

    def datos(self):
        return 'El nombre de su mascota es {}, tiene {} meses'.format(self.Nombre, self.Edad)

class MiniSuper(MiCasa):
    def _init_(self, PrecioProducto):
        self.PrecioProducto= PrecioProducto

    def datos(self):
        return 'El cereal cuesta ${} en el mini super que esta serca de mi casa'.format(self.PrecioProducto)
    
Nombre = Persona('Alexandra', 21, 'Femenino')
Perro = Mascota('Kiara', 8)
Mini = MiniSuper(10)
print(Nombre.datos())
print(Perro.datos())
print(Mini.datos())