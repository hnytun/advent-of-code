


"""
Fabric claim, contains an ID, starting position of fabric, and dimensions
"""

class Claim:

    def __init__(self,ID,xPos,yPos,xDimension,yDimension):
        self.ID = ID
        self.position = (xPos,yPos)
        self.dimension = (xDimension,yDimension)

    """
    Get positions that the fabric claim covers
    """
    def getCoveringArea(self):
        coveredArea = list()
        for x in range(self.position[0],self.position[0]+self.dimension[0]):
            for y in range(self.position[1],self.position[1] + self.dimension[1]):
                coveredArea.append((x,y))
        return coveredArea
    """
    returns the position of the fabric as a tuple
    """

    def getPosition(self):
        return (self.position[0],self.position[1])

    def getID(self):
        return self.ID

"""
gets input from file and makes a list of claim objects
"""

def getInput(inputFile):

    claimList = list()
    for line in open(inputFile,"r"):
        arguments = line.split(" ")
        ID = arguments[0]
        startingPosX = int(arguments[2].split(",")[0])
        startingPosY = int(arguments[2].split(",")[1][:-1])
        dimensionX = int(arguments[3].split("x")[0])
        dimensionY = int(arguments[3].split("x")[1])
        claimList.append(Claim(ID, startingPosX,startingPosY,dimensionX,dimensionY))
    return claimList




"""
Part 2 - finding a claim that doesnt share a position with any other:
"""
allPositions = list()
claimList = getInput("input.txt")

for claim in claimList:
     for position in claim.getCoveringArea():
         allPositions.append(position)

for claim in claimList:
    onlyOne = True
    for position in claim.getCoveringArea():
        if allPositions.count(position) != 1:
            onlyOne = False
            break
    if onlyOne == True:
        print(claim.getID())
        break

"""
#PART 1 - finding total amount of overlaps:
#this one takes a good 10-15 min to run, could be optimized later.

overlaps=0
seenPositions = list()
addedOverlaps = list()
count=0
for claim in claimList:
    count+=1
    #print("count: " + str(count) + "of " + str(len(claimList)))
    for position in claim.getCoveringArea():
        if position in seenPositions and position not in addedOverlaps:
            overlaps+=1
            seenPositions.append(position)
            addedOverlaps.append(position)
        else:
            seenPositions.append(position)
    if count%10 == 0:
        print(count)
        print("overlaps: ",overlaps)
print(overlaps)

"""
