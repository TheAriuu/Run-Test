import sys
sys.setrecursionlimit(1000000)

n=int(input())
a=int(input())

#Programa para saber si un número es potencia de 2
def esPot2(n):
    if (n%2): return n==1
    return esPot2(n//2)
# esta función sirve para saber si un número es potencia de n (por ejemplo 3)
def esPot3(n):
    if (n%3): return n==1
    return esPot3(n//3)

#La manera más eficiente de ver si un número es potencia de 2
def Potencia2(n):
    return n == (n&-n)

#Forma eficiente(con máscaras de bits) de saber si un n es potencia de una de 2 (por ejemplo 4)
def esPot4(n):
    if (n<=0): return False
    if (n&(n-1) != 0): return False
    if n&0x55555555 == 0: return False
    return True

#Programa para saber el n-simo Fibonacci
def nsimoFibo(n):
    if (n<=1): return n
    return nsimoFibo(n-1) + nsimoFibo(n-2)

#Programa para saber si un número es par o impar
def esPar(n):
    if (n%2==0): return True
    return False

#Programa para obtener los digitos de un número (NO SIRVE PARA NADA)
def obtenerdigitos(n):
    if (n==0): return 0
    return n%10 + obtenerdigitos(n//10)*10

#Programa para obtener la suma de los digitos de un número
def sumaDigitos(n):
    if (n<10): return n
    return n%10 + sumaDigitos(n//10)

#Programa para saber la contidad de digitos pares que posee un número
def cantidadPares(n):
    if (n==0): return 1
    return cantidadParesAux(n,0)
def cantidadParesAux(n,cont):
    if (n==0): return cont
    if ((n%10)%2 == 0): 
        cont+=1
    return cantidadParesAux(n//10,cont)

#Programa para saber el valor absoluto
def valorAbs(x):
    if (x>=0): return x
    return -x


# Programa que calcula n factorial (versión recursiva pila e iterativa)
def fact(n):
    if (n==0): return 1
    return n * fact(n-1)

def factI(n):
    p = 1
    for i in range (1,n+1):
        p *= i
    return p

# Suma doble de prueba, recursiva pila e iterativa:
def s1(ini,fin):
    if (fin<ini): return 0
    return fin*fin + s1(ini,fin-1)
def s2(n):
    if (n<1): return 0
    return s1(n,n*n) + s2(n-1)
    
def sumaDoble(n):
    s1=0
    for i in range(1,n+1):
        s2=0
        for j in range(i,(i*i)+1):
            s2+= j*j
        s1+= s2
    return s1

# Programa para saber si un número es primo
def esPrimo(n):
    if (n==2): return True
    if (n%2==0): return False
    return esPrimoAux(3,n)
def esPrimoAux(i,n):
    if (i*i > n): return True
    if(n%i==0): return False
    return esPrimoAux(i+2,n)

# Programa para elevar un número y no usar **
def elevar(a,n):
    if(n==0): return 1
    r = elevar(a,n>>1)
    r*=r
    if(n%2): r*=a
    return r

#Prgrama para sacar la raíz cuadrada
def raizCuad(n):
    return raizCuadAux(1,n,n)
def cuad(x): return x*x
def raizCuadAux(i,s,n):
    m = (i+s)/2
    err = 0,0001
    if (cuad(m-err)<n and cuad(m+err)>n): return m
    if (cuad(m)<n): return raizCuadAux(m,s,n)
    return raizCuadAux(i,m,n)

#Función que retorna una lista con todos los númneros enteros entre a y b (sin incluir a b) y un salto c.
def rango(a,b,c):
    if (a>=b): return []
    return [a] + rango(a+c,b,c)

print(rango(n))

#Dominio: dos enteros a y b.
#Codominio: Un Sí si a es múltiplo de b y si no un No
a,b = map(int, input().split())

def EsMultiplo(a,b):
  if (a%b == 0): return 'Sí'
  return 'No'

print(EsMultiplo(a,b))

#Programa para saber la tabla de múltiplicar o los múltiplos de un número n
n = int(input("Ingrese un número: "))
i = 1
while i <= 10:
    print(n * i)
    i += 1

#Ejercicio 11 de la tarea 3: Suma de suma
def sumaDoble(n):
  s1 = 0
  for i in range(1,n+1):
    s2 = 0
    for j in range(1,i+1):
      s2 += i*j
    s1 += s2
  return s1

def sumaDobleRecursivaCola(n, s1=0):
  if n == 0: return s1
  else:
    s2 = 0
    for j in range(1, n+1):
      s2 += n*j
    s1 += s2
    return sumaDobleRecursivaCola(n-1, s1)