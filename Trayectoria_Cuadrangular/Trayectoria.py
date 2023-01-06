#!/usr/bin/env python3                         
# encoding: utf-8

#Linea 1 - “Shebang”,le indicamos a la máquina con qué programa lo vamos a ejecutar.
#Linea 2 - Python 3 - asume que solo se utiliza ASCII en el código fuente
#para usar utf-8 hay que indicarlo al principio de nuestro script encoding: utf-8

#!/usr/bin/env python3                         
# encodingc: utf-8

#Linea 1 - “Shebang”,le indicamos a la máquina con qué programa lo vamos a ejecutar.
#Linea 2 - Python 3 - asume que solo se utiliza ASCII en el código fuente
#para usar utf-8 hay que indicarlo al principio de nuestro script encoding: utf-8

#IMPORTA LIRBRERÍAS

#Importar la API de Ros para python
import rospy
#Importa el tipo de mensaje Vector3 del paquete geometry_msgs
from geometry_msgs.msg import Vector3
#Importa el tipo de mensaje Twist del paquete geometry_msgs
from geometry_msgs.msg import Twist
#Importa el tipo de mensaje Odometry del paquete nav_msgs
from nav_msgs.msg import Odometry
#Importa el tipo de mensaje Float32 del paquete std_msgs
from std_msgs.msg import Float32

#Otras librerías adicionales 
import time 
import numpy as np


######################################################################################333
#DEFINICIONES 

#Se define variable global L
global L

#Imprimir en pantalla y pedir el L en cm
print('Hola, usuario')
L = float(input("Ingrese el valor de Distancia ( cm ): "))
#Pasar de cm a m
result = L/100.0

##############################################################################33

def desplazamiento_x():
    #Para el desplazamiento del robot 
    vel_bot.linear.x = result/1.0
    vel_bot.angular.z = 0.0
    #Imprime en pantalla
    print('AVANCE')
    #Retardo
    time.sleep(3.0)
    #Se publica el mensaje de velocidad 
    pub_vel.publish(vel_bot) 

def giro():
    #Para el giro del robot     
    vel_bot.linear.x = 0.0
    vel_bot.angular.z = 1.52
    #Imprime en pantalla
    print('GIRO')
    #Retardo
    time.sleep(1.0)
    #Se publica el mensaje de velocidad 
    pub_vel.publish(vel_bot)

def pare():
    #Para detener el robot
    vel_bot.linear.x = 0.0
    vel_bot.angular.z = 0.0
    #Se publica el mensaje de velocidad 
    pub_vel.publish(vel_bot)
  
########################################################################################

#Se crea nodo y se inicializa
rospy.init_node('desplazamiento')

#Se crea una variable tipo Twist()
vel_bot = Twist()
#Se crea una variable tipo Float32()
distance = Float32()

#Se crea un objeto publicador 
pub_vel = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)

#########################################################################################

#Función principal 
if __name__ == '__main__': 
    try:    
            #Llama la función
            desplazamiento_x()
            #Retardo
            time.sleep(2.0)
            #Llama la función
            pare()
            #Retardo
            time.sleep(2.0)
            #Llama la función
            giro()
            #Retardo
            time.sleep(2.0)
            #Llama la función
            pare()
            #Retardo
            time.sleep(2.0)

            #Llama la función    
            desplazamiento_x()
            #Retardo
            time.sleep(2.0)
            #Llama a la función
            pare()
            #Retardo
            time.sleep(2.0)
            #Llama la función
            giro()
            #Retardo
            time.sleep(2.0)
            #Llama la función 
            pare()
            #Retardo
            time.sleep(2.0)

            #Llama la función 
            desplazamiento_x()
            #Retardo
            time.sleep(2.0)
            #Llama la función 
            pare()
            #Retardo
            time.sleep(2.0)
            #Llama la función 
            giro()
            #Retardo
            time.sleep(2.0)
            #Llama la función 
            pare()
            #Retardo
            time.sleep(2.0)

            #Llama la función
            desplazamiento_x()
            #Retardo
            time.sleep(2.0)
            #Llama la función 
            pare()
            #Retardo
            time.sleep(2.0)
            #Llama la función
            giro()
            #Retardo
            time.sleep(2.0)
            #Llama la función
            pare()
         
            #Para crear un archivo de texto. El "a" indica que lo que se añade no se vaya a borrar
            archive = open('distancia_txt',"a")
            #Para grabar los datos se utiliza .write()
            archive.write('%f\n'%result)
            #Se cierra 
            archive.close()

    except rospy.ROSInterruptException:    
        pass


    
