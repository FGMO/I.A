from Busqueda_Informada import *
from Busqueda_Desinformada import *
import random

def generarLaberinto(n = 8):
    laberinto = []
    for i in range(n):
        laberinto.append([' ' for j in range(n)])

    for i in range(n - 1):
        laberinto[random.randint(0, n - 1)][random.randint(0, n - 1)] = '*'
    return laberinto

def imprimir(laberinto):
    for i in range(len(laberinto)):
        print(laberinto[i])
        
def solucionAestrella(ruta, laberinto):
    for i in  range(len(ruta)):
        laberinto[ruta[i][0]][ruta[i][1]] = '-'
        if i >=  len(ruta)-1:
            laberinto[ruta[i][0]][ruta[i][1]] = 'M'

if __name__ == '__main__':
    laberinto = generarLaberinto()
    inicio = (0, 0)
    final = (7, 7)
    ruta = aEstrella(laberinto, inicio, final)
    print(ruta)
    busqueda(laberinto, inicio, final)
    solucionAestrella(ruta, laberinto)
    imprimir(laberinto)
