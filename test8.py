import re

def getRealLength(line):
    #rm quotes
        
    print ( line )    
    realLen = 0
    
    #8-1
    #replace unneeded patterns with exactly 1 symbol
    line = line[1:len(line)-1]
    line = re.sub(r'((\\x[0-9a-f]{2})|(\\\\)|(\\"))',
        '!',
        line)
    #8-2
    #backlashing string                    
    # line = re.sub(r'(?<=\\)(.)',
    #     r'\\\1',
    #     line)
    #backlashing quotes    
    # line = re.sub(r'"',
    #     r'\"',
    #     line)      
    # line = '"' + line[:len(line)-1] + '\""'
    print ( "Res " + line + " " + str(len(line)) )
    
    return len(line)


with open('test.file8', 'r') as f:
    realLens = 0
    lens = 0
    testStrs = [r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"']
    for line in f:       
        line = line.strip()     
        realLens += getRealLength(line)
        #print ( line )
        #rint ( len(line) )
        lens += len(line)
        
    
    print("Lengths: {}".format(lens))
    print("Real Lengths: {}".format(realLens))    
    print("Lengths minus Real Lengths: {}".format(realLens - lens))        
        
    