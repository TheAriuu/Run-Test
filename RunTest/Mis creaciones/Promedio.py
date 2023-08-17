#Sacar el promedio de un conjunto de números
T = int(input())
R = []
cantElementos = T
while T:
  C = int(input())
  R.append(C)
  T -= 1
print(sum(R)/cantElementos)