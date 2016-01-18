#4
import hashlib

testString = b"iwrupvqb"
#testString = b"abcdef"
 
#4-1
startValue = "0"*5
#4-2
#startValue = "0"*6
    
counter = 0
result = ""
while(True):
    m = hashlib.md5()
    m.update(testString + str(counter).encode())    
    hex = m.hexdigest()
                          
    if hex.startswith(startValue):
        result = hex
        break
    counter += 1
print(result)
print(counter)    


