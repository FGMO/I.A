import random
#import sys

n = 8 #Variable que indica el numero de reinas
soluciones = [] #Arreglo que almacena las posiciones de las reinas
#soluciones = [(-1, -1)]*n
tablero = [] #Tablero en le que se mostrara la solucion

#Bucle que inicializa el tablero con ceros
for i in range(n):
	tablero.append([0 for j in range(n)])

#METODO QUE UBICA LAS REINAS EN EL TABLERO
def ubicarReinas(i):
	if(i >= n): #Condicion de salida.
		print("Termina")
		return 0
	print("Ingresa a nodo:", i)
	f, c = (i, generaAleatorio(soluciones, n)) #Crea la tupla con la posicion en la fila y columna.
	print("Fila:", f, "Columna:", c)
	if(esValido((f, c))): #Valida si la posicion generada esta disponible para ubicar la Reina.
		soluciones.append((f, c)) #Aniade la posicion al arreglo de soluciones
		ubicarReinas(i + 1) #Despliega el siguiente nodo
	else: #Si la posicion no esta disponible
		print("Vuelve a nodo anterior:", i - 1) 
		soluciones.pop() #Retira la ultima tupla aniadida
		ubicarReinas(i - 1) #Regresa al nodo anterior
	
#METODO QUE VALIDA LA POSICION EN LA QUE SE UBICAN LAS REINAS
def esValido(posicion):
	f, c = posicion #Resive la tupla con la posicion a ser validada
	valido = False
	#Si en el arreglo existe unicamente una reina, esta por defecto es una posicion valida
	if(len(soluciones) == 0): 
		valido = True #Siempre indica como disponible la primer ubicacion donde va la primer reina
	for i in range(len(soluciones)): #Recorre el arreglo de soluciones
		f_r, c_r = soluciones[i] #Recupera las tuplas con las posiciones del arreglo de soluciones
		print("Entra >","Posicion Reina:", (f_r, c_r), "Posicion nueva:", (f, c))
		#Condicion para validar si la nueva posicion esta en una columna y diagonales distintas de las
		#Reinas ya ubicadas
		if(c_r != c and abs(f_r - f) != abs(c_r - c)):  
			print("Cumple >>", "Posicion Reina:", (f_r, c_r), "Posicion Nueva:", (f, c))
			valido = True #En caso de estar disponible la posicion nueva
		else:
			print("NO Cumple >>>", "Posicion Reina:", (f_r, c_r), "Posicion nueva:", (f, c))
			valido = False #En caso de que la posicion no este disponible
			break #Acaba el ciclo for
	return valido #Retorna un valor boolean para indicar la disponibilidad de la celda en el tablero

#METODO QUE GENERA POSICIONES ALEATORIAS PARA LAS COLUMNAS DE LAS REINAS
def generaAleatorio(soluciones, n):
	if(len(soluciones) == 0):# Condicion que genera un valor para la columna de la primera reina
		return random.randint(0, n - 1) #Retorna un valor aleatorio entre 0 y n-1
	c = soluciones[len(soluciones)-1][1] #Recupera la ultima tupla en el arreglo de soluciones
	#Genera un arreglo con el valor de la columna de la solucion recuperada del arreglo y lo resta y suma
	#mas 1
	arr = [c - 1, c, c + 1]  
	if(len(soluciones) > 1):# Condicon que verifica que en el arreglo hay mas de dos reinas ubicadas
		for i in range(len(soluciones) - 1):# Bucle que recorre el arreglo hasta n-1
			c = soluciones[i][1] #Recupera los valores de las columnas de las reinas anteriores
			arr.append(c) #Aniade los valores recuperados al arreglo
	print(soluciones, arr, n)
	aleatorio = True #Variable que verifica que se genere un aleatorio unico
	aux = 0 #Contador auxiliar
	while(aleatorio): #Bucle que se ejecuta mientras el aleatorio sea unico
		alt = random.randint(0, n - 1) #Genera un valor aleatorio
		cont = 0 #Contador
		#Bucle que rrecorre el arreglo con los valores de las columnas de las reinas ya ubicadas
		for i in range(len(arr)): 
			
			if(arr[i] != alt): #Condicion que verifica que se genere un aleatorio unico
			#Si se trata de un aleatorio unico el contador incrementa su valor en 1 
				cont += 1
				
			#Condicion que verifica si el aleatorio generado es igual a uno ya generado previamente
			if(arr[i] == alt): 
				aux += 1 #Incrementa el valor del contador auxiliar en 1
		
	#Condicion que verifica que ya se rrecorrio todo el arreglo y la posicion que se genero es unica
		if(cont >= len(arr)): 
			aleatorio = False #Setea el valor de la variable a false para detener el bucle
			return alt #Retorna la nueva posicion generada
		
	#Condicion que verifica que ya se rrecorrio todo el arreglo y no existen posiciones disponibles
		if(aux >= len(arr)):
			aleatorio = False #Setea el valor de la variable a false para detener el bucle
			return 0 #Retorna 0 si no se encontro una posicion disponible

#sys.setrecursionlimit(10000)
ubicarReinas(0) #Llamada al metodo

print("Solucion:", soluciones)
for i in  range(len(soluciones)): #Bucle para aniadir las soluciones al tablero
	tablero[soluciones[i][0]][soluciones[i][1]] = 1 #1 Represeta a una reina en el tablero

for i in range(len(tablero)): #Bucle que imprime el tablero con la solucion
	print(tablero[i])
