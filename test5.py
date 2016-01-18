import re
def lineReader(line):
    isProper = False
        
    #5-1
    #vowelCount = 0    
    # vowels = set(['a','e','i','o','u'])
    # pairExists = False
    # prevChar = False
    
    # blacklist = ['ab', 'cd', 'pq', 'xy']
    
    # isBlackedLine = False
    # for element in blacklist:
    #     if element in line:
    #         isBlackedLine = True
    #         break
                
    # if not isBlackedLine:
    #     for char in line:
    #         if vowelCount < 3 and char in vowels:
    #             vowelCount += 1
    #         if not pairExists and prevChar != False:
    #             if char == prevChar:
    #                 pairExists = True
    #         prevChar = char
                    
    #     if pairExists and vowelCount >= 3:
    #         isProper = True
            
    #5-2            
    first = re.compile(r'\w*(\w\w)\w*\1\w*')
    second = re.compile(r'\w*(\w)\w\1\w*')
    isProper = first.match(line) != None and second.match(line) != None               
    
    return isProper
    
    
properCount = 0 
with open('test.file5', 'r') as f:
    for line in f:
        if lineReader(line):
            properCount += 1

    print ("Nice strings count: {}".format(properCount))            
    