class Calculadora():
    def __init__(self,_numero1,_numero2):
        self._numero1=_numero1
        self._numero2=_numero2
    
    @property
    def numero1(self):
        return self._numero1
    
    @property
    def numero2(self):
        return self._numero2
    
    @numero1.setter
    def numero1(self,a):
        self._numero1=a
        return self._numero1

    @numero2.setter
    def numero2(self,b):
        self._numero2=b
        return self._numero2

    def sumar(self):
        return self._numero1+self._numero2
    
    def restar(self):
        return self._numero1-self._numero2

    def multiplicar(self):
        return self._numero1*self._numero2
    
    def dividir(self):
        return self._numero1/self._numero2

a = Calculadora(3,3)
print(a.sumar())
print(a.restar())
print(a.multiplicar())
print(a.dividir())

class Areas():
    def __init__(self,_base,_altura):
        self._base=_base
        self._altura=_altura
    
    def area(self):
        return self._base*self._altura

class Cuadrado(Areas):
    def __init__(self,_base,_altura):
        super().__init__(_base,_altura)
    

    def area(self):
        return self._base*self._altura

class Triangulo(Areas):
    def __init__(self,_base,_altura):
        super().__init__(_base,_altura)

    def area(self):
        return (self._base*self._altura)/2
    
class Pentagono(Areas):
    def __init__(self,_base,_altura):
        super().__init__(_base,_altura)

    def area(self):
        return ((self._base*self._altura))*(5/2)



c=Cuadrado(3,3)
print(c.area())
t=Triangulo(3,3)
print(t.area())
p=Pentagono(3,3)
print(p.area())

