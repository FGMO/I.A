from Busqueda_Informada import *
from Busqueda_Desinformada import *
import pygame
import random

def generarObtaculos(n):
	obstaculos = []
	for i in range(n - 1):
		obstaculos.append((random.randint(0, n - 1), random.randint(0, n - 1)))
	return obstaculos
	
def generarLaberinto(n, obstaculos):
	laberinto = []
	for i in range(n):
		laberinto.append([' ' for j in range(n)])

	for i in range(len(obstaculos)):
		x, y = obstaculos[i]
		laberinto[x][y] = '*'
	return laberinto

def imprimir(laberinto):
	for i in range(len(laberinto)):
		print(laberinto[i])

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
BLANCO1 = (252, 252, 252)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)

pygame.init()

dimensiones = [600, 600]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Laberinto")

juego_terminado = False
x1 = y1 = 0
x2 = y2 = 0
k = 0
l = 0
inicio = (0, 0)
final = (7, 7)
obstaculos = [(3, 4), (2, 2), (3, 2), (4, 2), (5, 2), (2, 4), (4, 4), (5, 4), (2, 5), (2, 6), (3, 6), (4, 6), (5, 6), (4, 5), (7, 3), (0, 3), (3, 0), (4, 0), (7, 0), (0, 7)]
print(obstaculos)
laberinto = generarLaberinto(8, obstaculos)
imprimir(laberinto)
ruta1 = aEstrella(laberinto, inicio, final)
busqueda(laberinto, inicio, final)
ruta2 = devolverRuta()
ruta2.append(final)

reloj = pygame.time.Clock()
ancho = int(dimensiones[0] / 8)
alto = int(dimensiones[1] / 8)
yi, xi = inicio
yf, xf = final
while juego_terminado is False:
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			juego_terminado = True
		if evento.type == pygame.KEYDOWN:
			if evento.key == pygame.K_r:
				k = l = 0
				
	pantalla.fill(BLANCO)
	color = 0
	for i in range(0, dimensiones[0], ancho):
		for j in range(0, dimensiones[1], alto):
			if color % 2 == 0:
				pygame.draw.rect(pantalla, BLANCO1, [i, j, ancho, alto], 0)
			else:
				pygame.draw.rect(pantalla, BLANCO, [i, j, ancho, alto], 0)
			color += 1
		color += 1
	for yo, xo in obstaculos:
		color = (150, 150, (random.randint(120, 200)))
		pygame.draw.rect(pantalla, color, [ xo * 75, yo * 75, ancho, alto], 0)
	pygame.draw.rect(pantalla, VERDE, [xi * 75, yi * 75, ancho, alto], 0)
	pygame.draw.rect(pantalla, ROJO, [xf * 75, yf * 75, ancho, alto], 0)
	pygame.draw.rect(pantalla, AZUL, [x1 * 75, y1 * 75, ancho, alto], 0)
	pygame.draw.rect(pantalla, AMARILLO, [x2 * 75, y2 * 75, ancho, alto], 0)
		
	if(k < len(ruta1)):
		y1, x1 = ruta1[k]
		k += 1
	else:
		k = 0
	if(l < len(ruta2)):
		y2, x2 = ruta2[l]
		l += 1
	else:
		l = 0
	pygame.display.flip()
	reloj.tick(2)
	
pygame.quit()
