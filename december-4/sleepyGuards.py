
from collections import Counter
from timeit import default_timer as timer

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


    #for ID of most sleepy guard
    def mostSleep(self):
        mostSleep = (0,0)
        for guard in self.getGuards():
            amountOfSleep = self.guards[guard].fetchSleep()
            if amountOfSleep > mostSleep[1]:
                mostSleep = (guard, self.guards[guard].fetchSleep())
        return mostSleep[0]

    def hasGuard(self,ID):
        if ID in self.guards:
            return True
        else:
            return False


class Guard:

    def __init__(self,ID):
        self.ID = ID
        self.totalSleep = 0
        self.sleepTimes = list()

    def addSleep(self,amount):
        self.totalSleep += amount

    def fetchSleep(self):
        return self.totalSleep

    def getID(self):
        return self.ID

    def fallAsleep(self,minute):
        self.lastTimeOfSleep = minute

    def wakeUp(self,minute):
        self.lastTimeOfWake = minute
        self.addSleep(self.lastTimeOfWake-self.lastTimeOfSleep)
        for time in range (self.lastTimeOfSleep,self.lastTimeOfWake):
            self.sleepTimes.append(time)

    def mostFrequentMinute(self):
        cnt = Counter(self.sleepTimes)
        return cnt.most_common(1)

def newShiftID(line):
    splitLine = line.split(" ")
    if splitLine[2] == "Guard":
        ID = splitLine[3][1:]
        return ID
    else:
        return None

def sleepEvent(line):
    if line.split(" ")[2] == "falls":
        return True
    else:
        return False

def wakeEvent(line):
    if line.split(" ")[2] == "wakes":
        return True
    else:
        return False

def getTime(line):
    return int(line.split(" ")[1][:5].split(":")[1])


start = timer()
eventList = getInput("input.txt")
factory = Factory()
currentID = None
for line in eventList:
    newGuardID = newShiftID(line)
    if newGuardID != None and not factory.hasGuard(newGuardID):
        #print("new guard begins shift!",newGuardID)
        currentID = newGuardID
        factory.addGuard(newGuardID)
    elif newGuardID != None and factory.hasGuard(newGuardID):
        currentID = newGuardID
    elif sleepEvent(line):
        #print("fell asleep!")
        time = getTime(line)
        factory.getGuard(currentID).fallAsleep(time)
    elif wakeEvent(line):
        #print("woke up!")
        time = getTime(line)
        factory.getGuard(currentID).wakeUp(time)

#PART 1
print("---------PART 1----------")
mostSleepyGuard = factory.getGuard(factory.mostSleep())
mostFreqMinute = mostSleepyGuard.mostFrequentMinute()[0][0]
amount = mostSleepyGuard.fetchSleep()
print("Guard", factory.mostSleep(),"slept the most, with a total of", amount, "minutes, and spends most time asleep on 00:" + str(mostFreqMinute))
print("-------------------------")

#PART 2
mostSleepOnSameMinute = (0,0)
mostSleepyGuard = 0
for guard in factory.getGuards():
    mostFreq = factory.getGuard(guard).mostFrequentMinute()
    if mostFreq == []:
        continue
    fellAsleepOn = mostFreq[0][0]
    amount = mostFreq[0][1]

    if amount > mostSleepOnSameMinute[1]:
        mostSleepOnSameMinute = (fellAsleepOn,amount)
        mostSleepyGuard = guard
print("--------PART 2----------")
print("Guard",mostSleepyGuard,"slept on",mostSleepOnSameMinute[0], mostSleepOnSameMinute[1], "times")
print("------------------------")
end = timer()
print("computation time:",end-start)
