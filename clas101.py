#import time module
import time
from playsound import playsound
seconds=int(input('enter time in no. of seconds'))
def Count_Down_Timer(seconds):
    while seconds>0:
       mins=int (seconds/60)
       secs=int(seconds%60)
       timer=f'{mins}:{secs}'
       print(timer, end='\r')
       time.sleep(1)
       seconds=seconds-1
    print('time Up')

Count_Down_Timer(seconds)
playsound('')

#while num>5:
 #   print(num)
 #   num=num-1