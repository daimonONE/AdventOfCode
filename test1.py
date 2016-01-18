#1
with open('test.file1', 'r') as f:
    floor = 0   
    pos = 1  
    for line in f:
        for char in line:
            if char == '(':
                floor += 1
            else:
                floor -= 1
            if floor == -1:
                break
            pos += 1                         
    print("Elevator is at {} floor".format(pos))