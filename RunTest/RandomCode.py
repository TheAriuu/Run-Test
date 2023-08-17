import sys
sys.setrecursionlimit(1000000)
n=int(input())
'''a = int(input())'''

#Es par o impar?
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