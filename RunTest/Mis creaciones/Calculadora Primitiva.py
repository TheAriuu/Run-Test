#Calculadora Primitiva
i, j = map(int, input().split())
n = int(input())
def calcu(i,j,n):
    if n==1: return i+j
    if n==2: return i-j
    if n==3: return i*j
    if n==4: return i//j
print(calcu(i,j,n))