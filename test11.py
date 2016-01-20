import array
import re
from common import debug
from datetime import datetime
startTime = datetime.now()

#do something


SMALL_A_CODE = list(b'a')[0]
SMALL_Z_CODE = list(b'z')[0]
SMALL_I_CODE = list(b'i')[0]
SMALL_O_CODE = list(b'o')[0]
SMALL_L_CODE = list(b'l')[0]
#BIG_A_CODE = list(b'A')[0]
#BIG_Z_CODE = list(b'Z')[0]
#print(SMALL_A_CODE, SMALL_Z_CODE, BIG_A_CODE, BIG_Z_CODE)
def modifyBytesWord(bWord):
    newWord = bWord
    word = bWord.decode()
    wordLen = len(word)
    res1 = word.find('i')
    res2 = word.find('l')
    res3 = word.find('o')
    
    resList = []
    for x in [res1,res2,res3]:
        if x != -1:        
            resList.append(x)
    if len(resList):    
        minRes = min(resList)
        if minRes == res1:
            res = res1
            charCode = SMALL_I_CODE
        elif minRes == res2:
            res = res2
            charCode = SMALL_L_CODE
        elif minRes == res3:
            res = res3
            charCode = SMALL_O_CODE                
                
        
        if res != -1:
            newWord = bWord[:res] + bytes(bytearray([charCode + 1])) + bytes(bytearray([SMALL_A_CODE]*(wordLen-res-1)))                    
    return newWord

def incrementBytesWord(word):
    result = True
    #lastChar = word[len(word)-1]
    newWord = b''
    incremented = False    
    insertedChars = 0
    for i in range(len(word) - 1, -1, -1):
        char = word[i]
        #print("Char is {}".format(char))
        insertedChars += 1        
        if char == SMALL_Z_CODE:
            #newWord.insert(0, SMALL_A_CODE)
            newWord = bytes(bytearray([SMALL_A_CODE])) + newWord                
        else:
            #newWord.insert(0, char + 1)
            newWord = bytes(bytearray([char + 1])) + newWord
            incremented = True            
            break        
    #print(newWord)        
    if not incremented:
        #means we reached end
        result = False
    else:
        result = word[:len(word)-insertedChars] + newWord#array.array('B', newWord).tostring()
        #result = array.array('B', newWord).tostring()                            
        
    return result                                                    

test2 = re.compile(r'^(?:(?!i|o|l).)*$') #Not contains i, o, l
test3 = re.compile(r'\w*(\w)\1\w*(\w)\2\w*') #Two different non-overlapping pairs


def checkBytesPassword(bWord):
    isGood = False
        
    #print(word)
    # res = test2.match(word)
    # if res:
    #     debug("test2 pass")
    word = bWord.decode()        
    if not 'i' in word and not 'l' in word and not 'o' in word:
        prevChar = bWord[0]
        counter = 0
        straightChars = 1        
                    
        
        res = test3.match(word)
        if res:
            debug("test3 pass")
            for char in bWord:                
                if counter > 0:
                    if char == (prevChar + 1):
                        straightChars += 1
                    else:
                        straightChars = 1                
                if straightChars == 3:
                    isGood = True
                    debug("test1 pass")
                    break
                prevChar = char
                counter += 1
                
    return isGood

#11-1    
#word = b'hxbxwxba'
#11-2
word = incrementBytesWord(b'hxbxxyzz')

#word = b'ghijklmn'

count = 0
while word:
    word = modifyBytesWord(word)
    if checkBytesPassword(word):
        print("Found {}".format(word.decode()))  
        break       
    word = incrementBytesWord(word)
    # if not count % 1000:
    #     print(word.decode())
    count += 1

print("Finished for {}".format(datetime.now() - startTime))