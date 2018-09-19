import random
from WordSearchInfo import WordSearchInfo

def fillRestOfWordSearch(wordSearchInfo):
    LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for k in range(wordSearchInfo.wordSearchDepth):
        for j in range(wordSearchInfo.wordSearchHeight):
            for i in range(wordSearchInfo.wordSearchWidth):
                if wordSearchInfo.wordSearch[k][j][i] == 0:
                    randomLetter = random.choice(LETTERS)
                    wordSearchInfo.wordSearch[k][j][i]=randomLetter


def addWord(canidatePositionDepthIncrementValue, canidatePositionHeightIncrementValue, canidatePositionWidthIncrementValue, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo):
    #dont need to check if the space exists in wordSearch, as tryWord does that
    for letter in word: #add the word to the word Search
        wordSearchInfo.wordSearch[canidatePositionDepth][canidatePositionHeight][canidatePositionWidth] = letter #update the correct spot in wordSearch
        nextOpenSpace = canidatePositionWidth + (canidatePositionHeight * wordSearchInfo.wordSearchWidth) + (canidatePositionDepth * wordSearchInfo.wordSearchWidth * wordSearchInfo.wordSearchHeight) #remove said spot from openWordSearchSpaces
        if nextOpenSpace in wordSearchInfo.openWordSearchSpaces:#TODO shorthen?
            tempOpenWordSearchSpaces = wordSearchInfo.openWordSearchSpaces
            tempOpenWordSearchSpaces.remove(nextOpenSpace)
            wordSearchInfo.openWordSearchSpaces = tempOpenWordSearchSpaces
            #wordSearchInfo.openWordSearchSpaces = wordSearchInfo.openWordSearchSpaces.remove(nextOpenSpace)
        canidatePositionWidth += canidatePositionWidthIncrementValue
        canidatePositionHeight += canidatePositionHeightIncrementValue
        canidatePositionDepth += canidatePositionDepthIncrementValue


def tryWord(word, canidatePosition, directions, wordList, wordSearchInfo):
    canidatePositionWidth = canidatePosition % wordSearchInfo.wordSearchWidth#TODO this is already calculated in gcp
    canidatePositionHeight = (canidatePosition // wordSearchInfo.wordSearchWidth) % wordSearchInfo.wordSearchHeight
    canidatePositionDepth = canidatePosition // (wordSearchInfo.wordSearchWidth * wordSearchInfo.wordSearchHeight)
    #get direction to try
    random.shuffle(directions)
    directionWorks = True
    for direction in directions:
        directionWorks = True
        canidatePositionWidthCopy = canidatePositionWidth
        canidatePositionHeightCopy = canidatePositionHeight
        canidatePositionDepthCopy = canidatePositionDepth

    #Depth does not change
        if direction == "right":
            for letter in word[1:]: #the first element is skipped because it is already checked in getCanidatePosition
                if canidatePositionWidthCopy + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[canidatePositionDepthCopy][canidatePositionHeightCopy][canidatePositionWidthCopy + 1] == 0:
                    canidatePositionWidthCopy += 1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(0, 0, 1, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo)
                break
            
        elif direction == "rightDown":
            for letter in word[1:]:
                if canidatePositionHeightCopy + 1 < wordSearchInfo.wordSearchHeight and canidatePositionWidthCopy + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[canidatePositionDepthCopy][canidatePositionHeightCopy + 1][canidatePositionWidthCopy + 1] == 0:
                    canidatePositionHeightCopy += 1
                    canidatePositionWidthCopy += 1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(0, 1, 1, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo)
                break

        elif direction == "down":
            for letter in word[1:]:
                if canidatePositionHeightCopy + 1 < wordSearchInfo.wordSearchHeight and wordSearchInfo.wordSearch[canidatePositionDepthCopy][canidatePositionHeightCopy + 1][canidatePositionWidthCopy] == 0:
                    canidatePositionHeightCopy += 1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(0, 1, 0, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo)
                break

        elif direction == "leftDown":
            for letter in word[1:]:
                if canidatePositionHeightCopy + 1 < wordSearchInfo.wordSearchHeight and canidatePositionWidthCopy - 1 >= 0 and wordSearchInfo.wordSearch[canidatePositionDepthCopy][canidatePositionHeightCopy + 1][canidatePositionWidthCopy - 1] == 0:
                    canidatePositionHeightCopy += 1
                    canidatePositionWidthCopy += -1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(0, 1, -1, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo)
                break

        elif direction == "left":
            for letter in word[1:]:
                if canidatePositionWidthCopy - 1 >= 0 and wordSearchInfo.wordSearch[canidatePositionDepthCopy][canidatePositionHeightCopy][canidatePositionWidthCopy - 1] == 0:
                    canidatePositionWidthCopy += -1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(0, 0, -1, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo)
                break

        elif direction == "leftUp":
            for letter in word[1:]:
                if canidatePositionHeightCopy - 1 >= 0 and canidatePositionWidthCopy - 1 >= 0 and wordSearchInfo.wordSearch[canidatePositionDepthCopy][canidatePositionHeightCopy - 1][canidatePositionWidthCopy - 1] == 0:
                    canidatePositionHeightCopy += -1
                    canidatePositionWidthCopy += -1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(0, -1, -1, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo)
                break

        elif direction == "up":
            for letter in word[1:]:
                if canidatePositionHeightCopy - 1 >= 0 and wordSearchInfo.wordSearch[canidatePositionDepthCopy][canidatePositionHeightCopy - 1][canidatePositionWidthCopy] == 0:
                    canidatePositionHeightCopy += -1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(0, -1, 0, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo)
                break
            
        elif direction == "rightUp":
            for letter in word[1:]:
                if canidatePositionHeightCopy - 1 >= 0 and canidatePositionWidthCopy + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[canidatePositionDepthCopy][canidatePositionHeightCopy - 1][canidatePositionWidthCopy + 1] == 0:
                    canidatePositionHeightCopy += -1
                    canidatePositionWidthCopy += 1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(0, -1, 1, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo)
                break

    #depth goes out (to the user)
        elif direction == "rightOut":
            for letter in word[1:]: #the first element is skipped because it is already checked in getCanidatePosition
                if canidatePositionDepthCopy - 1 >= 0 and canidatePositionWidthCopy + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[canidatePositionDepthCopy - 1][canidatePositionHeightCopy][canidatePositionWidthCopy + 1] == 0:
                    canidatePositionDepthCopy += -1
                    canidatePositionWidthCopy += 1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(-1, 0, 1, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo)
                break
            
        elif direction == "rightDownOut":
            for letter in word[1:]:
                if canidatePositionDepthCopy - 1 >= 0 and canidatePositionHeightCopy + 1 < wordSearchInfo.wordSearchHeight and canidatePositionWidthCopy + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[canidatePositionDepthCopy - 1][canidatePositionHeightCopy + 1][canidatePositionWidthCopy + 1] == 0:
                    canidatePositionDepthCopy += -1
                    canidatePositionHeightCopy += 1
                    canidatePositionWidthCopy += 1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(-1, 1, 1, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo)
                break

        elif direction == "downOut":
            for letter in word[1:]:
                if canidatePositionDepthCopy - 1 >= 0 and canidatePositionHeightCopy + 1 < wordSearchInfo.wordSearchHeight and wordSearchInfo.wordSearch[canidatePositionDepthCopy - 1][canidatePositionHeightCopy + 1][canidatePositionWidthCopy] == 0:
                    canidatePositionDepthCopy += -1
                    canidatePositionHeightCopy += 1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(-1, 1, 0, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo)
                break

        elif direction == "leftDownOut":
            for letter in word[1:]:
                if canidatePositionDepthCopy - 1 >= 0 and canidatePositionHeightCopy + 1 < wordSearchInfo.wordSearchHeight and canidatePositionWidthCopy - 1 >= 0 and wordSearchInfo.wordSearch[canidatePositionDepthCopy - 1][canidatePositionHeightCopy + 1][canidatePositionWidthCopy - 1] == 0:
                    canidatePositionDepthCopy += -1
                    canidatePositionHeightCopy += 1
                    canidatePositionWidthCopy += -1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(-1, 1, -1, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo)
                break

        elif direction == "leftOut":
            for letter in word[1:]:
                if canidatePositionDepthCopy - 1 >= 0 and canidatePositionWidthCopy - 1 >= 0 and wordSearchInfo.wordSearch[canidatePositionDepthCopy - 1][canidatePositionHeightCopy][canidatePositionWidthCopy - 1] == 0:
                    canidatePositionDepthCopy += -1
                    canidatePositionWidthCopy += -1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(-1, 0, -1, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo)
                break

        elif direction == "leftUpOut":
            for letter in word[1:]:
                if canidatePositionDepthCopy - 1 >= 0 and canidatePositionHeightCopy - 1 >= 0 and canidatePositionWidthCopy - 1 >= 0 and wordSearchInfo.wordSearch[canidatePositionDepthCopy - 1][canidatePositionHeightCopy - 1][canidatePositionWidthCopy - 1] == 0:
                    canidatePositionDepthCopy += -1
                    canidatePositionHeightCopy += -1
                    canidatePositionWidthCopy += -1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(-1, -1, -1, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo)
                break

        elif direction == "upOut":
            for letter in word[1:]:
                if canidatePositionDepthCopy - 1 >= 0 and canidatePositionHeightCopy - 1 >= 0 and wordSearchInfo.wordSearch[canidatePositionDepthCopy - 1][canidatePositionHeightCopy - 1][canidatePositionWidthCopy] == 0:
                    canidatePositionDepthCopy += -1
                    canidatePositionHeightCopy += -1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(-1, -1, 0, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo)
                break
            
        elif direction == "rightUpOut":
            for letter in word[1:]:
                if canidatePositionDepthCopy - 1 >= 0 and canidatePositionHeightCopy - 1 >= 0 and canidatePositionWidthCopy + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[canidatePositionDepthCopy - 1][canidatePositionHeightCopy - 1][canidatePositionWidthCopy + 1] == 0:
                    canidatePositionDepthCopy += -1
                    canidatePositionHeightCopy += -1
                    canidatePositionWidthCopy += 1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(-1, -1, 1, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo)
                break

    #depth goes in (away from user)
        elif direction == "rightIn":
            for letter in word[1:]: #the first element is skipped because it is already checked in getCanidatePosition
                if canidatePositionDepthCopy + 1 < wordSearchInfo.wordSearchDepth and canidatePositionWidthCopy + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[canidatePositionDepthCopy + 1][canidatePositionHeightCopy][canidatePositionWidthCopy + 1] == 0:
                    canidatePositionDepthCopy += 1
                    canidatePositionWidthCopy += 1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(1, 0, 1, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo)
                break
            
        elif direction == "rightDownIn":
            for letter in word[1:]:
                if canidatePositionDepthCopy + 1 < wordSearchInfo.wordSearchDepth and canidatePositionHeightCopy + 1 < wordSearchInfo.wordSearchHeight and canidatePositionWidthCopy + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[canidatePositionDepthCopy + 1][canidatePositionHeightCopy + 1][canidatePositionWidthCopy + 1] == 0:
                    canidatePositionDepthCopy += 1
                    canidatePositionHeightCopy += 1
                    canidatePositionWidthCopy += 1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(1, 1, 1, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo)
                break

        elif direction == "downIn":
            for letter in word[1:]:
                if canidatePositionDepthCopy + 1 < wordSearchInfo.wordSearchDepth and canidatePositionHeightCopy + 1 < wordSearchInfo.wordSearchHeight and wordSearchInfo.wordSearch[canidatePositionDepthCopy + 1][canidatePositionHeightCopy + 1][canidatePositionWidthCopy] == 0:
                    canidatePositionDepthCopy += 1
                    canidatePositionHeightCopy += 1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(1, 1, 0, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo)
                break

        elif direction == "leftDownIn":
            for letter in word[1:]:
                if canidatePositionDepthCopy + 1 < wordSearchInfo.wordSearchDepth and canidatePositionHeightCopy + 1 < wordSearchInfo.wordSearchHeight and canidatePositionWidthCopy - 1 >= 0 and wordSearchInfo.wordSearch[canidatePositionDepthCopy + 1][canidatePositionHeightCopy + 1][canidatePositionWidthCopy - 1] == 0:
                    canidatePositionDepthCopy += 1
                    canidatePositionHeightCopy += 1
                    canidatePositionWidthCopy += -1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(1, 1, -1, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo)
                break

        elif direction == "leftIn":
            for letter in word[1:]:
                if canidatePositionDepthCopy + 1 < wordSearchInfo.wordSearchDepth and canidatePositionWidthCopy - 1 >= 0 and wordSearchInfo.wordSearch[canidatePositionDepthCopy + 1][canidatePositionHeightCopy][canidatePositionWidthCopy - 1] == 0:
                    canidatePositionDepthCopy += 1
                    canidatePositionWidthCopy += -1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(1, 0, -1, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo)
                break

        elif direction == "leftUpIn":
            for letter in word[1:]:
                if canidatePositionDepthCopy + 1 < wordSearchInfo.wordSearchDepth and canidatePositionHeightCopy - 1 >= 0 and canidatePositionWidthCopy - 1 >= 0 and wordSearchInfo.wordSearch[canidatePositionDepthCopy + 1][canidatePositionHeightCopy - 1][canidatePositionWidthCopy - 1] == 0:
                    canidatePositionDepthCopy += 1
                    canidatePositionHeightCopy += -1
                    canidatePositionWidthCopy += -1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(1, -1, -1, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo)
                break

        elif direction == "upIn":
            for letter in word[1:]:
                if canidatePositionDepthCopy + 1 < wordSearchInfo.wordSearchDepth and canidatePositionHeightCopy - 1 >= 0 and wordSearchInfo.wordSearch[canidatePositionDepthCopy + 1][canidatePositionHeightCopy - 1][canidatePositionWidthCopy] == 0:
                    canidatePositionDepthCopy += 1
                    canidatePositionHeightCopy += -1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(1, -1, 0, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo)
                break
            
        elif direction == "rightUpIn":
            for letter in word[1:]:
                if canidatePositionDepthCopy + 1 < wordSearchInfo.wordSearchDepth and canidatePositionHeightCopy - 1 >= 0 and canidatePositionWidthCopy + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[canidatePositionDepthCopy + 1][canidatePositionHeightCopy - 1][canidatePositionWidthCopy + 1] == 0:
                    canidatePositionDepthCopy += 1
                    canidatePositionHeightCopy += -1
                    canidatePositionWidthCopy += 1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(1, -1, 1, canidatePositionWidth, canidatePositionHeight, canidatePositionDepth, word, wordSearchInfo)
                break

    if directionWorks:
        print("added ", word, " at position [",canidatePositionDepth,"][",canidatePositionHeight,"][",canidatePositionWidth,"] in the ",direction," direction")
        return True
    else:
        return False


def getCanidatePosition(wordSearchInfo):
    while True: 
        tempOpenWordSearchSpaces = wordSearchInfo.openWordSearchSpaces
        if len(tempOpenWordSearchSpaces) == 0:
            print("there is no place to put the remaining words. Please try again.") #TODO if this is triggered, automatically run the whole program again
            return -1
        canidatePosition = random.choice(tempOpenWordSearchSpaces)
        canidatePositionWidth = canidatePosition % wordSearchInfo.wordSearchWidth#TODO this is already calculated in gcp
        canidatePositionHeight = (canidatePosition // wordSearchInfo.wordSearchWidth) % wordSearchInfo.wordSearchHeight
        canidatePositionDepth = canidatePosition // (wordSearchInfo.wordSearchWidth * wordSearchInfo.wordSearchHeight)
        if wordSearchInfo.wordSearch[canidatePositionDepth][canidatePositionHeight][canidatePositionWidth] != 0:
            continue
        return canidatePosition


def findNearestCube(goal):
    i = 1
    while i * i * i < goal:
        i += 1
    return i


def print3DWordSearch(wordSearchInfo):
    for k in range((wordSearchInfo.wordSearchDepth)):
        for j in range(wordSearchInfo.wordSearchHeight):
            print(*wordSearchInfo.wordSearch[k][j])
        print('\n')

        
def write3DWordSearchToFile(wordSearchInfo, wordSearchFile):
    for k in range((wordSearchInfo.wordSearchDepth)):
        for j in range(wordSearchInfo.wordSearchHeight):
            print(*wordSearchInfo.wordSearch[k][j],file=wordSearchFile)
        print('\n',file=wordSearchFile)


def createWordSearch(wordList, wordSearchInfo, directions):
    wordAdded = False
    canidatePosition = -1
    while len(wordList) > 0 and wordSearchInfo.openWordSearchSpaces != None:
        canidatePosition = getCanidatePosition(wordSearchInfo)
        if canidatePosition == -1: # If there are no more open spaces in wordSearch
            break
        random.shuffle(wordList)
        for word in wordList:
            wordAdded = tryWord(word, canidatePosition, directions, wordList, wordSearchInfo)# wordSearch, wordSearchWidth, wordSearchHeight, wordSearchSize)
            if wordAdded: # if the word was added, remove it as an option and find a new postion to repeat the process over from
                wordList.remove(word)
                break
        if wordAdded == False:
            tempOpenWordSearchSpaces = wordSearchInfo.openWordSearchSpaces#TODO shorten?
            tempOpenWordSearchSpaces.remove(canidatePosition)
            wordSearchInfo.openWordSearchSpaces = tempOpenWordSearchSpaces
            #wordSearchInfo.openWordSearchSpaces = wordSearchInfo.openWordSearchSpaces.remove(canidatePosition) #this randomly sets openWordSearchSpaces as None
    print("words left:",wordList)
    if len(wordList) == 0:
        return True
    return False


def main():
    #TODO add the ability to read files from a CLI
    wordSearchGridMultiplier = 2 # the larger this number is, the more likely that every  word gets added
    wordList = []
    directions = ["right", "rightDown", "down", "leftDown", "left", "leftUp", "up", "rightUp","rightOut", "rightDownOut", "downOut", "leftDownOut", "leftOut", "leftUpOut", "upOut", "rightUpOut", "rightIn", "rightDownIn", "downIn", "leftDownIn", "leftIn", "leftUpIn", "upIn", "rightUpIn"]
    wordListFile = open("WordSearchWords.txt","r+")
    wordSearchFile = open("WordSearch.txt","w+")
    for line in wordListFile:
        wordList.append(line.rstrip('\n').upper())
    wordListFile.close()
    print(wordList)

    #set up size of wordSeach
    maxWordLength = len(max(wordList, key = len))
    sumOfWordLengths = len(''.join(wordList))
    nearestCube = findNearestCube(sumOfWordLengths)
    wordSearchMinLength = max(maxWordLength, nearestCube) + 1 #done to increase the speed of a succesful createWordSearch() with every word added
    print("maxWordLength:",maxWordLength,", sumOfWordLengths:",sumOfWordLengths,", nearestCube:",nearestCube,", wordSearchMinLength:",wordSearchMinLength)
    wordSearchHeight = random.randint(wordSearchMinLength,(wordSearchGridMultiplier * wordSearchMinLength))
    wordSearchWidth = random.randint(wordSearchMinLength,(wordSearchGridMultiplier * wordSearchMinLength))
    wordSearchDepth = random.randint(wordSearchMinLength,(wordSearchGridMultiplier * maxWordLength))
    print(", wordSearchDepth:",wordSearchDepth,", wordSearchHeight:",wordSearchHeight,", wordSearchWidth:",wordSearchWidth)
    wordSearchSize = wordSearchHeight * wordSearchWidth* wordSearchDepth
    
    wordSearch = [[[0 for i in range(wordSearchWidth)] for j in range(wordSearchHeight)] for k in range(wordSearchDepth)] 
    openWordSearchSpaces = [i for i in range(wordSearchSize)]

    #print(wordSearch)
    wordSearchInfo = WordSearchInfo(wordSearch, wordSearchDepth, wordSearchHeight, wordSearchWidth, wordSearchSize, openWordSearchSpaces)

    allWordsAdded = False
    while(allWordsAdded == False):
        wordListCopy = wordList.copy()
        allWordsAdded = createWordSearch(wordListCopy, wordSearchInfo, directions)
        if allWordsAdded == False:
            wordSearch = [[[0 for i in range(wordSearchWidth)] for j in range(wordSearchHeight)] for k in range(wordSearchDepth)] 
            openWordSearchSpaces = [i for i in range(wordSearchSize)]
            wordSearchInfo = WordSearchInfo(wordSearch, wordSearchDepth, wordSearchHeight, wordSearchWidth, wordSearchSize, openWordSearchSpaces)
            print("attempt failed. Trying again")

    fillRestOfWordSearch(wordSearchInfo) # comment this out to see the results without the random letters
    print3DWordSearch(wordSearchInfo)
    write3DWordSearchToFile(wordSearchInfo, wordSearchFile)
    wordSearchFile.close()
    wordListFile.close()


print("generating the word search")
if __name__=="__main__":
    main()  
