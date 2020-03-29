import rospy
from package_robot.srv import SumaTwoInts
def add_two_ints_client(x,y):
	rospy.wait_for_service('suma_two_ints')
	try:
		#Definimos el servicio cliente en la variable add_two_ints_
		#name service|clase servicio
		add_two_ints = rospy.ServiceProxy('suma_two_ints', SumaTwoInts)
		resp = add_two_ints(x, y)
		return resp.sum
	except rospy.ServiceException as e :
	print("service call failed: %s"%e)

def nodo ():
	rospy.init_node('nodo_suma_two_ints_client')
	#definimos dos variables x & y para realizar la suma de  los dos enteros
	x = 7
	y = 8
	print("Requesting %s+%s"%(x, y))
	#Imprimimos el resultado de a operacion de los dos enteros
	print("%s + %s = %s" %(x, y, add_two_ints_client(x, y)))
if __name__ == '__main__':
	try:
		nodo()
	except rospy.ROSInterruptException:
		pass
