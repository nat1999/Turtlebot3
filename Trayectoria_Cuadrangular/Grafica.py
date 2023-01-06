#!/usr/bin/env python3                         
# encoding: utf-8

#Linea 1 - “Shebang”,le indicamos a la máquina con qué programa lo vamos a ejecutar.
#Linea 2 - Python 3 - asume que solo se utiliza ASCII en el código fuente
#para usar utf-8 hay que indicarlo al principio de nuestro script encoding: utf-8

#Importa las librerías 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np

#Base de datos
path3 = ('distancia_txt')
#Lectura de la base de datos 
data3 = pd.read_csv(path3, header=None)
#Selecciona los elementos en base a la posición 
r =  data3.iloc[:,0]
#Imprime en pantalla
print(r)


plt.figure(1)
#Las coordenadas 
x=[0,r[0],r[0],0,0]
y=[0,0,r[0],r[0],0]
#Título de la gráfica
plt.title('Trayectoria cuadrangular')
#Título para el eje x de la gráfica
plt.xlabel('Eje x')
#Título para el eje y de la gráfica 
plt.ylabel('Eje y')
#Condiciones de la graficación 
plt.plot(x,y,marker ='o')
#Rejillas
plt.grid()
#Mostrar la gráfica 
plt.show()
