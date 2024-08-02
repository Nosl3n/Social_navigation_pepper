#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from naoqi import ALProxy

def get_hand_actuator_positions():
    ip = "192.168.31.23"  # Dirección IP de tu robot Pepper
    port = 9559

    # Conectar con el módulo ALMotion
    motion_proxy = ALProxy("ALMotion", ip, port)

    # Nombres de los actuadores del brazo derecho y la mano
    names = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]

    # Obtener los ángulos actuales de los actuadores
    angles = motion_proxy.getAngles(names, True)

    # Imprimir los ángulos actuales
    for name, angle in zip(names, angles):
        print("{}: {:.2f} radianes".format(name, angle))

if __name__ == "__main__":
    rospy.init_node('pepper_get_hand_actuator_positions')
    get_hand_actuator_positions()
