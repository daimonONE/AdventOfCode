

def lineReader(line):
    res = False
    values = line.split('x')
    if len(values) == 3:
        length = int(values[0])
        width = int(values[1])
        height = int(values[2])
        #side1 = length*width
        #side2 = length*height
        #side3 = width*height
        #extraWrap = min([side1,side2,side3])
        #res = 2*side1 + 2*side2 + 2*side3 + extraWrap
        values = sorted([length, width, height])
        res = 2*(values[0] + values[1])
        res += length * width * height    
        
    return res

#3
# with open('test.file', 'r') as f:
#     houses = set()
#     x1 = 0
#     y1 = 0
#     x2 = 0
#     y2 = 0
#     counter = 0
#     coordinates = [[x1,y1], [x2,y2]]
#     for line in f:
#         for char in line:
#             index = counter%2
#             if char == '^':
#                 coordinates[counter%2][1] -= 1
#             elif char == 'v':
#                 coordinates[counter%2][1] += 1
#             elif char == '>':
#                 coordinates[counter%2][0] += 1
#             elif char == '<':
#                 coordinates[counter%2][0] -= 1
#             else:
#                 continue            
#             houses.add(tuple(coordinates[counter%2]))            
#             counter += 1 
#     print(len(houses))

#2
# with open('test.file', 'r') as f:
#     ribbon = 0         
#     for line in f:
#         res = lineReader(line)
#         if res != False:
#             ribbon += res
#     print(ribbon)

#1
# with open('test.file', 'r') as f:
#     floor = 0   
#     pos = 1  
#     for line in f:
#         for char in line:
#             if char == '(':
#                 floor += 1
#             else:
#                 floor -= 1
#             if floor == -1:
#                 break
#             pos += 1                         
#     print(pos)

#4
# import hashlib

# testString = b"iwrupvqb"
# #testString = b"abcdef"
 
# counter = 0
# result = ""
# while(True):
#     m = hashlib.md5()
#     m.update(testString + str(counter).encode())    
#     hex = m.hexdigest()         
#     if hex.startswith("000000"):
#         result = hex
#         break
#     counter += 1
# print(result)
# print(counter)                
