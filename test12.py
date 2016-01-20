import json



def getNumbersFromContainer(container):
    sum = 0
    for data in container:
        if isinstance(data, list):
            sum += getNumbersFromContainer(data)
        elif isinstance(data, dict):
            values = data.values()
            #12-2
            if not "red" in values:
                sum += getNumbersFromContainer(list(data.values()))
        elif isinstance(data, str):                     
            if data.isdigit():
                sum += int(data) 
        else:
            sum += data
            
    return sum




if __name__ == "__main__":

    with open('test.file12', 'r') as f:
        jsonData = json.loads(f.read().strip())
        print(getNumbersFromContainer(jsonData))