import time
import sys
import random
import importlib
from . import solve

def findcompx():

    givecomp={1:"exponential",2:"n^3",3:"n^2lgn",4:"n^2",5:"nlgn",6:"nlgn",7:"n",8:"logarithmic"}
    # dictionary assign complexity where key is pow10 value

    pow10 = 0

    above1s = False
    for pow10 in range(1,6+1):

        arr=[random.randrange(-10000,10000) for x in range ((10**pow10))]
        # list arr consisting of 10^pow10 integers gets created

        start_time = time.time()

        solve.solve(arr) # result is basically filename.functonName
        
        
        timetaken = time.time()-start_time
        #print(time.time()-start_time)

        if(timetaken > 1):
            above1s = True
            break
    if above1s == False:
        if timetaken <= 0.0001:
            pow10 = 8
        else:
            pow10 = 7
    return givecomp[pow10]

findcompx()

 #        Wed 16 Sep 2020 04:33:22 PM IST 
       #        astrainL3gi0N


