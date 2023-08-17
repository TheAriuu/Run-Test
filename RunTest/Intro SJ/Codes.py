

#Saber si un número es primo

'''"Rcursivo (De cola)"
def esPrimoRC(n,i=3):
    if n==2: return True
    if not n%2: return False
    if i*i>n: return True
    if n%i==0: return False
    return esPrimoRC(n,i+2)

"Recursivo (De pila)"
def esPrimoRP(n):
    if n==2: return True
    if n%2==0: return False
    return esPrimoAux(3,n)
def esPrimoAux(i,n):
    if i*i>n: return True
    if n%i==0: return False
    return esPrimoAux(i+2,n)

"Iterativo"
def esPrimoI(n):
    if n==2: return True
    if not n%2: return False
    i = 3
    while i*i<=n:
        if n%i==0: return False
        i+=2
    return True

print(esPrimoRC(n))
print(esPrimoRP(n))
print(esPrimoI(n))

#Determinar la edad dado el año de nacimiento
n = int(input("Año de nacimiento: "))
años = 2023-n
edadMeses = años*12
edadDias = edadMeses*30
print("Ud tiene: {} años".format(años))
print("Edad en meses: {}".format(edadMeses))
print("Edad en dias: {}".format(edadDias))

#Sacar el área de un triángulo
b,a = map(float, input("Ingrese la base y la altura: ").split())
areaTriangulo = b*a/2
print("Área = {:.2f}".format(areaTriangulo))'''

#Hacer calculadora del IMC (idea)
#Cálculo del IMC
p = float(input("Ingrese su peso: "))
h = float(input("Ingrese su altura en metros: "))

def conversion(p,h):
    l2k= p/2.205
    p2m = h*2.54
    print(l2k,p2m)

IMC = p/(h*h)

def clasificacion(IMC):
    if IMC<18.5: print("Su estado es Desnutrición")
    elif IMC<25: print("Su estado es Normal")
    elif IMC<=30: print("Su estado es Sobrepeso")
    elif IMC<=40: print("Su estado es Obesidad Leve")
    else: print("Su estado es Obesidad Grave")


print("Su IMC es: {:.2f} y {}".format(IMC))
print(clasificacion(IMC))

#Año bisiesto