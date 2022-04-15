#!/usr/bin/env python3
from tkinter import*
import rospy
from std_msgs.msg import String

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

    pub = rospy.Publisher('GUI_send', String, queue_size=10)
    rospy.init_node('GUI', anonymous=True)
    rate = rospy.Rate(100) # 1hz

    S1_value = str(S1.get())
    S2_value = str(S2.get())
    S3_value = str(S3.get())
    
    data_str = "["+S1_value+","+S2_value+","+S3_value+"]"

    rospy.loginfo(data_str)
    pub.publish(data_str)
    rate.sleep()

S1= Scale(frame,from_=0,to=180,command=talker)
S1.place(x=10, y=10)

S2= Scale(frame,from_=0,to=180,command=talker)
S2.place(x=70, y=10)

S3= Scale(frame,from_=0,to=180,command=talker)
S3.place(x=130, y=10)

frame.mainloop()