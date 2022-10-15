def ejercicioRaro():
    number1=int(input("Ingrese el primer numero: "))
    number2=int(input("ingrese el segundo numero: "))

    if number1>number2:
        return 1
    elif number1<number2:
        return -1
    else:
        return 0

def iva(dinero,iva=None):
    if iva==None:
        return dinero + dinero*0.21
    else:
        return dinero + dinero*(iva/100)
print(ejercicioRaro())
print(iva(1000,10))
