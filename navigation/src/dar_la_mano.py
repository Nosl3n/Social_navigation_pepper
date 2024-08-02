#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from naoqi import ALProxy

def shake_hand():
    ip = "192.168.31.23"  # Dirección IP de tu robot Pepper
    port = 9559

    # Conectar con el módulo ALMotion y ALRobotPosture
    motion_proxy = ALProxy("ALMotion", ip, port)
    posture_proxy = ALProxy("ALRobotPosture", ip, port)

    # Asegurarse de que el robot esté en la postura inicial
   # posture_proxy.goToPosture("StandInit", 0.5)

    # Habilitar la rigidez de los motores
    motion_proxy.setStiffnesses("RArm", 1.0)

    # Definir los ángulos para la posición de dar la mano
    hand_wave_angles = [
        0.48,  # shoulder pitch
        -0.1, # shoulder roll
        1.32,  # elbow yaw
        0.64,  # elbow roll
        -0.03   # wrist yaw
    ]

    # Mover el brazo a la posición de dar la mano
    names = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]
    motion_proxy.angleInterpolationWithSpeed(names, hand_wave_angles, 0.2)

    # Abrir la mano
    motion_proxy.openHand("RHand")

    rospy.sleep(1)  # Esperar 2 segundos para la acción

    # Cerrar la mano
    motion_proxy.closeHand("RHand")
    rospy.sleep(2) 
    motion_proxy.openHand("RHand")
    # Mover el brazo de regreso a la posición inicial
    motion_proxy.angleInterpolationWithSpeed(names, [1.4, 0.3, 1.0, 1.5, 0.0], 0.2)

    # Deshabilitar la rigidez de los motores
    motion_proxy.setStiffnesses("RArm", 0.0)

if __name__ == "__main__":
    rospy.init_node('pepper_shake_hand')
    shake_hand()
