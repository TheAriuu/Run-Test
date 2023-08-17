#Imprimir n Hola Mundos!
n = int(input())
def holamundo(n):
    r = []
    for i in range(n+1):
        palabra = "Hola Mundo!"
        r.append(palabra)
    return r
lista = holamundo(n)
for j in lista:
    print(j)