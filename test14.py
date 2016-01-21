import re
from math import floor

if __name__ == "__main__":
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
        for deer in deers:
            (name, speed, flyTime, restTime) = deer
            travelDist = speed*flyTime
            i = floor(time/(flyTime+restTime))
            print(i)
            tempDistance = i * travelDist
            print(tempDistance)
            travelTimeLeft = time - (i * (flyTime+restTime))
            print(travelTimeLeft)
                        
            if travelTimeLeft >= 0:
                if travelTimeLeft > flyTime:
                    travelTimeLeft = flyTime                
                tempDistance += speed*travelTimeLeft
                        
            print(name, tempDistance)
            if distance == None:
                distance = tempDistance
                winner = name 
            else:
                if distance < tempDistance:
                    distance = tempDistance
                    winner = name
                
        print ("Winner is {} with distance of {}".format(winner, distance))
        
