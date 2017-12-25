import RPi.GPIO as g
import time

#GPIO mode
g.setmode(g.BOARD)
g.setwarnings(False)
#set GPIO pins
trig1=18
echo1=19
alt=40
#set GPIO direction
g.setup(trig1,g.OUT)
g.setup(echo1,g.IN)
def distance():
    #set Trigger to HIGH
    g.output(trig1, True)
    st1,at1 = 0.0,0.0;

    #set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    g.output(trig1, False)
    #Start Time
    while g.input(echo1)==0:
        st1 = time.time()
    #time of arrival
    while g.input(echo1)==1:
        at1 = time.time()
    #time elapsed
    t1=st1-at1
    #sonic speed (34300 cm/s)
    d1 = (t1 * 34300) / 2
 return d1
if __name__ == '__main__':
    try:
        while True:
            dist1 = distance()
            if(dist<=30)
                g.output(alt,True)
                
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("stop")
        g.cleanup()
