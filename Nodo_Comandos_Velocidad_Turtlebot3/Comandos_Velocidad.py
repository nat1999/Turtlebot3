#!/usr/bin/env python3                         
# encoding: utf-8

#Linea 1 - “Shebang”,le indicamos a la máquina con qué programa lo vamos a ejecutar.
#Linea 2 - Python 3 - asume que solo se utiliza ASCII en el código fuente
#para usar utf-8 hay que indicarlo al principio de nuestro script encoding: utf-8

#Realizado por Natalia Arenas Londoño

import rospy                          #Importar la API de Ros para python
from geometry_msgs.msg import Twist   #Importa el tipo de mensaje Twist del paquete geometry_msgs

#Crear un nodo

rospy.init_node('mover_robot')                                    #Inicializar el nodo
pub_vel = rospy.Publisher('cmd_vel',Twist,queue_size=1)           #Se crea objeto publicador

vel_bot = Twist()                                                 #Crear la variable del tipo Twist

#Para modificar la velocidad lineal y angular

vel_bot.linear.x = 0.2
vel_bot.angular.z = 0.3

fs = 10                    #La frecuencia de publicación de los mensajes 
pub_rate = rospy.Rate(fs)  #Se crea un objeto que permita publicar a determinada frecuencia 

#Para publicar 100 veces el mismo mensaje de velocidad
for i in range(100):
    pub_vel.publish(vel_bot)      #Para publicar el mensaje de velocidad
    pub_rate.sleep()              #Retardo 
    print('nro_comando: %d ', i) 
    print('---')

#Para detener al robot

vel_bot.linear.x = 0.0
vel_bot.angular.z = 0.0
pub_vel.publish(vel_bot) 
print('--Terminado--')
