a={"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

city=input("Ingrese el país: ")

if city in a:
    print(a[city])
else:
    print("El país no esta dsiponible")

b={1 : "Casillas", 15 : "Ramos",3 : "Pique", 5 : "Puyol",11 : "Capdevila", 14 : "Xabi Alonso",16 : "Busquets", 8 : "Xavi Hernandez",18 : "Pedrito", 6 : "Iniesta",7 : "Villa"

}

c =input("Ingrese el numero: ")
print(b[int(c)])