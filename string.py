import math

texto="Te quiero solo como amigo"

print(texto[0:2])
"""Manera de leer un arrey alrevez"""
print(texto[-3:])
"""Se saltea dos caractteres"""
lista=[print(texto[i]) for i in range(0,len(texto),2)]
"""imprimir el texto inversamente"""
print(texto[::-1])
"""imprimir el inverso mas no el inverso"""
print(texto+texto[::-1])


