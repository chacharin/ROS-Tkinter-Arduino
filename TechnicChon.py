from tkinter import*
from pyfirmata import Arduino
import time
board = Arduino("COM5")
print("Connect Good")

#ตั้ง Pin มอเตอร์
ServoBase = board.get_pin('d:3:s')
ServoLeft = board.get_pin('d:4:s')
ServoRight = board.get_pin('d:5:s')

#ตั้งท่าเริ่มต้น
ServoBase.write(90) 
ServoLeft.write(50)
ServoRight.write(60)
print("set")

#ตั้งฟังก์ชั่นเมื่อกดปุ้ม"สั่ง"
def Click():
    global dataS1
    global dataS2 
    global dataS3
    global save_list
    #ถ้ารับค่าจากกล่องข้อความว่า save
    if E1.get()=="save":
        box = [dataS1,dataS2,dataS3]
        save_list.append(box)
        print(save_list)
     #ถ้ารับค่าจากกล่องข้อความว่า run
    elif E1.get() == 'run':
        for i in range(len(save_list)):
            #มอเตอร ์ฐาน วิ่ง
            if save_list[i][0] > Servobase.read():
                while save_list[i][0] > Servobase.read():
                    ServoBase.write(ServoBase.read()+1)
                    time.sleep(0.008)
            elif save_list[i][0] > Servobase.read():
                while save_list[i][0] > Servobase.read():
                    ServoBase.write(ServoBase.read()-1)
                    time.sleep(0.008)
            #มอเตอร์ ซ้าย วิ่ง
            if save_list[i][1] > ServoLeft.read():
                while save_list[i][1] > ServoLeft.read():
                    ServoLeft.write(ServoLeft.read()+1)
                    time.sleep(0.008)
            elif save_list[i][1] < ServoLeft.read():
                while save_list[i][1] < ServoLeft.read():
                    ServoLeft.write(ServoLeft.read()-1)
                    time.sleep(0.008)
            #มอเตอร์ ขวา วิ่ง
            if save_list[i][2] > ServoRight.read():
                while save_list[i][2] > ServoRight.read():
                    ServoRight.write(ServoRight.read()+1)
                    time.sleep(0.008)
            elif save_list[i][1] < ServoRight.read():
                while save_list[i][1] < ServoRight.read():
                    ServoRight.write(ServoRight.read()-1)
                    time.sleep(0.008)
        #ถ้าคำสั่งไม่เข้าเงื่อนไข
        else:
            print("error")

#ตั้งฟังก์ชั่นรับค่าจากแถบเลื่อน 1 >>> มอเตอร์ ฐาน
def SS1(val):
    global dataS1
    dataS1 = S1.get()
    ServoBase.write(dataS1)
#ตั้งฟังก์ชั่นรับค่าจากแถบเลื่อน 2 >>> มอเตอร์ ซ้าย
def SS2(val):
    global dataS2
    dataS2 = S2.get()
    ServoLeft.write(dataS2)
#ตั้งฟังก์ชั่นรับค่าจากแถบเลื่อน 3 >>> มอเตอร์ ขวา
def SS3(val):
    global dataS3
    dataS3 = S3.get()
    ServoRIght.write(dataS3)

#ตั้งค่ากรอบหน้าต่าง
root_window = Tk()
root_window.geometry("400x400")
root_window.title("Test-Software")

#สร้างปุ่มกด
B1 = Button(root_window,text="สั่ง", width = 10, fg="blue",command=Click)
B1.place(x=250,y=324)
B2 = Button(root_window,text="ปิดโปรแกรม", width = 30, fg="red",command=root_window.destroy)
B2.place(x=65,y=360)

#สร้างช่องกรอก
E1=Entry(root_window,width = 15)
E1.place(x=95,y=320)

#สร้างฉลาก
L1 = Label(root_window,text = "แผนกช่างยนต์ ทีม B35-37  วิทยาลัยเทคนิคชลบุรี")
L1.place(x=58, y=10)

#สร้างแถบเลื่อน
S1 = Scale(root_window, from_=0, to=180,width=20, length=256 , command = SS1)
S1.place(x=75, y=40)
#ตั้งจุดเริ่มแถบเลื่อน 1 >>> มอเตอร์ ฐาน
S1.set(90)
S2 = Scale(root_window, from_=45, to=90,width=20, length=256 , command = SS2)
S2.place(x=125, y=40)
#ตั้งจุดเริ่มแถบเลื่อน  2 >>> มอเตอร์ ซ้าย
S2.set(50)
S3 = Scale(root_window, from_=35, to=113,width=20, length=256 , command = SS3)
S3.place(x=175, y=40)
#ตั้งจุดเริ่มแถบเลื่อน  3 >>> มอเตอร์ ขวา 
S3.set(60)


#สั่งให้แสดงหน้าจอไปเรื่อยๆ
root_window.mainloop()
