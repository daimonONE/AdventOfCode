from common import debug
#from itertools import groupby
import re

def lookAndSay(number):
    #solution 1
    # sNumber = str(number)
    # lastChar = sNumber[0]
    # currChar = sNumber[1:] + " "
    # count = 1
    # mNumber = ""
    # for char in sNumber:        
    #     if lastChar != None:
    #         debug("LastChar is {} and Char is {}".format(lastChar, char))
    #         if char != lastChar:
    #             debug("Saving")
    #             mNumber += str(count) + lastChar
    #             lastChar = char
    #             count = 1
    #         else:
    #             count += 1            
    
    #solution 2
    #mNumber = ''.join(list(str(len(list(g))) + k for k,g in groupby(number)))   
    
    #solution 3
    mNumber = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), number)
        
    return mNumber


    

if __name__ == "__main__":

    counter = 0
    startNumber = "3113322113"    
    
    number = startNumber
    #10-1
    #times = 40
    #10-2
    times = 50
    while(counter != times):
       number = lookAndSay(number)
       counter += 1
        
    print("Modified {} - {} times".format(startNumber, times))
    print("Length is {}".format(len(str(number))))    
