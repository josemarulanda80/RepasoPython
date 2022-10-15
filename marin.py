class Marino():
    
    def message():
        return "Hola soy un marino"

class Pulpo(Marino):

    def message(self):
        return "Hola soy un pulpo"

class Foca(Marino):

    def __init__(self,mensaje):
        super().__init__()
        self.mensaje=mensaje
    def message(self):
        return f"Hola soy un {self.mensaje}"

       
a = Pulpo()
print(a.message())
b=Foca("foca")
print(b.message())