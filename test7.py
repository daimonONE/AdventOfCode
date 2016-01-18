import re

nodes = dict()
rules = []
class Node:    
    #constructor
    def __init__(self, name,p1=None, p2=None,  act=None, v=None, ch=None):
        self.name = name
        self.parent1 = p1
        #parent2 may be node or value
        self.parent2 = p2
        if ch:
            self.children = ch
        else:
            self.children = []
        self.value = v
        self.action = act        
        
    def toString(self):
        string = "Node: {}\n".format(self.name)
        string += "\tParent1\t\t" + str(self.parent1) + "\n"
        string += "\tParent2\t\t" + str(self.parent2) + "\n"
        for child in self.children:
            string += "\tChild\t\t" + str(child) + "\n"
        string += "\tValue\t\t" + str(self.value) + "\n"
        string += "\tAction\t\t" + str(self.action) + "\n"        
        return string

    def addChild(self, child):
        self.children.append(child)        
    
    
CMD_RSHIFT = "RSHIFT"
CMD_LSHIFT = "LSHIFT"
CMD_AND = "AND"
CMD_OR = "OR"
CMD_NOT = "NOT"
actionsList = [CMD_AND, CMD_OR, CMD_NOT, CMD_LSHIFT, CMD_RSHIFT]
 
    
roots = []
with open('test.file7', 'r') as f:
    primaryActionRE = re.compile(r'(.*)->\s(\w+)')
    binaryActionRE = re.compile(r'(\w+)\s(\w+)\s(\w+)')
    unaryActionRE = re.compile(r'(\w+)\s(\w+)')
    for line in f:
        needCreateNode = False
        nodeName = None
        parent1 = None
        parent2 = None
        action = None
        value = None
        res = primaryActionRE.match(line)
        #print(line)
        if res != None:
            leftPart = res.group(1).strip()
            nodeName = res.group(2).strip()
            #print(nodeName)
            res = binaryActionRE.match(leftPart)            
            if res != None:
                #print("binary")
                parent1 = res.group(1)                    
                action = res.group(2)
                parent2 = res.group(3)
                if parent1.isdigit():
                    temp = parent1
                    parent1 = parent2
                    parent2 = temp
                needCreateNode = True
            else:
                res = unaryActionRE.match(leftPart)
                if res != None:
                    #print("unary")
                    action = res.group(1)
                    parent1 = res.group(2)
                    needCreateNode = True
                else:
                    #Key value
                    #print("standalone")
                    if leftPart.isdigit():
                        value = leftPart
                        if not nodeName in roots: 
                            roots.append(nodeName)
                    else:
                        parent1 = leftPart
                    needCreateNode = True                    
               
        rules.append((nodeName, parent1, parent2, action, value)) 
        
        #7-2
        if(nodeName == 'b'):
            value = '46065'
        
                    
        if needCreateNode:
            if nodeName not in nodes:
                #print("not exists ." + nodeName + "." )
                nodes[nodeName] = Node(nodeName, parent1, parent2, action, value)
                #print("NodeName is in nodes {}".format(nodeName in nodes))
            else:
                # print("exists")
                tempNode = nodes[nodeName]
                tempNode.parent1 = parent1
                tempNode.parent2 = parent2
                tempNode.action = action
                tempNode.value = value
                
            if parent1 in nodes:
                nodes[parent1].addChild(nodeName)
            else:
                tempNode = Node(name = parent1)
                nodes[parent1] = tempNode
                tempNode.addChild(nodeName)
                
            if parent2 != None and not parent2.isdigit():
                if parent2 in nodes:
                    nodes[parent2].addChild(nodeName)
                else:
                    tempNode = Node(name = parent2)
                    nodes[parent2] = tempNode
                    tempNode.addChild(nodeName)
                    

# print("Start output")                
# for key, node in nodes.items():
#     print("Key is " + str(key))
#     print(node.toString())
# print("End output")
               

calculatedCount = 0

def calculateNode(node):
    if not node.value is None:
        #print("Already calculated")
        return False
    parent1 = nodes[node.parent1]
    value1 = None
    value2 = None
    if not parent1.value is None:
        value1 = int(parent1.value)
    if node.parent2: 
        if not node.parent2.isdigit():
            parent2 = nodes[node.parent2]
            if not parent2.value is None:
                value2 = int(parent2.value)
        else:
            value2 = int(node.parent2)
    
    value = None
    if node.action and node.action in actionsList:
        if node.action == CMD_NOT:
            if not value1 is None:
                value = ~value1            
            # else:
            #     print("Can't calculate yet, {}".format(value1))
        else:
            if not (value1 is None) and not (value2 is None):            
                if node.action == CMD_AND:
                    value = value1 & value2
                elif node.action == CMD_OR:
                    value = value1 | value2
                elif node.action == CMD_RSHIFT:
                    value = value1 >> value2
                elif node.action == CMD_LSHIFT:
                    value = value1 << value2                    
            # else:                
            #     print("Can't calculate yet, {} and {}".format(value1, value2))
    else:
        #print("Get value from parent")
        if not value1 is None:
            value = value1
        # else:
        #     print("Can't calculate yet, {}".format(value1))
    
    if value is None:
        #print("Error: can't calculateNode")
        return False        
    if not value is None:
        # print("Value is calculated " + str(value))
        node.value = value
        return True
        

stop = False
iterationsCount = 0
while calculatedCount < len(nodes):
    for key, node in nodes.items():
        children = node.children
        for child in children:
            #print("Calculating " + child)              
            if calculateNode(nodes[child]):
                if child == 'a':
                    stop = True
                    break
                calculatedCount += 1
        if stop: 
            break
    if stop:
        break
    print("Calculated {} of {} for {} iterations".format(calculatedCount, len(nodes), iterationsCount))
                
    iterationsCount += 1
    #if iterationsCount == 10:
    #    break
        
        
    
print(nodes['a'].toString())    
print("A value is {}".format(nodes['a'].value))    
         
        
    
                  
            
            
        
            
        