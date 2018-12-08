
from timeit import default_timer as timer
import string


def readFile(inputFile):
    return open(inputFile, 'r').read()

"""
Removed chars on index 1 and index 2
"""
def removeChars(string,index1,index2):
    return string[:index1] + string[index2+1:]

"""
Removed all occurrences of a type, both lowercase and uppercase, for example c and C
"""
def removeAllOfType(string,type):
    return string.replace(type.lower(),"").replace(type.upper(),"")



def sameTypeDifferentPolarity(p1,p2):
    if p1.lower() == p2.lower() and p1 != p2:
        return True
    else:
        return False

"""
Finds length of a polymer after reaction
"""
def getReactionLength(s):
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
    return len(cs.rstrip())

"""
Finds the shortest length of a polymer possible by removing each letter of the alphabet step-wise
from the string and calculating the new strings respective reaction length
"""
def mostEffectiveRemovalLength(s):
    alphabet = list(string.ascii_lowercase)
    shortest = len(s)
    for letter in alphabet:
        removedString = removeAllOfType(s,letter)
        length = getReactionLength(removedString)
        if length < shortest:
            shortest = length
    return shortest





print("------------part 1-----------")
start = timer()
str = readFile("input.txt")
length = getReactionLength(str)
print(length,"units remain after reacting the polymer")
end = timer()
print("computation time:",end-start)



print("------------part 2-----------")
start = timer()
print(mostEffectiveRemovalLength(str), "is the length of the shortest polymer i can produce")
end = timer()
print("computation time:",end-start)
