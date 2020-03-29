#!/usr/bin/env python 
# encoding: utf-8

import rospy

def nodo (): 
	rospy.init_node('node1')
	mensaje="Hola mundo"
	rospy.loginfo(mensaje)
if __name__ == '__main__':
	try:
		nodo()
	except rospy.ROSInterrupException:
		pass
