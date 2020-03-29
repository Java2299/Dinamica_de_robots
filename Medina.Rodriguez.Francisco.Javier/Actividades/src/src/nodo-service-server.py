import rospy
from package_robot.srv import SumaTwoInts, SumaTwoIntsResponse
def handle_suma_two_int(req):
	print ("returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
	return SumaTwoIntsResponse(req.a + req.b)
		
def nodo():
	rospy.init_node('nodo_suma_ints_server')
	#Declaramos nuestro serviv¿cio server
	#Name Service|clase servicio|función para procesar la data enviada por el c:
	s = rospi.Service('suma_two_ints_server')
	print("Ready to add two ints.")
	rospy.spin()

if __name__ == '__main__':
	try:
		nodo()
	except rospy.ROSInterruptException:
		pass
