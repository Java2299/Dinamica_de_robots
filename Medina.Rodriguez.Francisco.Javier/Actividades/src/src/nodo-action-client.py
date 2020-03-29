import rospy
import actionlib
from package_robot.msg import DoCarWashAction, DoCarWashGoal
def feedback_cd(msg):
	print('Feedback received ->'+str(msg)+'%')
def call_server():
	clent = actionlib.SimpleActionClient('do_wash_car', DoCarWashAction)
	clent.wait_for_server()
	goal = DoCarWashGoal()
	goal.number_of_cars = 5
	client.send_goal(goal, feedback_cb=feedback_cd)
	client.wait_for_result()
	result = client.get_result
	return result
	
if __name__ == '__main__':
	try: 
		rospy.init.node('nodo_action_client')
		result = call_server()
		print("The result is:", result)
	except rospy.ROSInterruptException :
		pass
		
