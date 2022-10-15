lis=[]
def add_number():
    a=int(input("Ingrese el número: "))
    lis.append(a)
    return lis

def par_or_impar(lis):
    par=[i for i in lis if i%2==0]
    impar=[i for i in lis if i%2!=0]
    return par, impar

add_number()
add_number()
add_number()
add_number()

p,i=par_or_impar(lis)
print(p)
print(i)

def factorial():
    number=int(input("Ingrese el numero: "))
    cont=1
    for i in range(1,number+1):
        cont=cont*i
    return cont

print(factorial())