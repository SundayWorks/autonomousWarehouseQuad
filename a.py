import RPi.GPIO as g
import time
import pigpio

#GPIO mode
g.setmode(g.BOARD)

#set GPIO pins
trig1=18
#trig2=21
#trig3=23
#trig4=29
#trig5=32
echo1=19
#echo2=22
#echo3=26
#echo4=31
#echo5=35

#set GPIO direction
g.setup(trig1,g.OUT)
g.setup(echo1,g.IN)
#g.setup(trig2,g.OUT)
#g.setup(echo2,g.IN)
#g.setup(trig3,g.OUT)
#g.setup(echo3,g.IN)
#g.setup(trig4,g.OUT)
#g.setup(echo4,g.IN)
#g.setup(trig5,g.OUT)
#g.setup(echo5,g.IN)

def distance():
    #set Trigger to HIGH
    g.output(trig1, True)
    #g.output(trig2, True)
    #g.output(trig3, True)
    #g.output(trig4, True)
    #g.output(trig5, True)
    
    #set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    g.output(trig1, False)
    #g.output(trig2, False)
    #g.output(trig3, False)
    #g.output(trig4, False)
    #g.output(trig5, False)
    
    StartTime = time.time()
    StopTime = time.time()
 
    #Start Time
    while g.input(echo1)==0:
        st1 = time.time()
    #while g.input(echo2)==0:
       # st2 = time.time()
 
    #time of arrival
    while g.input(echo1)==1:
        at1 = time.time()
    #while g.input(echo2)==1:
        #at2 = time.time()
        
    #time elapsed
    te1=st1-at1
    #te2-st2-at2
    
    #sonic speed (34300 cm/s)
    d1 = (te1 * 34300) / 2
    #d2 = (te2 * 34300) / 2
    
    return d1
    #return d2
 
if __name__ == '__main__':
    try:
        while True:
            dist1 = distance()
            print ("MD1 = %.1f cm" % dist1)
            time.sleep(1)
            #print ("MD2 = %.1f cm" % dist2)
            #time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("stop")
        g.cleanup()






































































