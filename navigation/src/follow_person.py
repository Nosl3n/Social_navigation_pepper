#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState
from naoqi import ALProxy
ip = "192.168.31.23"  # Dirección IP de tu robot Pepper
port = 9559
posture_proxy = ALProxy("ALRobotPosture", ip, port)
# Variables globales para almacenar la orientación de la cabeza
head_yaw = 0.0
head_pitch = 0.0
posture_proxy.goToPosture("StandInit", 0.5)
def person_position_callback(pos_msg):
    global head_yaw, head_pitch

    # Obtener las coordenadas de la persona
    x = pos_msg.linear.x
    y = pos_msg.linear.y

    # Crear un mensaje de velocidad
    cmd_vel = Twist()

    # Control simple: mover el robot hacia la persona
    if y < 320:  # La persona está a la izquierda
        cmd_vel.angular.z = 0.1
    elif x > 320:  # La persona está a la derecha
        cmd_vel.angular.z = -0.1

    if y < 240:  # La persona está arriba
        cmd_vel.linear.x = 0.4
    elif x > 240:  # La persona está abajo
        cmd_vel.linear.x = -0.1

    # Publicar el comando de velocidad
    cmd_pub.publish(cmd_vel)

def head_position_callback(joint_state):
    global head_yaw, head_pitch
    # Actualizar las variables globales con la posición actual de la cabeza
    head_yaw = joint_state.position[joint_state.name.index('HeadYaw')]
    head_pitch = joint_state.position[joint_state.name.index('HeadPitch')]

if __name__ == '__main__':
    rospy.init_node('follow_person_node', anonymous=True)
    rospy.Subscriber('/person_position', Twist, person_position_callback)
    rospy.Subscriber('/pepper_robot/pose/joint_states', JointState, head_position_callback)
    cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    rospy.loginfo("Nodo de seguimiento de personas iniciado.")
    rospy.spin()
