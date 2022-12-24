# Se elabora dos gráficas con los datos almacenados en el archivo . txt , una de las posiciones y 
# la otra de las orientaciones expresadas en ángulos de Euler.

#!/usr/bin/env python3                         
# encoding: utf-8

#Linea 1 - “Shebang”,le indicamos a la máquina con qué programa lo vamos a ejecutar.
#Linea 2 - Python 3 - asume que solo se utiliza ASCII en el código fuente
#para usar utf-8 hay que indicarlo al principio de nuestro script encoding: utf-8

#Importa librerías
import pandas as pd 
import matplotlib.pyplot as plt 

#Lectura de la base de datos 
path = ('x.txt')
data = pd.read_csv(path, header=None, names=['Posición x'])

path = ('y.txt')
data1 = pd.read_csv(path, header=None, names=['Posición y'])

path = ('z.txt')
data2 = pd.read_csv(path, header=None, names=['Orientación'])

#Gráfica de la base de datos
plt.figure(1)
plt.title('Gráfica de odometría')
plt.xlabel('Posicion en x')
plt.ylabel('Posicion en y')
plt.plot(data,data1,'b')
plt.grid()

plt.figure(2)
plt.title('Gráfica de la orientación')
plt.plot(data2,'r')
plt.grid()

plt.show()

