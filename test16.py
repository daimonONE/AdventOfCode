import re    
from common import debug

if __name__ == "__main__":            
    with open("test.file16", "r") as f:
        CHILDREN = "children"
        CATS = "cats"
        SAMOYEDS = "samoyeds"
        POMERANIANS = "pomeranians"
        AKITAS = "akitas"
        VIZSLAS = "vizslas"
        GOLDFISH = "goldfish"
        TREES = "trees"
        CARS = "cars"
        PERFUMES = "perfumes"
        detectList = [CHILDREN, CATS, SAMOYEDS, POMERANIANS, AKITAS, VIZSLAS, GOLDFISH, TREES, CARS, PERFUMES]
        parserNum = re.compile(r'Sue\s(\d+):')
        parsers = dict()
        for value in detectList:
            parsers[value] = re.compile(r'.*{}:\s(\d+).*'.format(value))
        foundAunt = None      
        foundAuntMatches = 0                  
        testValues = dict()
        testValues[CHILDREN] = 3
        testValues[CATS] = 7
        testValues[SAMOYEDS] = 2
        testValues[POMERANIANS] = 3
        testValues[AKITAS] = 0
        testValues[VIZSLAS] = 0
        testValues[GOLDFISH] = 5
        testValues[TREES] = 3
        testValues[CARS] = 2
        testValues[PERFUMES] = 1
        
        for line in f:                    
            res = parserNum.match(line)
            if res:
                num = res.group(1)                            
                matchesCount = 0
                for key, parser in parsers.items():
                    res = parser.match(line)
                    if res:
                        #16-1
                        # val = int(res.group(1))
                        # if testValues[key] == val:
                        #      matchesCount += 1
                        #16-2
                        val = int(res.group(1))
                        match = False
                        if key == CATS or key == TREES:
                            match = val > testValues[key]
                        elif key == GOLDFISH or key == POMERANIANS:
                            match = val < testValues[key]
                        else:
                            match =  testValues[key] == val
                        if match:
                            debug("Sue {} matched {} {}".format(num, key, val))
                            matchesCount += 1
                        else:
                            debug("Sue {} NOT matched {} {}".format(num, key, val))
                            matchesCount = 0
                            break
                if matchesCount > foundAuntMatches:
                    debug("Found Aunt " + num + " {}".format(matchesCount))
                    foundAunt = num
                    foundAuntMatches = matchesCount
                                                       
    print("Found Aunt is Sue {}".format(foundAunt))     