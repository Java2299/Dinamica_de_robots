#!/usr/bin/env python 
# encoding: utf-8
import rospy
from std_msgs.msg import String 
def nodo (): 
	rospy.init_node('node_publisher')
	pub = rospy.Publisher('example',String, queue_size=10)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		mensaje = "Nodo Publisher"
		rospy.loginfo(mensaje)
		pub.publish(mensaje)
		rate.sleep()
if __name__ == '__main__':
	try:
		nodo()
	except rospy.ROSInterrupException:
		pass
