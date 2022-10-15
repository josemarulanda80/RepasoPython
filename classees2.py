import math

class Alumno():
    def __init__(self,_nombre,_dato):
        self._nombre=_nombre
        self._dato=_dato
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def dato(self):
        return self._dato
    
    @nombre.setter
    def nombre(self,variable):
        self._nombre=variable
        return self._nombre
    
    @dato.setter
    def dato(self,variable):
        self._dato=variable
        return self._dato

    def nota(self):
        if self._dato <3:
            return f"reprobe con {self._dato}"
        else:
            return f"aprobe con {self._dato}"
    
    def __str__(self) -> str:
        return f"Mi nombre es {self._nombre} con nota de {self._dato} y {self.nota()}"

a = Alumno("Jose",5)

print(a.nombre)
a.nombre="Alejandro"
print(a.nombre)
print(a.dato)
a.dato=2
print(a.dato)
print(str(a))

class Pow():
    def __init__(self,base,exponente):
        self.base=base
        self.exponente=exponente

    def ex(self):
        return self.base**self.exponente


p=Pow(2,3)
print(p.ex())