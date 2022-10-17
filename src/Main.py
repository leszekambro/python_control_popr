#!/usr/bin/python

from __future__ import print_function
import rospy
import math
from ardrone_autonomy.msg import Navdata
from sensor_msgs.msg import Imu
from std_msgs.msg import Float32

global ax
global ay
global az

global q 

def fax(mssg):
	global ax
	global ay
	global az
	ax = mssg.ax
	ay = mssg.ay
	az = mssg.az

def fq(mssg):
	global q
	q = mssg.angular_velocity.x
	
def main():
	global ax
	global ay
	global az
	global q
	ax = 0
	ay = 0
	az = 0
	q  = 0
	rospy.init_node('python_ardrone')
	S_a = rospy.Subscriber('/ardrone/navdata', Navdata, fax)
	S_a = rospy.Subscriber('/ardrone/imu', Imu, fq)
	P_f = rospy.Publisher("~fi", Float32, queue_size=30)
	P_t = rospy.Publisher("~teta", Float32, queue_size=30)
	delay = rospy.Rate(15)
	fi = Float32()
	teta = Float32()
	with open('plik_dane.txt', 'w') as f:
		while not rospy.is_shutdown():
			fi.data = ax
			teta.data = az
			P_f.publish(fi)
			P_t.publish(teta)
			print (q)
			print(az,file=f)
			delay.sleep()

if __name__=='__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass
