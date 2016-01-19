import common  

def getShortestRoute(elements, routes):
    distance = None
    visitedOrder = None
    distances = []
    for element in elements:
        visited = set()
        visited.add(element)
        tempVisitedOrder = [element]    
        
        debug("Start element: " + element )
        currentElement = element
        
        tempDistance = 0
        while len(visited) < len(elements):
            value = None        
            currentRoute = None
            debug(visited)        
            for tempElement in elements:            
                if not tempElement in visited:
                    debug("Temp element " + tempElement)                                
                    if (currentElement, tempElement) in routes:                    
                        tempValue = routes[(currentElement, tempElement)]
                        debug("Route found {}".format((currentElement, tempElement)))                    
                    elif (tempElement, currentElement) in routes:
                        tempValue = routes[(tempElement, currentElement)]
                        debug("Route found {}".format((tempElement, currentElement)))
                    else:
                        debug("Error: no route from {} to {}".format(currentElement, tempElement))
                        continue
                    if value != None:                    
                        if tempValue < value:
                            debug("Switch route from {} {} to {} {}".format(currentRoute, value, tempElement, tempValue))
                            currentRoute = tempElement
                            value = tempValue
                    else:
                        debug("No value yet: route is now {} with value {}".format(tempElement, tempValue))
                        value = tempValue
                        currentRoute = tempElement
                    
            if value != None:
                tempDistance += value
                visited.add(currentRoute)
                tempVisitedOrder.append(currentRoute)
                currentElement = currentRoute
                debug("Visited {}".format(tempVisitedOrder))
                debug("Travel Value {}".format(tempDistance))
            else:
                debug("Wrong")
        
        distances.append(tempDistance)
                
        if distance != None:
            if tempDistance < distance:
                distance = tempDistance
                visitedOrder = tempVisitedOrder            
        else:
            distance = tempDistance
            visitedOrder = tempVisitedOrder                       
                
    return (distance, visitedOrder)

#Faerun, Norrath, Tristram, AlphaCentauri, Arbre, Snowdin, Tambi, Straylight

def getLongestRoute(elements, routes):
    perms = list(itertools.permutations(elements))
    distance = None        
    visitedOrder = None
    for permList in perms:
        tempDistance = 0
        currentElement = None
        for element in permList:
            if currentElement == None:
                currentElement = element
            else:
                if (currentElement, element) in routes:                    
                    tempDistance += routes[(currentElement, element)]
                    debug("Route found {}".format((currentElement, element)))                    
                elif (element, currentElement) in routes:
                    tempDistance += routes[(element, currentElement)]
                    debug("Route found {}".format((element, currentElement)))
            currentElement = element
        if distance == None or tempDistance > distance:
            distance = tempDistance
            visitedOrder = permList
    
    return (distance, visitedOrder)    
            
                    
            



if __name__ == "__main__":
    import re
    import itertools
    
    #test example    
    # routes = dict()
    # routes[('London', 'Dublin')] = 464
    # routes[('London', 'Belfast')] = 518
    # routes[('Dublin', 'Belfast')] = 141
    
    with open("test.file9", "r") as f:
        parser = re.compile(r'(\w+)\sto\s(\w+)\s=\s(\d+)')
        elements = set()
        routes = dict()
        for line in f:
            res = parser.match(line)
            if res != None:
                routes[(res.group(1), res.group(2))] = int(res.group(3))
                elements.add(res.group(1))
                elements.add(res.group(2))
        #print(routes)
                        


    #shortest route
    
    res = getShortestRoute(elements, routes)    
    
    if res[0] != None and res[1] != None:             
        print("Shortest route is:")
        print("->".join(res[1]))
        print("Value: {}".format(res[0]))
    else:
        print("Not found route")
        
    res = getLongestRoute(elements, routes)    
    
    if res[0] != None and res[1] != None:             
        print("Longest route is:")
        print("->".join(res[1]))
        print("Value: {}".format(res[0]))
    else:
        print("Not found route")
    
        