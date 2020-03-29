# encoding: utf -8

import rospy
import actionlib
from package_robot.msg import DoCarWashAction, DoCarWashFeedback, DoCarWashResult
class DoActionServer:
	def __init__(self):
		self.server = actionlib.SimpleActionServer('do_wash_car', DoCarWashAction, self.excute, False) #Declaramos nuestra accion server con nombre do_wash_car
		self.server.start()
		print("Running action server do_wash_car ...")
	def excute(self, goal):
		feedback = DoCarWashFeedback()
		result = DoCarWashResult()
		rate = rospy.Rate(1)
		for x in range (0,goal.number_of_cars):
			result.total_cars_cleaned += 1
			feedback.percent_cars_complete = (result.total_cars_cleaned*100.0)/goal.
			number_of_cars
			self.server.publish_feedback(feedback)
			rate.sleep()
		self.server.set_succeeded(result)
if __name__ == '__main__':
	rospy.init_node('nodo_action_server')
	server = DoActionServer()
	rospy.spin()
	
