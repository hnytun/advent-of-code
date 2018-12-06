

"""
Input handling, take in and sort

"""

def sortTimestamps(eventList):
    eventList.sort(key = lambda x: x.split("]")[0])
    return eventList

def getInput(inputFile):
    allEvents = list()
    for line in open(inputFile):
        allEvents.append(line)
    return sortTimestamps(allEvents)




class Factory:

    def __init__(self):
        self.guards = dict()

    def getGuards(self):
        return self.guards

    def addGuard(self,ID):
        self.guards[ID] = Guard(ID)

    def getGuard(self,ID):
        return self.guards[ID]

    def mostSleep(self):
        pass


class Guard:

    def __init__(self,ID):
        self.ID = ID
        self.totalSleep = 0

    def addSleep(self,amount):
        self.totalSleep += amount

    def fetchSleep(self):
        return self.totalSleep




eventList = getInput("input.txt")

#print eventList for debugging
for e in eventList:
    print(e)

####test###
factory = Factory()
factory.addGuard(1)
factory.getGuard(1).addSleep(10)
print(factory.getGuard(1).fetchSleep())
