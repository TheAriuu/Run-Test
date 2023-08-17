#Función para sacar logaritmo
def logaritmo(a,x):
    if a==1: return 0
    resultado = 0
    while x>=a:
        x = x/a
        resultado += 1
    return resultado

#Operaciones con potencias:
n = int(input("¿Qué quieres hacer "))
def potencias(n):
    if n==1:
        #Genera una lista de potencias
        a = int(input("¿Hasta que potencia quieres la lista? "))
        b = int(input("potencia = "))
        r = []
        for i in range(0,a+1):
            operacion = b**i
            descripcion = f"{b}^{i} es {operacion}"
            r.append(descripcion)     
        for elemento in r:
            print(elemento)

    elif n==2:
        #Verifica potencias
        i = int(input("¿Qué número quieres verificar? "))
        j = int(input("potencia = "))
        e = logaritmo(j,i)
        def esPot(i,j):
            if i%j: return i==1
            return esPot(i//j,j)
        if esPot(i,j): print(esPot(i,j),f"y es {j}^{e}")
        else: print(esPot(i,j))
    else:
        print("Opción no es válida")
potencias(n)