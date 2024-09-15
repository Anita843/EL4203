import math
from time import perf_counter
import numpy as np
import matplotlib.pyplot as plt

# definicion de la clase pedida
class Caminos:
    def __init__(self,n,m):
        self.n = n #ancho grilla
        self.m = m #largo grilla
    
    # metodos para calcular el tiempo por separado    
    def medir_tiempo_recursivo(self):
        tiempo_inicio = perf_counter()
        resultado = self.cantidad_caminos()
        tiempo_total = perf_counter() - tiempo_inicio
        return tiempo_total
    
    def medir_tiempo_iterativo(self):
        tiempo_inicio = perf_counter()
        resultado = self.cantidad_caminos_2()
        tiempo_total = perf_counter() - tiempo_inicio
        return tiempo_total
    
    # metodo generalizado para calcular el tiempo con un decorador
    def medir_tiempo(func): 
        def decorador(*args, **kwargs): # permite que pueda aplicarse a cualquier función
            inicio = perf_counter()
            resultado = func(*args, **kwargs)
            tiempo_total = perf_counter() - inicio
            return resultado, tiempo_total # devuelve la cantidad de caminos y el tiempo de ejecución
        return decorador        
    
    
    def cantidad_caminos(self,x=0,y=0): # metodo recursivo
        if x == self.n-1 and y==self.m-1: # caso base
            return 1
        if x>=self.n or y>=self.m: # no hay mas caminos, se sale de la grilla
            return 0
        # si se elige hacia la derecha o hacia abajo
        return self.cantidad_caminos(x+1,y)+self.cantidad_caminos(x,y+1)

    def cantidad_caminos_2(self): # metodo iterativo
        fila = [1] * self.m # representa la primera fila de la grilla
        for i in range(1, self.n): # recorre cada fila
            for j in range(1, self.m): # recorre cada celda
                fila[j] += fila[j - 1] # actualiza el número de caminos posibles para cada celda
        return fila[self.m - 1]

    @medir_tiempo
    # se aplica el decorador a una nueva funcion donde se pueden aplicar ambos metodos
    def calcular_caminos(self, metodo):
        if metodo == 'recursivo':
            resultado = self.cantidad_caminos()
        elif metodo == 'iterativo':
            resultado = self.cantidad_caminos_2()
        else:
            raise ValueError("Método no reconocido. Use 'recursivo' o 'iterativo'.")
        return resultado


# prueba de que funcione bien
pcb = Caminos(3, 3)
rec = pcb.calcular_caminos('recursivo')
it = pcb.calcular_caminos('iterativo')

# funcion para generar gráficos comparativos
def generar_grafico(N):
    N_valores = range(1, N+1)  # tamaños de grillas a comparar
    tiempos_recursivos = []
    tiempos_iterativos = []

    for n in N_valores:
        pcb = Caminos(n, n)

        # Medimos tiempos de ejecución
        a, tiempo_recursivo = pcb.calcular_caminos('recursivo')
        b, tiempo_iterativo = pcb.calcular_caminos('iterativo')

        tiempos_recursivos.append(tiempo_recursivo)
        tiempos_iterativos.append(tiempo_iterativo)

    # Graficamos los tiempos
    plt.plot(N_valores, tiempos_recursivos, label="Recursivo", marker='o')
    plt.plot(N_valores, tiempos_iterativos, label="Iterativo", marker='x')
    plt.xlabel("Tamaño de la grilla N x N")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Comparación de Tiempos de Ejecución")
    plt.legend()
    plt.grid(True)
    plt.savefig("grafico_comparativo.svg", format="svg") 
    plt.show()

# generamos el gráfico hasta N=16
# comenté el generar_grafico(16) que cree porque se demora lo suyo (en mi pc al menos)
# descomentar si se quiere crear nuevamente el grafico
# generar_grafico(16)