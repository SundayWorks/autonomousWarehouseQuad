import serial
from Adafruit_IO import Client
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

a = "                                                          0004B8CAE79"
b="10004A853FE0"
c="10004B051C42"
d="45005D36133D"
e="4500412E6A40"
f="45005CF7E608"

while True:
 string = ser.read(12)
 if(a==string):
     aio=Client("b3c88629e7aa492bb50a50d4ed6d6080")
     aio.send("rfid",1)
 if(b==string):
     aio=Client("b3c88629e7aa492bb50a50d4ed6d6080")
     aio.send("rfid",2)
 if(c==string):
     aio=Client("b3c88629e7aa492bb50a50d4ed6d6080")
     aio.send("rfid",3)
 if(d==string):
     aio=Client("b3c88629e7aa492bb50a50d4ed6d6080")
     aio.send("rfid",4)
 if(e==string):
     aio=Client("b3c88629e7aa492bb50a50d4ed6d6080")
     aio.send("rfid",5)
 if(f==string):
     aio=Client("b3c88629e7aa492bb50a50d4ed6d6080")
     aio.send("rfid",6)
 
     
 print(string)
 
 #aio=Client("b3c88629e7aa492bb50a50d4ed6d6080")
 #aio.send("rfid",4)
   
