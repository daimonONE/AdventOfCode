import re

def countScore(components, counts, optionsList):
    values = dict()    
                
    calories = 0
    counter = 0
    for name, component in components.items():
        count = counts[counter]
        for option in optionsList:            
            
            if option in values:
                values[option] = values[option] + (count * component[option])
            else:
                values[option] = count * component[option]
            
        calories += count * component[CALORIES]
        if calories > 500:
            break 
        counter += 1
    
    #15-2            
    if calories != 500:
        score = 0
    else:
        score = 1
        for key, value in values.items():
            if value < 0:
                score = 0
                break
            score *= values[key]
            
    return score
        
        
    
    

if __name__ == "__main__":
    components = dict()
    CAPACITY = 0
    DURABILITY = 1
    FLAVOR = 2
    TEXTURE = 3
    CALORIES = 4
    
    optionsList = [CAPACITY, DURABILITY, FLAVOR, TEXTURE]
    
        
    with open("test.file15", "r") as f:
        parser = re.compile(r'-?\d')
        parserName = re.compile(r'(\w+):.*')
        for line in f:
            res = parserName.match(line)
            if res:
                name = res.group(1)
                matches = parser.findall(line)            
                if len(matches) >= 5:
                    capacity = int(matches[CAPACITY])
                    durability = int(matches[DURABILITY])
                    flavor = int(matches[FLAVOR])
                    texture = int(matches[TEXTURE])
                    calories = int(matches[CALORIES])
                    components[name] = (capacity, durability, flavor, texture, calories)
    print(components) 
    #finding maximum
    max = 101
    maxScore = 0
    maxCounts = []
        
    #Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
    #Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
    # for a in range(max):
    #     for b in range(max - a):
    #         counts = [a,b]
    #         score = countScore(components, counts, optionsList)
    #         if maxScore < score:
    #             maxScore = score
    #             maxCounts = [a,b]
    
    
    for a in range(max):
        for b in range(max - a):
            for c in range(max - a - b):
                for d in range(max - a - b - c):
                    counts = [a,b,c,d]
                    score = countScore(components, counts, optionsList)
                    if maxScore < score:
                        maxScore = score
                        maxCounts = [a,b,c,d]             
    
    print(maxScore, maxCounts)
        
                
                
                        