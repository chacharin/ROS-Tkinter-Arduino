#!/usr/bin/env python3
from tkinter import*
import rospy
from std_msgs.msg import String

counter = 0
frame=Tk()

def publish():
    print('publish')
    talker()
 
def talker():
    global counter
    pub = rospy.Publisher('GUI_send', String, queue_size=10)
    rospy.init_node('GUI', anonymous=True)
    rate = rospy.Rate(100) # 1hz
    data_str = str(counter)
    rospy.loginfo(data_str)
    pub.publish(data_str)
    rate.sleep()
    counter=counter+1

B1=Button(frame,text="OK",command=publish)
B1.pack()

frame.mainloop()