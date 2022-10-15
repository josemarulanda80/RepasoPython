import pandas as pd

data=pd.read_csv('/pandas/cereals.csv')

#Definir una columna como indice
data.set_index('Name',inplace=True)


#Crea un pequeño informe con datos de interes
data.describe()
#seleciona las filas deseadas del df 
data[1:4]

#
data[["name","ranting"]]

condicion=data["calories"]>70

# Seleccionarfilas según el indice

data.loc[[5,8],'name':'protein']
