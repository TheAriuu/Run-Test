n = int(input())
bi = int(input())
'''bf = int(input())'''


#Conversor de decimal a cualquier base
def DectoB(n,b):
    return D2b(n,b,0,1)
def D2b(n,b,bi,pot):
    if n==0: return bi
    return D2b(n//b, b, bi+(n%b)*pot, pot*10)


#Conversor de cualquier base a decimal
def BtoDec(n,b):
    return b2D(n,b,0,1)
def b2D(n,b,dec,pot):
    if (n==0): return dec
    return b2D(n//10, b, dec+(n%10)*pot, pot*b)

#Conversor de bases (para bases del 2 al 10)
def Base2base(n,bi,bf):
    decimal = BtoDec(n,bi)
    resultado = DectoB(decimal, bf)
    return resultado

print(DectoB(n,bi))