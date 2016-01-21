import re
from itertools import permutations

def calculateSitting(order):
    prevHuman = order[0]
    value = 0
    for human in order[1:]:        
        value += peopleValues[(prevHuman, human)]
        prevHuman = human
    value += peopleValues[(prevHuman, order[0])]
    
    
    order.reverse()
    prevHuman = order[0]    
    for human in order[1:]:        
        value += peopleValues[(prevHuman, human)]
        prevHuman = human
    value += peopleValues[(prevHuman, order[0])] 
    return value
        


if __name__ == "__main__":    
    
    peopleValues = dict()
    people = set()
        
    with open("test.file13", "r") as f:
        happiness = None
        order = None
        parser = re.compile(r'(\w+).+\s(gain|lose)\s(\d+).*to\s(\w+)\.')        
        for line in f:            
            res = parser.match(line)
            if res:
                action = res.group(2)
                value = int(res.group(3))
                if action == 'lose':
                    value *= -1
                human1 = res.group(1)
                human2 = res.group(4)
                peopleValues[(human1, human2)] = value                                
                people.add(human1)
                people.add(human2)
        
        for human in people:
            peopleValues[human, "Me"] = 0
            peopleValues["Me", human] = 0
        people.add("Me")
        variations = list(permutations(people))
        
        for variation in variations:
            value = calculateSitting(list(variation))
            if happiness == None:
                happiness = value
                order = variation
            else:                
                if happiness < value:
                    happiness = value
                    order = variation
        print("Happiness is {} with order {}".format(happiness, order))
                
                
    
    