#!/usr/bin/env python
# -*- coding: utf-8 -*-
from naoqi import ALProxy

ip = "192.168.31.23"  # Dirección IP de tu robot Pepper
port = 9559

# Crear una instancia de ALProxy para moverse
#motion_proxy = ALProxy("ALMotion", ip, port)
# Poner a Pepper en la posición sentada
#motion_proxy.rest()
#motion_proxy.wakeUp()
# Crear un proxy para el módulo ALAutonomousLife
autonomous_life_proxy = ALProxy("ALAutonomousLife", ip, port)

# Cambiar el estado de vida autónoma a 'solitary'
autonomous_life_proxy.setState("solitary")

print("Modo autónomo desactivado")

current_state = autonomous_life_proxy.getState()
print("Estado actual de vida autónoma:", current_state)