#<<<<<<Modulos Necesarios>>>>>>
import numpy as np
import matplotlib.pyplot as plt


s = """
+-----------------------------------------------------------------------------------------------------------+
|	Materia:					<Mecanica Analitica>														|
|																											|
|	Tarea:						Tarea 1																		|
|	Autores:					Salvador Negrete, Rodrigo Gardunio, Edson Esqueda, Edgar Ocampo				|
|	Lenguaje:					Python 2.7 (se necesitan las librerias numpy y matplotlib)					|
|	Profesor:					Gustavo Niz																	|
|	Fecha:						13 de Septiembre de 2018													|
|	Archivo a ejecutar:			tarea1.py 																	|
+-----------------------------------------------------------------------------------------------------------+
|	Descripcion:																							|
|	Este programa resuelve la primera parte de la tarea 1 de Mecanica Analitica, "Calculo Numerico de un 	|
|	Misil", dentro del codigo se encuentran los incisos y como este script de python resuelve cada uno de 	|
|	los incisos. Se detalla la resolucion de esta parte de la tarea a continuacion:							|
|																											|
|	El usuario introduce los valores del angulo inicial "theta" y la velocidad inicial "v0" y se computan	|
|	los valores de V y U, como:		U = v0 * cos(theta)		V = v0 * sin(theta)								|
|																											|
|	El usuario ingresa el numero de valores de "k" en los que se debe de dividir el intervalo de 0 a 1      |
|	equitativamente o introduce manualmente los valores de "k" entre 0 y 1.									|
|																											|
|	Se calculan los diferentes tiempos de vuelo para los diferentes valores de la constante de fuerza retar-|
|	dante "k", con angulo y velocidad iniciales ingresados por el usuario.									|
|																											|
|	El script luego calcula la maxima distancia alcanzada "R" para el tiempo de vuelo "T" y la constante "k"|
|	respectiva al tiempo.																					|
|																											|
|	Se genera un grafico de Rango en funcion de "k" para observar el comportamiento de esta relacion, para  |
|	comparar posteriormente con la aproximacion hecha en clase.												|
|																											|
|	Se genera un segundo grafico de la posicion horizontal y vertical y se describen las trayectorias toma- |
|	das por el misil para los diferentes valores de "k".													|
|																											|
|	Se generan 3 graficos de Altura contra Tiempo, Velocidad Horizontal contra Tiempo y Velocidad Vertical  |
|	contra Tiempo.																							|
|																											|
|	Se calculan los angulos necesarios para obtener la mayor distancia alcanzada para los diferentes valores|
|	de "k".																									|
|																											|
|	INPUT: angulo inicial "theta", velocidad inicial "v0" y criterio para division del intervalo o valores  |
|	de "k".																									|
|																											|
|	OUTPUT: Tiempo de vuelo "T" para valores de "k", maxima distancia alcanzada "R" para valores de "k", 	|
|	grafico de Rango vs "k", grafico de trayectoria de misil para diferentes valores de "k", grafico de 	|
|	altura vs tiempo, velocidad horizontal vs tiempo, velocidad vertical vs tiempo y angulos necesarios para|
|	obtener el mayor alcance.																				|
+-----------------------------------------------------------------------------------------------------------+
"""






#
#==============================================<FUNCIONES>=============================================================
#
# o = o = o = o = FUNCION kgenerator = o = o = o
s = """
+-----------------------------------------------------------------------------------+
|	Esta funcion kgenerator genera la lista de los valores k y los parametros se 	|
|	explican a continuacion:	(kgenerator regresa una lista)						|
|																					|
|	flag:	(flag es int)															|
|	   flag != 1: El usuario ingresa el numero de puntos de k que necesita en el 	|
|				  intervalo de 0 a 1 (vease nkpoints).								|
|	   flag == 1: (default) El usuatio ingresa el vector de los valores de k 		|
|				  manualmente (vease kvector).										|
|																					|
|	nkpoints: Numero de  puntos de k que el usiario necesita en el intervalo		|
|			  0 a 1 (default = 0), con default el usuario debe de ingresar los		|
|			  puntos manualmente. (nkpoints es int)									|
|																					|
|	kvector: Lista de puntos para k en el intervalo 0 a 1 sin agregar el 0. 		|
|			 (lista de floats)														|
|																					|
|																					|
|	Ejemplos:																		|
|																					|
|				K1 = kgenerator(flag = 0, nkpoints = 4)								|
|			 => K1 = [0, 0.2, 0.4, 0.6, 0.8]										|
|																					|
|				K2 = kgenerator(kvector = [0.001, 0.002, 0.01, 0.02])				|
|			 => K2 = [0, 0.001, 0.002, 0.01, 0.02]									|
|																					|
+-----------------------------------------------------------------------------------+
"""
def kgenerator(flag = 1, nkpoints = 0, kvector = [0]):

	if flag != 1:

		print "Generando Valores de k..."
		if nkpoints > 0:											#El usuario ingreso el numero de valores  de k que quiere

			d = 1.0/(nkpoints + 1)										#El intervalo equisdistante entre los puntos de K
			kdrop = [0 + i*d for i in range(nkpoints + 1)]
			print "Los valores de k son {}".format(kdrop)
			return kdrop											#Retorno del vector de K con el numero de valores equisdistantes
		else:														#El usuario marco flag = 0 pero no asigno valor para nkpoints

			return 0												#k = 0 es el caso estandar, no hay resistencia del aire

	else:															#flag es diferente del caso 0, entonces se tiene que ingresar el vector de K

		kvector.sort()												#se ordenan los elementos del vector ingresado


		#Banderas para comprobacion de que los elementos del vector estan dentro del intervalo
		flagtop = True
		flagdown = True
		genflag = True

		while(genflag == True):

			if kvector[0] <= 0:										#Se comprueba que el primer elemento de la lista es menor que 0 y esta fuera del intervalo, se elimina de la lista y se mantiene la condicion para hacer otra verificacion
				kvector.pop(0)
				flagdown = True
			else:
				
				flagdown = False

				if kvector[len(kvector) - 1] > 1:
					kvector.pop()
					flagtop = True										#Se comprueba que el ultimo elemento de la lista esta fuera del intervalo, se elimina este elemento y se mantiene la condicion para hacer otra verificacion
				else:
					flagtop = False

			genflag = (flagtop and flagdown)							#Ambas condiciones deben de haber cambiado para que la bandera cambie

		kvector.insert(0,0)

		return kvector



#
#===================================================<FIN DE FUNCIONES>=============================================================
#







s = """
+-------------------------------------------------------------------------------------------------------+
|	Aqui comienza la solucion del inciso a), agregar valores a los parametros soluciona el inciso b)	|
+-------------------------------------------------------------------------------------------------------+
"""

#=================================< PARAMETROS INICIALES >=======================================

#<<<<<ESTOS SON LOS UNICOS PARAMETROS INGRESADOS POR EL USUARIO>>>>>>

theta = 65*(np.pi/180)													#theta es el valor del angulo inicial del misil en radianes (ingresar flotante)
v0 = 500.															#v0 es la magnitud de la velocidad inicial (ingresar flotante)
K0 = kgenerator(kvector = [0.005, 0.01, 0.02, 0.04, 0.08])			#El vector de los puntos de k dentro del intervalo (informacion de funcion se encuentra mas arriba)

#<<<<<<FIN DE LOS PARAMETROS INGRESADOS POR EL USUARIO>>>>>>>>



g = 9.81									#m/s2 aceleracion de la gravedad

U = v0*np.cos(theta)						#U y V son variables del problema
V = v0*np.sin(theta)



# = o = o = o Calculo del tiempo maximo de vuelo T para cada valor de k o = o = o =  (Usando Newton)

T = []										#Iniciacion del vector T

for k in K0:								#Solucion de T para cada valor de K

	T0 = (2.0*V)/g							#Aproximacion inicial al resultado de T

	if k == 0:
		T.append(T0)
	else:
		for i in range(100):

			f_T0 = ((k*V + g)/(g*k))*(1 - np.exp((-1)*k*T0)) - T0 			#Calculo de f(T0)
			df_T0 = ((k*V + g)/(g*k))*(k*np.exp((-1)*k*T0)) - 1				#Calculo de f'(T0)

			T1 = T0 - (f_T0)/(df_T0) 										#Iteracion para aproximacion

			if abs(T1 - T0) < 0.00001:										#Criterio para detener iteracion
				T.append(T1)
				break

			if i == 99:														#Se guarda el valor de T a pesar de no encontrarlo
				T.append(T1)
				break
			
			T0 = T1

s = """
+-------------------------------------------+
|	Aqui termina la solucion del inciso a)	|
+-------------------------------------------+
"""


#==================================<CALCULO DE DISTANCIA MAXIMA Y PLOTEO>================================
R0 = []
for i in range(len(K0)):
	if i == 0:
		R0.append( ((v0**2)/g)*np.sin(2*theta) )
	else:
		R0.append( (U/K0[i])*(1 - np.exp((-1)*K0[i]*T[i])) )		#R0 es el vector que contiene los alcances maximos para cada k asociada

#<PLOTEO Alcance Maximo vs k>

#Interpolacion
#kinterp = np.arange(K0[0], K0[len(K0)-1], 0.001)
#print kinterp
#Rinterp = np.interp(kinterp, K0, R0)
#print Rinterp
plt.figure()
plt.plot(K0,R0)
plt.xlabel('Constante de Fuerza Retardante k ('r'$s^{-1}$' ')')
plt.ylabel('Alcance Maximo en x (m)')
plt.title('Alcance Maximo vs k')

#<FIN DE PLOTEO>
s = """
+-------------------------------------------------------------------------------+
|	Aqui termina la solucion del inciso b) y comienza la solucion del inciso c)	|
+-------------------------------------------------------------------------------+
"""

#o = o = o = o =Computo de las trayectorias para cada valor de k asociado= o = o = o = o
T_plotter = np.linspace(0,T[0], 1000)							#Tiempo maximo de computacion correspondiente a tiro parabolico y k = 0 y hecho para generar vectores de ploteo de mismo numero de elementos

x_plotter = []													#Inicializacion de arreglo que sera de 2 dimensiones conteniendo las posiciones
y_plotter = []													#a traves del tiempo para cada valor de k asociado

for k in K0:

	if k == 0:									#Caso parabolico
		x_plotter.append( [ v0*t*np.cos(theta) for t in T_plotter ] )
		y_plotter.append( [ (v0*t*np.sin(theta)) - (g*(t**2)/2) for t in T_plotter ] )
	else:										#Casos donde existe resistencia del aire
		x_plotter.append( [ (U/k)*(1 - np.exp((-1)*k*t)) for t in T_plotter ] )
		y_plotter.append( [ (((k*V + g)/(k**2))*(1 - np.exp((-1)*k*t))) - (g*t/k) for t in T_plotter ] )

#o = o = o = o =Ploteo de las trayectorias en una sola Figura= o = o = o = o

plt.figure()
for i in range(len(K0)):

	plab = 'k = {}'.format(K0[i])
	plt.plot(x_plotter[i],y_plotter[i], label = plab )

max_y = np.amax(y_plotter[0]) + 200
plt.axis([0,R0[0], 0, max_y])
plt.xlabel('Distancia Recorrida x (m)')
plt.ylabel('Distancia Recorrida y (m)')
plt.title('Posicion de Misil para cada valor de k')
plt.legend()

#FIN DEL PLOTEO DE TRAYECTORIAS

s = """
+-------------------------------------------------------------------------------+
|	Aqui termina la solucion del inciso c) y comienza la solucion del inciso d)	|
+-------------------------------------------------------------------------------+
"""
#= o = o = o = o =PLOTEO DE ALTURA CONTRA TIEMPO, VELOCIDAD HORIZONTAL CONTRA TIEMPO Y VELOCIDAD VERTICAL CONTRA TIEMPO o = o = o = o =

#=====> INICIA PLOTEO DE ALTURA CONTRA TIEMPO

plt.figure()
for i in range(len(K0)):
	plab = 'k = {}'.format(K0[i])
	plt.plot(T_plotter, y_plotter[i], label = plab)
plt.axis([0,T[0], 0, max_y])
plt.xlabel('Tiempo (s)')
plt.ylabel('Altura (m)')
plt.title('Altura Respecto al Tiempo para Cada Valor de k')
plt.legend()

#=====> TERMINA PLOTEO DE ALTURA CONTRA TIEMPO


#Calculo de velocidad Horizontal y Vertical

vx_plotter = []								#Iniciacion de vectores para las velocidades, quedan del mismo tamanio que T_plotter
vy_plotter = []								

for k in K0:

	if k == 0:
		vx_plotter.append( [ v0*np.cos(theta) for t in T_plotter ] )
		vy_plotter.append( [ (v0*np.sin(theta)) - g*t for t in T_plotter ] )
	else:
		vx_plotter.append( [ v0*np.exp((-1)*k*t) for t in T_plotter ] )
		vy_plotter.append( [ ((k*v0 + g)/(k))*np.exp((-1)*k*t) - g/k for t in T_plotter ] )


#=====> INICIA PLOTEO DE VELOCIDAD HORIZONTAL CONTRA TIEMPO

plt.figure()
for i in range(len(K0)):
	plab = 'k = {}'.format(K0[i])
	plt.plot( T_plotter, vx_plotter[i], label = plab)
max_y = np.amax(vx_plotter[0]) + 30.
#plt.axis([0 , T[0], 0, max_y] )
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad Horizontal (m/s)')
plt.title('Velocidad Horizontal Contra Tiempo para Cada Valor de k')
plt.legend()

#=====> TERMINA PLOTEO DE VELOCIDAD HORIZONTAL CONTRA TIEMPO



#=====> INICIA PLOTEO DE VELOCIDAD VERTICAL CONTRA TIEMPO

plt.figure()
for i in range(len(K0)):
	plab = 'k = {}'.format(K0[i])
	plt.plot( T_plotter, vy_plotter[i], label = plab)
max_y = np.amax(vy_plotter[0]) + 30
min_y = (-1)*max_y
plt.axis( [0, T[0], min_y, max_y] )
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad Vertical (m/s)')
plt.title('Velocidad Vertical Contra Tiempo para Cada Valor de k')
plt.legend()
plt.axhline(0, color = 'black')

#======> TERMINA PLOTEO DE VELOCIDAD HORIZONTAL CONTRA TIEMPO

s = """
+------------------------------------------+
|	Aqui termina la solucion del inciso d) |
+------------------------------------------+
"""

plt.show()

