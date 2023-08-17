#Función para saber si un número es potencia de 2 (NO es nada eficiente)
n = int(input())
def MIesPot2(n):
    while n%2==0:
        n = n<<2
    if n == 1: return True
    return False
print(MIesPot2(n))


#3 formas de sacar el mayor de un conjunto de 3 números.
#lo puedo mejorar para que lea T números en la entrada
#Y hacer un ciclo para que se ejecute n cantidad de veces necesarias
#De esa forma ya estaría programando el max completamente
#Version original
a,b,c = map(int, input().split())
def vlabs(x):
    if x>=0: return x
    return -x
M1 = (a+b+vlabs(a-b))//2
mayor = (M1+c+vlabs(M1-c))//2
print(mayor)

#Versión 2
mayor = a
if b>mayor:
    mayor = b
if c>mayor:
    mayor = c
print(mayor)

#Versión 3
mayor = max(a,b,c)
print(mayor)


#Mayor de n números
n = int(input("¿Cuántos números quiere comparar? "))
lista = []
print("A continuación ingrese los números: ")
while n:
    i = input()
    lista.append(i)
    n-=1
mayor = max(lista)
def verificar(mayor):
    if type(mayor) == int:
        return ("El número mayor es {:.0f}".format(mayor))
    return ("El número mayor es {}".format(mayor))
print(verificar(mayor))


#Conversor de decimal a binario
#Quiero hacer un conversor de bases para bases del 2 al 36
def d2b(n):
    l = []
    while n>=2:
        r = n%2
        l.append(str(r))
        n = n//2
    l.append(str(n))
    return "".join(l)


#Conversor de decimal a b base
def DectoB(n,b):
    return DtB(n,b,0,1)
def DtB(n,b,bi,pot):
    if n==0: return bi
    return DtB(n//b, b, bi+(n%b)*pot, pot*10)


#lista de números en b base (puedo hacer un programa que reciba una lista)
#recorra esa lista y va dandome los valores en la otra base.
def lista(n):
    r = []
    for i in range(0,n+1):
        operacion = DectoB(i,b)
        r.append(operacion)
    return r

final = lista(n)
for elemento in final:
    print(elemento)


#Forma eficiente(con máscaras de bits) de saber si un n es potencia de una de 2 (por ejemplo 4)
def esPot4(n):
    if (n<=0): return False
    if (n&(n-1) != 0): return False
    if n&0x55555555 == 0: return False
    return True


#Programa agarrado de internet para números primos:
lista = int(input('¿Hasta qué número quieres la lista?: '))
cont = 0
for i in range(2, lista + 1):
    primos = True
    for j in range(2,i):
        if i == j:
           break
        elif i%j == 0:
           primos = False
        else:
           continue
    if primos == True:
        print(' ',i, end='')
        cont += 1
print('\nHay %u números primos.' % cont )


def esPrimo(n):
  if (n==2): return True
  if (n%2 == 0): return False
  return esPrimoAux(3,n)
def esPrimoAux(i,n):
  if (i*i>n): return True
  if (n%i == 0): return False
  return esPrimoAux(i+2,n)


#Idea para la criba
n = int(input())
contador = 0
num = 2
matriz = []
fila = []

while contador < n:
    if esPrimo(num):
        fila.append(num)
        contador += 1
        if len(fila) == 10: # Cambiar aquí para modificar la cantidad de columnas
            matriz.append(fila)
            fila = []
    num += 1

if fila:
    matriz.append(fila)

for fila in matriz:
    print(fila)


#Calcular pi con series de taylor. (Clase 8 1:39:00)

#Lista de primos
def esPrimo(n):
    if n==1: return False
    if n==2: return True
    if not n%2: return False
    return esPrimoAux(n,3)
def esPrimoAux(n,i):
    if i*i>n: return True
    if not n%i: return False
    return esPrimoAux(n,i+2)


def listaPrimos(n):
    r = [2]
    i = 3
    while len(r)<n:
        if esPrimo(i):
            r.append(i)
        i+=2
    return r


#Hacer un programa que le pida al usuario el área de que figura quiere sacar
#Sacar el área de un triángulo
b,a = map(float, input("Ingrese la base y la altura: ").split())
areaTriangulo = b*a//2
print("Área = {:.1f}".format(areaTriangulo))