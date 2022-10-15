import numpy as np

one=np.array([[1,2,3],[4,5,6]])
print(one)
###Devuelve el numero de filas y columnas
print(one.shape)

ceros=np.zeros(10).astype(int)
ones=np.ones(10).astype(int)
print(ceros)
print(ones)

##Para cualquier numero
##primero el numero de repeticiones
##el numero a repetir 

numer=np.full(7,1)
print(numer)

###Para la tranpuesta de una matriz

matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)
print(np.transpose(matrix))