#this code is for autonomous control, need to modify it for our purpose

import numpy as np
from RPIO import PWM
import time

# initialize servo objects with PWM function
roll = PWM.Servo()
pitch = PWM.Servo()
throttle = PWM.Servo()
yaw = PWM.Servo()

# start PWM on servo specific GPIO no,GPIO no is used not pin no
roll.set_servo(5,1520)# pin 29
pitch.set_servo(6,1520)# pin 31
throttle.set_servo(13,1100)# pin 33
yaw.set_servo(19,1520)# pin 35
#pin 39 is Ground

# assigning global min and max values
th_min = 1100
th_max = 2400
r_min = 1100
r_max = 1900
p_min = 1100
p_max = 1900
y_min = 1100
y_max = 1900
th = 1100
r = 1520
p = 1520
y = 1520
th1 = 0

if(                        )#ON is pressed in the app
          
            #to ARM the Quad
            th = 1100
            throttle.set_servo(13,th)
            time.sleep(1)
            yaw.set_servo(19,1100)
            time.sleep(1)
            yaw.set_servo(19,1550)
            time.sleep(1)
            print 'System is armed'


                        # UP
                            th = th + 10
                            if (th < th_min):
                                throttle.set_servo(13,1100)
                                th = 1100
                            elif (th > th_max):
                                throttle.set_servo(13,2400)
                                th = 2400
                            elif (th > th_min & th < th_max):
                                throttle.set_servo(13,th)
                            continue

                        # DOWN
                            th = th - 10
                            if (th < th_min):
                                throttle.set_servo(13,1100)
                                th = 1100
                            elif (th > th_max):
                                throttle.set_servo(13,2400)
                                th = 2400
                            elif (th > th_min & th < th_max):
                                throttle.set_servo(13,th)
                            continue

                        # Yaw LEFT
                            y = y - 10
                            if (y < y_min):
                                yaw.set_servo(19,1100)
                                y = 1100
                            elif (y > y_max):
                                yaw.set_servo(19,1900)
                                y = 1900
                            elif (y > y_min & y < y_max):
                                yaw.set_servo(19,y)
                            continue

                        # Yaw RIGHT
                            y = y + 10
                            if (y < y_min):
                                yaw.set_servo(19,1100)
                                y = 1100
                            elif (y > y_max):
                                yaw.set_servo(19,1900)
                                y = 1900
                            elif (y > y_min & y < y_max):
                                yaw.set_servo(19,y)
                            continue

                        # Forward
                            p = p + 10
                            if (p < p_min):
                                pitch.set_servo(6,1100)
                                p = 1100
                            elif (p > p_max):
                                pitch.set_servo(6,1900)
                                p = 1900
                            elif (p > p_min & p < p_max):
                                pitch.set_servo(6,p)
                            continue
            
                        # Backward
                            p = p - 10
                            if (p < p_min):
                                pitch.set_servo(6,1100)
                                p = 1100
                            elif (p > p_max):
                                pitch.set_servo(6,1900)
                                p = 1900
                            elif (p > p_min & p < p_max):
                                pitch.set_servo(6,p)
                            continue

                        # Roll LEFT
                            r = r - 10
                            if (r < r_min):
                                roll.set_servo(5,1100)
                                r = 1100
                            elif (r > r_max):
                                roll.set_servo(5,1900)
                                r = 1900
                            elif (r > r_min & r < r_max):
                                roll.set_servo(5,r)
                            continue

                        # Roll RIGHT
                            r = r + 10
                            if (r < r_min):
                                roll.set_servo(5,1100)
                                r = 1100
                            elif (r > r_max):
                                roll.set_servo(5,1900)
                                r = 1900
                            elif (r > r_min & r < r_max):
                                roll.set_servo(5,r)
                            continue

                        # Stable
                                throttle.set_servo(13,th)
                            else:
                                pass
                            if r != 1520:
                                roll.set_servo(5,1520)
                            else:
                                pass
                            if p !=1520:
                                pitch.set_servo(6,1520)
                            else:
                                pass
                            if y != 1520:
                                yaw.set_servo(19,1520)
                            else:
                                pass
                            th1 = th
                            print 'STABLE'
                            continue
                            
if(                        )#OFF is pressed in the app
         
        # land
            throttle.set_servo(13,th-10)
            time.sleep(10)
            print 'landed'
            
        # Disarm
            throttle.set_servo(13,1100)
            time.sleep(1)
            yaw.set_servo(19,1900)
            time.sleep(1)
            yaw.set_servo(19,1520)
            time.sleep(1)
            print 'System is disarmed'

        time.sleep(0.1)

roll.stop_servo(5)
pitch.stop_servo(6)
throttle.stop_servo(13)
yaw.stop_servo(19)
aux.stop_servo(26)                  