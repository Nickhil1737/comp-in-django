import random
import time
from collections import Counter


#import the file containing algorithm here



def findcompx(result):
    complexity_dict = {"1":'lgn', "2":'n', "3":'nlgn', "4":'n^2', "5":'n^2lgn', "6":'n^2lgn',"7":'n^3',"8":'n^3', "10":'exponential'}
    last_time = 1
    sizeorder = 2**20
    list2nbyn = []
    timetakenlist = []
    for i in range(1, 21):
        arr = [random.randrange(-100000,100000) for i in range(2**i)]
        
        start_time = time.time()
        result(arr)
        time_taken = time.time()-start_time
        timetakenlist.append(time_taken)
        time2nbyn = time_taken/last_time
        list2nbyn.append(round(time2nbyn))

        #print(str(2**i)+ "   " + str(time_taken))
        if time_taken > 1:
            sizeorder = 2**i
            break
        last_time = time_taken
    stepDict = Counter(list2nbyn)
    steps = 1
    stepsval = 0
    for k, v in stepDict.items():
        if v >= stepsval:
            steps = k
            stepsval = v
    
    if steps == 2 and sizeorder < 1000000:
        steps += 1
    if steps > 8:
        return "exponential"
    return timetakenlist[-3:],str(steps)

# driver code

# Tuesday 29 December 2020 03:45:24 PM IST
            # astrainL3gi0N
