#2
def lineReader(line, part):
    res = False
    values = line.split('x')
    if len(values) == 3:
        length = int(values[0])
        width = int(values[1])
        height = int(values[2])
        if part == 1:
            side1 = length*width
            side2 = length*height
            side3 = width*height
            extraWrap = min([side1,side2,side3])
            res = 2*side1 + 2*side2 + 2*side3 + extraWrap
        elif part == 2:
            values = sorted([length, width, height])
            res = 2*(values[0] + values[1])
            res += length * width * height    
        
    return res

with open('test.file2', 'r') as f:
    value1 = 0
    value2 = 0         
    for line in f:
        res1 = lineReader(line, 1)
        if res1 != False:
            value1 += res1
        res2 = lineReader(line, 2)
        if res2 != False:
            value2 += res2
#2-1    
    print("Wrap needed {}".format(value1))
#2-2    
    print("Ribbon needed {}".format(value2))