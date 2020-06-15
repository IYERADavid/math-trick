import os
import time


seconds=float(0)
minutes=int(0)
hours=int(0)

run =raw_input('enter R to run program:')

while run.lower() =='r':
    
    if seconds >59:
        seconds=0
        minutes +=1
    if minutes >59:
        minutes=0
        hours +=1    
    seconds =(seconds + .1)
    print(hours,':',minutes,':',seconds)
    time.sleep(0.1)    