
"""
Gets checksum of a list of IDs
"""
def getChecksum(inputFile):
    inputList = makeListFromInput(inputFile)
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

"""
PART 2
"""

"""
Find indices of different letters on two strings, assuming they are the same size
- for this specific task our desired length of the indices list should be 1
"""

def findNumDiff(s1,s2):
    letters1 = list(s1)
    letters2 = list(s2)
    indices = list()
    count=0
    diff = 0
    while(count<len(letters1)):
        if letters1[count] != letters2[count]:
            indices.append(count)
        count+=1
    return indices

"""
Function to find one of the correct boxes by finding other boxes with an ID that differs in 1 character.
To find the common letters we then remove the differenting character
"""

def findCommonLetters(inputFile):
    inputList = makeListFromInput(inputFile)
    for ID in inputList:
        for otherID in inputList:
            if otherID != ID and len(findNumDiff(ID,otherID)) == 1:
                index = findNumDiff(ID,otherID)[0]
                return ID[:index] + ID[index+1:]

print("checksum: " + str(getChecksum("input.txt")))
print("common ID of correct boxes: " + str(findCommonLetters("input.txt")))
