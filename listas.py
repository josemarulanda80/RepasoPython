a=[20, 50, "Curso", 'Python', 3.14]

l=[print(i) for i in a]

entry_one=input("Ingrese el primer dato: ")
entry_second=input("Ingresar el segundo dato: ")

a[0]=entry_one
a[1]=entry_second

l=[print(i) for i in a]
