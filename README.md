
ขั้นตอนการติดตั้ง Arduino IDE บน Ubuntu
  $sudo apt-get update
  $ sudo apt-get upgrade
  $ mkdir arduino
  $ cd arduino/
  $ wget https://downloads.arduino.cc/arduino-1.8.15-linux64.tar.xz
  $ tar -xvf ./arduino-1.8.15-linux64.tar.xz
  $ cd arduino-1.8.15/
  $ sudo ./install.sh

ขั้นตอนการติดตั้ง CH340 บน Ubuntu
  $ mkdir CH340_Source
  $ cd CH340_Source
  $ git clone https://github.com/juliagoda/CH341SER.git
  $ cd CH341SER
  $ make clean
  $ make
  $ sudo make load
  $ sudo rmmod ch341 (เพื่อขจัดไดร์ฟเวอร์เก่า อาจเกิด Error หากไม่พบไดร์ฟเวอร์เก่า)
  $ lsmod | grep ch34 (แสดงไดร์ฟเวอร์ที่ถูกติดตั้งใหม่แล้ว)
  $ dmesg (ทดสอบการ detect ด้วยการ  ถอดสาย และ เสียสาย )
  




















ชัชรินทร์  เลิศยศบดินทร์
Chacharin Lertyosbordin
chaightlert@gmail.com
# ROS-Tkinter-Arduino
Try to create software GUI with Tkinter and also connect with Arduino

VDO-Show case
Button-Publisher ==> https://youtu.be/OZNDReMTi5E

VDO-Show case
Scale-Publisher ==> https://youtu.be/hUTWt4uarkE

VDO-Show case
3-Scale-Control-Arm ==> https://youtu.be/KxNNupYkPYM
