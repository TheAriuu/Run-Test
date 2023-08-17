import sys
sys.setrecursionlimit(10000000)

n = int(input())
'''x = int(input())'''
'''a,b = map(int, input().split())'''

#función sencilla de grado 1
def f(n):
    if n==0: return 0
    return 3*n + f(n-1)

#función normal de collatz
def collatz(n):
    if n%2==0: return n//2
    return 3*n+1

#función recursiva: conjetura de collatz
def collatzR(n):
    #print(n) esto es para ver los pasos que realizaron
    if n==1: return 1
    if n%2==0: return collatzR(n//2)
    if n%2==1: return collatzR(3*n+1)
    
#función sencilla e ineficiente de fibonacci
def fibonacci(n): #función de grado 2
# 0 1 1 2 3 5 8 13 21
    if n<=1: return n
    return fibonacci(n-1) + fibonacci(n-2)
   
#Función que me va diciendo una secuencia random
def secuencia(n):
    if n==0: return 1
    if n==1: return 2
    return secuencia(n-1)*2 + secuencia(n-2)

#Función que me dice el valor absoluto
def vlabs(n):
    if n>=0: return n
    return -n

#Función que determina si un número es potencia de 2
def esPot2(n):
    #print(n)
    if n%2: return n==1 #si es impar, se verifica si n==1, si sí
    #se retorna True y si no se retorna False
    return esPot2(n//2) #si es par lo voy dividiendo entre 2

#Sumatoria de ejemplo
def suma(n):
    if n<1: return 0
    return n/(n+1) + s1(n-1)

#Productoria de ejemplo (diferentes formas de hacerlo)
'''recursión de pila (top-down)'''
def prod(n):
    if n<1: return 1
    return (3*n/(n+1)) * prod(n-1)

'''recursión de pila (bottom-up)'''
def prod2(n,i=1):
    if i>n: return 1
    return (3*i/(i+1)) * prod2(n,i+1)

'''recursión de cola (top-down)'''
def prod3(n, r=1):
    if n<1: return r
    return prod3(n-1, r * (3*n/(n+1)))

'''recursión de cola (bottom-up)'''
def prod4(n, i=1, r=1):
    if i>n: return r
    return prod4(n, i+1, r * (3*i/(i+1)))

#Función para sacar el fatorial de un n
def fact(n):
    #print(n)
    if n<=1: return 1
    return n * fact(n-1)

#Sumatorias y productorias
def s1(n):
    if n<=0: return 0
    return ((n*n)/(n+1)) + s1(n-1)

def s2(n):
    #print(n)
    if n<1: return 0
    return (3*n)/2 + s2(n-1)

def s3(n):
    if n>1000: return 0 #bottom-up
    return n*n + s3(n+1)

def p4(a,b): #factorial desde a hasta b
    if a>b: return 1
    return a * p4(a+1,b)

def p5(n):
    if n<3: return 1
    return (2*n) * p5(n-1)

#Sumatoria doble
def f(ini,fin):
    if fin<ini: return 0
    return (fin*fin) + f(ini,fin-1)

def g(n):
    if n<1: return 0
    return f(n,n*n) + g(n-1)

#2° sumatoria doble
def suma2(ini,fin,n):
    if fin<ini: return 0
    return ini*fin*n + suma2(ini,fin-1,n)

def suma1(n,ini=1): #también se puede hacer llamando a una función auxiliar
    if ini>n: return 0
    return suma2(ini,3*n,n) + suma1(n,ini+1)

#Función para convertir de celcius a farenheit
def farenheit(c):
    return c*1.8+32

#Recursión de pila vs cola
#pila = lifo (last in, first out)
#cola = fifo (first in, first out)
def sumaR(n):
    if n<0: return 0
    return 3*n+1 + sumaR(n-1)

def sumaCola(n, r=0):
    if n<0: return r #acercamiento top-down
    return sumaCola(n-1, r + (3*n+1))

#función de cola con acercamiento bottom-up
def sumaCola2(n):
    return Aux(0,n,0)
def Aux(i,n,r):
    if i>n: return r
    return Aux(i+1, n, r + 3*i+1)

#Otra forma de hacerlo sin usar auxiliar
def p(n, i=0, r=0):
    if i>n: return r
    return p(n, i+1, r + 3*i+1)

#2 formas de impirmir potencias:
#Forma Iterativa
'''for i in range(1,101):
    if esPot2(i): print(i, "SI es pot 2")
    else: print(i, "NO es pot 2")

#Forma Recursiva
#Para hacerlo al revés hay que mandarle donde empieza y donde termina
def imprimePotencias(n):
    if n and esPot2(n): 
        print(n, "SI es pot 2")
    elif n: 
        print(n, "NO es pot 2")
    else: return 
    imprimePotencias(n-1)
imprimePotencias(n)'''

#Es potencia de 2? con máscaras de bits (eficiente)
def esPotencia2(n):
    return n == (n&-n)

#Programa para saber si un número es primo
def esPrimo(n):
    if n==2: return True
    if n%2==0: return False
    return esPrimoAux(n,3)
def esPrimoAux(n,i):
    if i*i>n: return True 
    if n%i==0: return False
    return esPrimoAux(n,i+2)


#Programa para elevar un número, y no usar **
def elevar(a,n):
    if n==0: return 1
    r = elevar(a,n>>1)
    r*=r
    if n%2: r*=a
    return r

#Programa para sacar el logaritmo
def logaritmo(a,x):
    if a==1: return 0
    r = 0
    while x>=a:
        x = x/a
        r += 1
    return r

#Funcion para sacar la raiz cuadrada
def raizCuad(n):
    return RCA(1,n,n)
def cuad(x):
    return x*x
def RCA(i,s,n):
    m = (i+s)/2
    err = 0.00001
    if cuad(m-err)<n and cuad(m+err)>n: return m
    if cuad(m)<n: return RCA(m,s,n)
    return RCA(i,m,n)


#EsPrimo iterativo
def esPrimoI(n):
    if (n==2): return True
    if (n%2==0): return False
    i = 3
    while(i*i<=n):
        if (n%i==0): return False
        i += 2
    return True

#RaizCuad iterativo
def raizcuadI(n):
    sup = n
    inf = 1
    m = (inf+sup)/2
    err = 0.000001
    while(cuad(m-err)>=n or cuad(m+err)<=n): #mientras no esté cerca del n
        if cuad(m)>n: sup=m
        else: inf=m
        m = (inf+sup)/2
    return m


#Ejemplo de suma iterativa vs recursiva
def sumaI(n):
    s=0
    for i in range(3,n+1):
        s += (i+1)//i
    return s

def sumaR(n):
    if n<3: return 0
    return (n+1)//n + sumaR(n-1)

#2° suma iterativa
def sumI(n):
    s1 = 0
    for i in range(1,n+1):
        s2=0
        for j in range(i,i*i+1):
            s2 += j+i
        s1 += s2
    return s1

#3° suma recursiva vs iterativa
def Aux2(ini,fin,i):
    if ini>fin: return 0
    return i*ini + Aux2(ini+1,fin,i)
def Aux1(ini,fin):
    if ini>fin: return 1
    return Aux2(fin,fin*fin,ini) * Aux1(ini,fin-1)
def sumaTripleR(n,ini=1):
    if ini>n: return 0
    return Aux1(ini,n) + sumaTripleR(n,ini+1)


def sumaTripleI(n):
    s1=0
    for i in range(1,n+1):
        p2=1
        for j in range(i,n+1):
            s3=0
            for k in range(j,j*j+1):
                s3+=i*k
            p2*=s3
        s1+=p2
    return s1


print(fact(n))