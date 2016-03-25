import re
import time

start_time = time.time()


#results = set()
#replacements = []
#with open('test.file19', 'r') as f:
#    parser = re.compile(r'(\w+)\s=>\s(\w+)')            
#    for line in f:
#        res = parser.match(line)
#        if res:
#            replacements.append( (res.group(1), res.group(2)) )        
#        else:
#            startString = line
                           
#if not startString:
#    print("File Not Read Properly -> Start String is Empty")
#    exit(1)
    
#if not len(replacements):
#    print("File Not Read Properly -> Replacements List is Empty")
#    exit(1)
        
## Test
## startString = 'HOH'
## replacements = [('H', 'HO'), ('H', 'OH'), ('O', 'HH')]

#for pair in replacements:
#    index = 0    
#    while index != -1:
#        index = startString.find(pair[0], index)
#        if index != -1:    
#            resString = startString[0:index] + startString[index:].replace(pair[0], pair[1], 1)
#            results.add(resString)
#            #print(resString)        
#            index += 1
        
#print(len(results))    


#Part 2

startList = [startString]
endString = 'e'
replacements = []
with open('test.file19', 'r') as f:
    parser = re.compile(r'(\w+)\s=>\s(\w+)')            
    for line in f:
        res = parser.match(line)
        if res:
            replacements.append( (res.group(2), res.group(1)) )        
        else:
            startString = line

replacements.sort(key=lambda x: len(x[0]), reverse=True)
print(replacements)

found = False
iteration = 0
repIndex = 0        
while not found and iteration < 1000:
    if repIndex >= len(replacements):
        break        
    pair = replacements[repIndex]
    index = 0    
    while index != -1:
        index = startString.find(pair[0], index)
        if index != -1:    
            startString = startString.replace(pair[0], pair[1], 1)
            print(startString)            
            iteration += 1
            repIndex = 0
            index = 0
            if startString == endString:
                found = True
        else:
            repIndex += 1
                        
if found:    
    print("Found item on {} iteration".format(iteration))
else:
    print("NOT Found item")
print("--- %s seconds ---" % (time.time() - start_time))    
        
        
        