import re



rows = 1000
columns = 1000

#part2    
lights = [[0 for x in range(columns)] for x in range(rows)]  

def makeAction(value,x1,y1,x2,y2):    
    diff = 0
    if value == ACTION_TURN_ON:
        diff = 1
    elif value == ACTION_TURN_OFF:
        diff = -1
    elif value == ACTION_TOGGLE:
        diff = 2
                                    
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            lights[i][j] += diff
            if lights[i][j] < 0:
                lights[i][j] = 0


ACTION_TURN_OFF = 0
ACTION_TURN_ON = 1
ACTION_TOGGLE = 2
    
with open('test.file6', 'r') as f:
    valuesRE = re.compile(r".*?(\d+),(\d+)\sthrough\s(\d+),(\d+)")
    for line in f:    
        if line.startswith("turn on"):
            action = ACTION_TURN_ON
        elif line.startswith("turn off"):
            action = ACTION_TURN_OFF
        elif line.startswith("toggle"):
            action = ACTION_TOGGLE
                        
        res = valuesRE.match(line)
        if res != None:
            x1 = int(res.group(1))
            y1 = int(res.group(2))
            x2 = int(res.group(3))
            y2 = int(res.group(4))
            makeAction(action, x1, y1, x2, y2)

    litCount = 0            
    for i in range(0, rows):
        for j in range(0, columns):
            if lights[i][j]:
                litCount += lights[i][j]            
            
    print (litCount)            
    