#3

#part2
with open('test.file3', 'r') as f:
    houses = set()
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    counter = 0
    coordinates = [[x1,y1], [x2,y2]]
    for line in f:
        for char in line:
            index = counter%2
            if char == '^':
                coordinates[counter%2][1] -= 1
            elif char == 'v':
                coordinates[counter%2][1] += 1
            elif char == '>':
                coordinates[counter%2][0] += 1
            elif char == '<':
                coordinates[counter%2][0] -= 1
            else:
                continue            
            houses.add(tuple(coordinates[counter%2]))            
            counter += 1 
    print(len(houses))