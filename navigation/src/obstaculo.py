#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from costmap_2d.costmap_2d_ros import Costmap2DROS
from costmap_2d.costmap_2d_publisher import Costmap2DPublisher
from tf import TransformListener
import numpy as np

def add_static_obstacle(costmap, x, y, radius, cost):
    mx, my = costmap.world_to_map(x, y)

    for i in range(-radius, radius + 1):
        for j in range(-radius, radius + 1):
            if np.sqrt(i**2 + j**2) <= radius:
                cx = mx + i
                cy = my + j
                costmap.set_cost(cx, cy, cost)

def main():
    rospy.init_node('static_obstacle_node')

    x = rospy.get_param('~x', 5.0)  # Coordenada X del centro del obstáculo
    y = rospy.get_param('~y', 5.0)  # Coordenada Y del centro del obstáculo
    radius = rospy.get_param('~radius', 1)  # Radio del obstáculo en metros
    cost = rospy.get_param('~cost', 254)  # Coste del obstáculo, 254 es considerado casi letal (como un muro)

    tf_listener = TransformListener()
    costmap_ros = Costmap2DROS("my_costmap", tf_listener)

    rospy.sleep(1)  # Espera a que los nodos ROS estén listos

    costmap = costmap_ros.getCostmap()

    add_static_obstacle(costmap, x, y, radius, cost)

    costmap_publisher = Costmap2DPublisher(costmap)
    costmap_publisher.publishCostmap()

    rospy.spin()

if __name__ == '__main__':
    main()
