
"""
Gets checksum of a list of IDs
"""
def getChecksum(inputList):
    twice = 0
    thrice = 0
    for ID in inputList:
        twiceFound = False
        thriceFound = False
        for c in list(ID): #for each character in the ID string
            charCount = list(ID).count(c) #how many times character appear in string
            if charCount == 2 and twiceFound == False:
                twiceFound = True
                twice += 1
            if charCount == 3 and thriceFound == False:
                thriceFound = True
                thrice += 1
    return twice*thrice

"""
Makes a list of ID strings from an input file
"""
def makeListFromInput(inputFile):
    inList = list()
    for line in open(inputFile,"r"):
        inList.append(line.rstrip())
    return inList

print(getChecksum(makeListFromInput("input.txt")))
