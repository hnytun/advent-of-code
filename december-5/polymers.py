
from timeit import default_timer as timer

def readFile(inputFile):
    return open(inputFile, 'r').read()

"""
Replaces index 1 and index 2 with a new string
"""
def removeChars(string,index1,index2):
    return string[:index1] + string[index2+1:]


def sameTypeDifferentPolarity(p1,p2):
    if p1.lower() == p2.lower() and p1 != p2:
        return True
    else:
        return False


def getReaction(s):
    cs = s
    index1 = 0
    index2 = 1
    while(index2 < len(cs)):
        if sameTypeDifferentPolarity(cs[index1],cs[index2]):
            #print("found reaction", cs[index1],cs[index2])
            #print("removed", cs[index1],cs[index2])
            cs = removeChars(cs,index1,index2)
            #if we hit a reaction, we backtrack until we cant find another resulting reaction
            #earlier in the list
            index1 -=1
            index2 -=1
            continue
        index1 +=1
        index2 +=1
    return cs.rstrip()

#part 1
start = timer()
str = readFile("input.txt")
str = getReaction(str)
print(len(str))
end = timer()
print("computation time:",end-start)
