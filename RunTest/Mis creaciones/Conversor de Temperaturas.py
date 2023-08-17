#Conversor de temperaturas
n= int(input())
def temperatura(n):
    if n==1:
    #Celcius a farenheit
        c = float(input("Ingrese la temperatura en Celsius: "))
        c2f = c*(9/5) + 32
        print("{:.2f} Celcius es igual a {:.2f} farenheit".format(c,c2f))
    elif n==2:
    #Farenheit a celcius
        f = float(input("Ingrese la temperatura en Fahrenheit: "))
        f2c = (f-32) * (5/9)
        print("{:.2f} farenheit es igual a {:.2f} celcius".format(f,f2c))
    else:
        print("Opción no es válida")
temperatura(n)