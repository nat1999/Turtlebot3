#Se publica los estados indefinidos (S=(x , y , θ) ) 
#de un robot que se encuentra ejecutando comandos de velocidad con v=0.2 [m/s] y w=0.3[rad/s] 


#!/usr/bin/env python3                         
# encoding: utf-8

#Linea 1 - “Shebang”,le indicamos a la máquina con qué programa lo vamos a ejecutar.
#Linea 2 - Python 3 - asume que solo se utiliza ASCII en el código fuente
#para usar utf-8 hay que indicarlo al principio de nuestro script encoding: utf-8

#Realizado por Natalia Arenas Londoño

#Importar la API de Ros para python
import rospy                          
#Importa el tipo de mensaje Twist del paquete geometry_msgs
from geometry_msgs.msg import Twist   
#Importa el tipo de mensaje Vector3 del paquete geometry_msgs
from geometry_msgs.msg import Vector3
#Importa el tipo de mensaje Odometry del paquete nav_msgs
from nav_msgs.msg import Odometry
#Importa librería para la transformación de quaternios a ángulos de Euler
from tf.transformations import euler_from_quaternion, quaternion_from_euler 

##############################################################################################3

#Función que recibe el mensaje de odometría 
def callback(odm):
           #Para indicar variables globales 
            global roll, pitch , yaw   
            #Se crea una variable tipo Vector3()                    
            odom_xy = Vector3()
            #Se conoce la odometría (posición "x" y "y")
            odom_xy.x = odm.pose.pose.position.x
            odom_xy.y = odm.pose.pose.position.y
            #Se conoce la orientación mediante la transformación de quaternios a ángulos de Euler
            orientation_q = odm.pose.pose.orientation
            orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
            (roll, pitch, yaw) = euler_from_quaternion (orientation_list)

            #Muestra en pantalla
            print('La orientacion = ',yaw)
            print('Posición x =   ',odom_xy.x)
            print('Posición y = ',odom_xy.y)
            print('-----')
            

            #Se crea un objeto que permita publicar a determinada frecuencia   
            pub_rate = rospy.Rate(10) 
            #Retardo
            pub_rate.sleep()
            #Se publica mensajes en el tópico /odom_xy
            pub_xy.publish(odom_xy)

            #Para crear un archivo de texto. El "a" indica que lo que se añade no se vaya a borrar
            archive = open('datos.txt',"a")
            #Para grabar los datos se utiliza .write()
            archive.write('%f\n'%odom_xy.x + '%f\n'%odom_xy.y + '%f\n'%yaw)
            #Se cierra 
            archive.close()
                                                        
            #Para la posición x
            archive_x = open('x.txt',"a")
            #Para grabar los datos se utiliza .write()
            archive_x.write('%f\n'%odom_xy.x)
            #Se cierra 
            archive_x.close()
                                                        
            #Para la posición y
            archive_y = open('y.txt',"a")
            #Para grabar los datos se utiliza .write()
            archive_y.write('%f\n'%odom_xy.y)
            #Se cierra 
            archive_y.close()
                                                        
            #Para la orientación 
            archive_z = open('z.txt',"a")
            #Para grabar los datos se utiliza .write()
            archive_z.write('%f\n'%yaw)
            #Se cierra 
            archive_z.close()
            
#################################################################################################


#Inicializa el nodo y lo crea
rospy.init_node('node_general')

#Crea una variable de tipo Twist()
vel_bot = Twist()
#Se crea el objeto publicador 
pub_vel = rospy.Publisher('cmd_vel',Twist,queue_size=1)
#Pregunta por los valores de velocidades 
print('Hola usuario, ingrese los siguientes datos ')
vel_bot.linear.x = float(input('Ingrese la velocidad lineal: '))
vel_bot.angular.z = float(input('Ingrese la velocidad angular: '))

#Se crea el objeto suscriptor
sub_odm = rospy.Subscriber('odom',Odometry,callback)
#Se crea el objeto publicador
pub_xy = rospy.Publisher('odom_xy', Vector3, queue_size=1)
#Se publica el mensaje 
pub_vel.publish(vel_bot)    
#Espera a que se publique y se reciba el mensaje  
rospy.spin()
     
