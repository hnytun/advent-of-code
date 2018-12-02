
"""
December 1st.
"""

def frequencyList(inputFile):
    inputFile = inputFile
    frequencyList = list()
    startingFrequency = 0
    while(True):
        for line in open(inputFile,"r"):
            if list(line)[0] == "+":
                number = line.split("+")[1:][0]
                startingFrequency += int(number)
            elif list(line)[0] == "-":
                number = line.split("-")[1:][0]
                startingFrequency -= int(number)

            if startingFrequency in frequencyList:
                return startingFrequency
            frequencyList.append(startingFrequency)


print(frequencyList("input.txt"))
