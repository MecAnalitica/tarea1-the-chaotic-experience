import math
import sys
sys.setrecursionlimit(10000)

#Se definen dos funciones una para cada lado de la ecuación trascendental.
def f(t):
    return t
 
def g(t, v, k, theta):
    G = 9.81
    v = V * math.sin(math.radians(theta))
    return (k * v + G)/(G * k) * (1. - math.exp(-k * t))
 
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
        
def perturbativa(k, V, theta):
    g = 9.81
    v = V * math.sin(math.radians(theta))
    X = ((2 * v)/g)*(1 - ((k * v)/(3 * g)))
    print(X)
    
def T_sin_friccion(V, theta):
    g = 9.81
    v = V * math.sin(math.radians(theta))
    T = (2 * v)/g
    print(T)
    
#Definicion de los parametros e intervalo (A,B).     
A = 1.
B = 500
V = 500
k = 10e-10
theta = 65

print("SOLUCION TIEMPO T TIRO PARABOLICO CON RESISTENCIA AL AIRE")

if k = 0:
    T_sin_friccion(V, theta)
    
else:
    if (f(A) - g(A, V, k, theta))*(f(B) - g(B, V, k, theta)) < 0.:
        print("El resultado es: ")
        biseccion(A, B)
        perturbativa(k, V, theta)
    
    else:
        print("Seleccione un intervalo más grande.")
