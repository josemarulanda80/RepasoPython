from re import A, S


class Fabrica():
    def __init__(self,_llantas,_color,_precio):
        self._llantas=_llantas
        self._color=_color
        self._precio=_precio

    @property
    def llantas(self):
        return self._llantas
    
    @property
    def color(self):
        return self._color

    @property
    def precio(self):
        return self._precio

    @llantas.setter
    def llantas(self,a):
        self._llantas=a
        return self._llantas

    @color.setter
    def color(self,a):
        self._color=a
        return self._color
    
    @color.setter
    def precio(self,a):
        self._precio=a
        return self._precio

class Moto(Fabrica):
    def __init__(self,_llantas,_color,_precio):
        super().__init__(_llantas,_color,_precio)

class Carro(Fabrica):
    def __init__(self,_llantas,_color,_precio):
        super().__init__(_llantas,_color,_precio)

m=Moto(2,"Negro",1000)
print(m.color)
print(m.llantas)
print(m.precio)
c=Carro(4,"Rojo",10000)
print(c.color)
print(c.llantas)
print(c.precio)



