#!/usr/bin/env python3
from tkinter import*
import rospy
from std_msgs.msg import Int16

frame=Tk()
frame.geometry("200x200")

S1_value = 0
S2_value = 0
S3_value = 0


def publish():
    talker()

def talker(val):
    global S1_value
    global S2_value
    global S3_value

    pub1 = rospy.Publisher('servo_1', Int16, queue_size=10)
    pub2 = rospy.Publisher('servo_2', Int16, queue_size=10)
    pub3 = rospy.Publisher('servo_3', Int16, queue_size=10)
    rospy.init_node('GUI', anonymous=True)
    rate = rospy.Rate(100) 

    S1_value = Int16(S1.get())
    S2_value = Int16(S2.get())
    S3_value = Int16(S3.get())
    
    #data_str = "["+S1_value+","+S2_value+","+S3_value+"]"
    #rospy.loginfo(S1_value)
    pub1.publish(S1_value)
    pub2.publish(S2_value)
    pub3.publish(S3_value)
    rate.sleep()

S1= Scale(frame,from_=0,to=180,command=talker)
S1.place(x=10, y=10)
S1.set(90)

S2= Scale(frame,from_=0,to=180,command=talker)
S2.place(x=70, y=10)
S2.set(90)

S3= Scale(frame,from_=0,to=180,command=talker)
S3.place(x=130, y=10)
S3.set(90)

frame.mainloop()