import re
from math import floor

import os

if __name__ == "__main__":
    # count = 1
    # for i in range(100):
    #     os.system("cls")
    #     print("."*count)
    #     count += 1    
    # exit()
    deers = []
    with open("test.file14", "r") as f:
        parser = re.compile(r'(\w+).*\s(\d+)\skm/s.*for\s(\d+)\sseconds.*for\s(\d+)\sseconds.*')
        for line in f:
            res = parser.match(line)
            if res:
                name = res.group(1)
                speed = int(res.group(2))
                flyTime = int(res.group(3))
                restTime = int(res.group(4))
                deers.append((name, speed, flyTime, restTime))
        time = 2503
        distance = None
        winner = None        
        #14-1            
        # for deer in deers:
        #     (name, speed, flyTime, restTime) = deer
        #     travelDist = speed*flyTime
        #     i = floor(time/(flyTime+restTime))
        #     print(i)
        #     tempDistance = i * travelDist
        #     print(tempDistance)
        #     travelTimeLeft = time - (i * (flyTime+restTime))
        #     print(travelTimeLeft)
                        
        #     if travelTimeLeft >= 0:
        #         if travelTimeLeft > flyTime:
        #             travelTimeLeft = flyTime                
        #         tempDistance += speed*travelTimeLeft
                        
        #     print(name, tempDistance)
        #     if distance == None:
        #         distance = tempDistance
        #         winner = name 
        #     else:
        #         if distance < tempDistance:
        #             distance = tempDistance
        #             winner = name
        #print ("Winner is {} with distance of {}".format(winner, distance))
        
        #14-2
        deerScores = dict()
        for deer in deers:
            deerScores[deer[0]] = 0
        deerDistances = dict()
        for seconds in range(1, time):
            for deer in deers:
                (name, speed, flyTime, restTime) = deer
                travelDist = speed*flyTime
                i = floor(seconds/(flyTime+restTime))
                #print(i)
                tempDistance = i * travelDist
                #print(tempDistance)
                travelTimeLeft = seconds - (i * (flyTime+restTime))
                #print(travelTimeLeft)
                            
                if travelTimeLeft >= 0:
                    if travelTimeLeft > flyTime:
                        travelTimeLeft = flyTime                
                    tempDistance += speed*travelTimeLeft
                            
                #print(name, tempDistance)
                deerDistances[deer[0]] = tempDistance
            maxDistance = None
            deerLeaders = []
            for deer, dist in deerDistances.items():
                if maxDistance != None:
                    if maxDistance < dist:
                        maxDistance = dist
                        deerLeaders = [deer]
                    elif maxDistance == dist:
                        deerLeaders.append(deer)                    
                else:
                    maxDistance = dist
                    deerLeaders = [deer]
                    
            for deer in deerLeaders:
                deerScores[deer] = deerScores[deer] + 1                
        
        maxScoreDeer = max(deerScores, key=deerScores.get)
        print("{} has max score {}".format(maxScoreDeer, deerScores[maxScoreDeer]))
        
                
                
                
        
