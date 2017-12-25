import RPi.GPIO as g
import time

#GPIO mode
g.setmode(g.BOARD)
g.setwarnings(False)
#set GPIO pins
trig1=18
trig2=21
trig3=23
trig4=26
trig5=31
echo1=19
echo2=22
echo3=24
echo4=29
echo5=32

#set GPIO direction
g.setup(trig1,g.OUT)
g.setup(echo1,g.IN)
g.setup(trig2,g.OUT)
g.setup(echo2,g.IN)
g.setup(trig3,g.OUT)
g.setup(echo3,g.IN)
g.setup(trig4,g.OUT)
g.setup(echo4,g.IN)
g.setup(trig5,g.OUT)
g.setup(echo5,g.IN)

def distance():
    #set Trigger to HIGH
    g.output(trig1, True)
    g.output(trig2, True)
    g.output(trig3, True)
    g.output(trig4, True)
    g.output(trig5, True)
    st5,st4,st3,st2,st1,at1,at2,at3,at4,at5 = 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0;

    #set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    g.output(trig1, False)
    g.output(trig2, False)
    g.output(trig3, False)
    g.output(trig4, False)
    g.output(trig5, False)

    #Start Time
    while g.input(echo1)==0:
        st1 = time.time()
    while g.input(echo2)==0:
        st2 = time.time()
    while g.input(echo3)==0:
        st3 = time.time()
    while g.input(echo4)==0:
        st4 = time.time()
    while g.input(echo5)==0:
        st5 = time.time()
        
 
    #time of arrival
    while g.input(echo1)==1:
        at1 = time.time()
    while g.input(echo2)==1:
        at2 = time.time()
    while g.input(echo3)==1:
        at3 = time.time()
    while g.input(echo4)==1:
        at4 = time.time()
    while g.input(echo5)==1:
        at5 = time.time()
        
    #time elapsed
    t1=st1-at1
    t2=st2-at2
    t3=st3-at3
    t4=st4-at4
    t5=st5-at5
  
    #sonic speed (34300 cm/s)
    d1 = (t1 * 34300) / 2
    d2 = (t2 * 34300) / 2
    d3 = (t3 * 34300) / 2
    d4 = (t4 * 34300) / 2
    d5 = (t5 * 34300) / 2
    
    
    #print(d1,"a",d2,"b",d3,"e",d4,"f",d5)
    print(d1)
    
 
if __name__ == '__main__':
    try:
        while True:
            #[dist1,dist2] = distance()
            #print ("MD1 = %.1f cm" % dist1)
            #time.sleep(1)
            #print ("MD2 = %.1f cm" % dist2)
            #time.sleep(1)
             distance()
             
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("stop")
        g.cleanup()





































































