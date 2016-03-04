
import copy


rows = 100
columns = 100

lights = [[0 for x in range(columns)] for x in range(rows)]  

def getPointNextState(row, column, lightsBackup):
    #print("Row {}, Column {}".format(row, column))
    points = []
    nextColumn = column + 1
    prevColumn = column - 1
    
    nextColumnGood = nextColumn < columns
    prevColumnGood = prevColumn >= 0
    
    nextRow = row + 1
    prevRow = row - 1
    
    if nextRow < rows:
        if nextColumnGood:
            points.append( (nextRow, nextColumn) )
        if prevColumnGood:
            points.append( (nextRow, prevColumn) )
        points.append( (nextRow, column) )
    if prevRow >= 0:
        if nextColumnGood:
            points.append( (prevRow, nextColumn) )
        if prevColumnGood:
            points.append( (prevRow, prevColumn) )
        points.append( (prevRow, column) )  
        
    if nextColumnGood:
        points.append( (row, nextColumn) )
    if prevColumnGood:
        points.append( (row, prevColumn) )
    points.sort()
    #print(points)
    #print(lightsBackup)
    prevPointState = lightsBackup[row][column]    
    nextPointState = 0
    onCounter = 0
    for point in points:
        #print(lightsBackup[point[0]][point[1]])
        if lightsBackup[point[0]][point[1]]:
            onCounter += 1
    if prevPointState:
        if onCounter == 2 or onCounter == 3:
            nextPointState = 1
    else:
        if onCounter == 3:
            nextPointState = 1
    #print("PrevState was {},onCounter {}, nextState {}".format(prevPointState, onCounter, nextPointState))
    
    return nextPointState
    
    
def toggle():   
    #print("Toggle") 
    lightsBackup = copy.deepcopy(lights)    
    #print(lightsBackup)
    for i in range(0, rows):    
         for j in range(0, columns):
            if not isCorner(i, j):
                lights[i][j] = getPointNextState(i, j, lightsBackup)
            #print(lights[i][j])

def isCorner(row, column):
    if row == 0 and column == 0 or row == 0 and column == columns - 1 or row == rows - 1 and column == 0 or row == rows - 1 and column == columns - 1:
        return True
    return False
    
with open('test.file18', 'r') as f:
    i = 0
    j = 0
    for line in f:
        j = 0
        for char in line:    
            if char == '#':
                lights[i][j] = 1            
            j += 1
        i += 1   
    lights[0][0] = 1
    lights[0][columns - 1] = 1
    lights[rows - 1][0] = 1
    lights[rows - 1][columns - 1] = 1
        
    count = 100
    while count:
        toggle()
        count -= 1
        #print (lights)    
    litCount = 0            
    for i in range(0, rows):
        for j in range(0, columns):
            if lights[i][j]:
                litCount += lights[i][j]            
            
    print (litCount) 
                                               
    