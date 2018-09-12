import math
import sys
sys.setrecursionlimit(10000)

#Se definen dos funciones una para cada lado de la ecuación trascendental.
def f(t):
    return t
 
def g(t, V, k, theta):
    G = 9.81
    v = V * math.sin(theta)
    return ((k * v + G)/(G * k)) * (1. - math.exp(-k * t))
 
def biseccion(a, b):
    #Se calcula el punto medio entre el intervalo (A, B).
    c = (b + a)/2.
    
    #Se verifica si el punto medio de (A, B) coincide con la intersección de ambas funciones.
    if f(c) == g(c, V, k, theta):
        print(c) 
 
    #De no coincidir el punto medio con la intersección de f y g se redefinen los extremos del
    #intervalo, si el producto de las diferencias entre f y g en los puntos a y c es mayor que
    #cero, significa entonces que el la interseccion esta fuera de el intervalo (a, c), en caso 
    #contrario esta dentro del intervalo (a, c).
    if (f(a) - g(a, V, k, theta))*(f(c) - g(c, V, k, theta)) > 0.:
        a = c
        b = b
        biseccion(a, b)
 
    if (f(a) - g(a, V, k, theta))*(f(c) - g(c, V, k, theta)) < 0.:
        a = a
        b = c
        biseccion(a, b)
        
#Definicion de los parametros e intervalo (A,B).     
A = 1.
B = 1000
V = 500
k = 0.00001
theta = 65

print("SOLUCION TIEMPO T TIRO PARABOLICO CON RESISTENCIA AL AIRE")


if (f(A) - g(A, V, k, theta))*(f(B) - g(B, V, k, theta)) < 0.:
    print("El resultado es: ")
    biseccion(A, B)
  
else:
    print("Seleccione un intervalo más grande.")
