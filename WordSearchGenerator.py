import random
from WordSearchInfo import WordSearchInfo

def fillRestOfWordSearch(wordSearchInfo):
    LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for row in range(wordSearchInfo.wordSearchHeight):
        for col in range(wordSearchInfo.wordSearchWidth):
            if wordSearchInfo.wordSearch[row][col] == 0:
                randomLetter = random.choice(LETTERS)
                wordSearchInfo.wordSearch[row][col]=randomLetter


def addWord(canidatePositionIIncrementValue, canidatePositionJIncrementValue, canidatePositionHeight, canidatePositionWidth, word, wordSearchInfo):
    #dont need to check if the space exists in wordSearch, as tryWord does that
    for letter in word: #add the word to the word Search
        wordSearchInfo.wordSearch[canidatePositionHeight][canidatePositionWidth] = letter #update the correct spot in wordSearch
        nextOpenSpace = (wordSearchInfo.wordSearchWidth * canidatePositionHeight) + canidatePositionWidth #remove said spot from openWordSearchSpaces
        if nextOpenSpace in wordSearchInfo.openWordSearchSpaces:#TODO shorthen?
            wordSearchInfo.openWordSearchSpaces.remove(nextOpenSpace)
        canidatePositionHeight += canidatePositionIIncrementValue
        canidatePositionWidth += canidatePositionJIncrementValue


def tryWord(word, canidatePosition, directions, wordList, wordSearchInfo): #TODO add a check in try word to see if instead of '0', if the character in wordSearch[height][width] is already the 2nd character of the word. To increase overlap potential
    canidatePositionHeight = canidatePosition // wordSearchInfo.wordSearchWidth
    canidatePositionWidth = canidatePosition % wordSearchInfo.wordSearchWidth
    #get direction to try
    random.shuffle(directions)
    directionWorks = True
    for direction in directions:
        directionWorks = True
        canidatePositionHeightCopy = canidatePositionHeight
        canidatePositionWidthCopy = canidatePositionWidth

        if direction == "right":
            for letter in word[1:]: #the first element is skipped because it is already checked in getCanidatePosition
                if canidatePositionWidthCopy + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[canidatePositionHeightCopy][canidatePositionWidthCopy + 1] == 0:
                    canidatePositionWidthCopy += 1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(0, 1, canidatePositionHeight, canidatePositionWidth, word, wordSearchInfo)
                break
                    
        elif direction == "rightDown":
            for letter in word[1:]:
                if canidatePositionHeightCopy + 1 < wordSearchInfo.wordSearchHeight and canidatePositionWidthCopy + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[canidatePositionHeightCopy + 1][canidatePositionWidthCopy + 1] == 0:
                    canidatePositionHeightCopy += 1
                    canidatePositionWidthCopy += 1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(1, 1, canidatePositionHeight, canidatePositionWidth, word, wordSearchInfo)
                break

        elif direction == "down":
            for letter in word[1:]:
                if canidatePositionHeightCopy + 1 < wordSearchInfo.wordSearchHeight and wordSearchInfo.wordSearch[canidatePositionHeightCopy + 1][canidatePositionWidthCopy] == 0:
                    canidatePositionHeightCopy += 1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(1, 0, canidatePositionHeight, canidatePositionWidth, word, wordSearchInfo)
                break

        elif direction == "leftDown":
            for letter in word[1:]:
                if canidatePositionHeightCopy + 1 < wordSearchInfo.wordSearchHeight and canidatePositionWidthCopy - 1 >= 0 and wordSearchInfo.wordSearch[canidatePositionHeightCopy + 1][canidatePositionWidthCopy - 1] == 0:
                    canidatePositionHeightCopy += 1
                    canidatePositionWidthCopy += -1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(1, -1, canidatePositionHeight, canidatePositionWidth, word, wordSearchInfo)
                break

        elif direction == "left":
            for letter in word[1:]:
                if canidatePositionWidthCopy - 1 >= 0 and wordSearchInfo.wordSearch[canidatePositionHeightCopy][canidatePositionWidthCopy - 1] == 0:
                    canidatePositionWidthCopy += -1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(0, -1, canidatePositionHeight, canidatePositionWidth, word, wordSearchInfo)
                break

        elif direction == "leftUp":
            for letter in word[1:]:
                if canidatePositionHeightCopy - 1 >= 0 and canidatePositionWidthCopy - 1 >=0 and wordSearchInfo.wordSearch[canidatePositionHeightCopy - 1][canidatePositionWidthCopy - 1] == 0:
                    canidatePositionHeightCopy += -1
                    canidatePositionWidthCopy += -1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(-1, -1, canidatePositionHeight, canidatePositionWidth, word, wordSearchInfo)
                break

        elif direction == "up":
            for letter in word[1:]:
                if canidatePositionHeightCopy - 1 >= 0 and wordSearchInfo.wordSearch[canidatePositionHeightCopy - 1][canidatePositionWidthCopy] == 0:
                    canidatePositionHeightCopy += -1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(-1, 0, canidatePositionHeight, canidatePositionWidth, word, wordSearchInfo)
                break
            
        elif direction == "rightUp":
            for letter in word[1:]:
                if canidatePositionHeightCopy - 1 >= 0 and canidatePositionWidthCopy + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[canidatePositionHeightCopy - 1][canidatePositionWidthCopy + 1] == 0:
                    canidatePositionHeightCopy += -1
                    canidatePositionWidthCopy += 1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(-1, 1, canidatePositionHeight, canidatePositionWidth, word, wordSearchInfo)
                break

    if directionWorks:
        print("added ", word, " at position [",canidatePositionHeight,"][",canidatePositionWidth,"] in the ",direction," direction")
        return True
    else:
        return False


def getCanidatePosition(wordSearchInfo):
    while True: 
        tempOpenWordSearchSpaces = wordSearchInfo.openWordSearchSpaces
        if len(tempOpenWordSearchSpaces) == 0:
            print("there is no place to put the remaining words. Please try again.")
            return -1
        canidatePosition = random.choice(tempOpenWordSearchSpaces)
        canidatePositionHeight = canidatePosition // wordSearchInfo.wordSearchWidth
        canidatePositionWidth = canidatePosition % wordSearchInfo.wordSearchWidth
        if wordSearchInfo.wordSearch[canidatePositionHeight][canidatePositionWidth] != 0:
            wordSearchInfo.openWordSearchSpaces.remove(canidatePosition)
            continue
        return canidatePosition


def findNearestSquare(goal):
    i = 1
    while i * i < goal:
        i += 1
    return i


def print2DWordSearch(wordSearchInfo):
    for i in range(wordSearchInfo.wordSearchHeight):
        print(*wordSearchInfo.wordSearch[i])

        
def write2DWordSearchToFile(wordSearchInfo, wordSearchFile):
    for i in range(wordSearchInfo.wordSearchHeight):
        print(*wordSearchInfo.wordSearch[i], file=wordSearchFile)


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
            wordSearchInfo.openWordSearchSpaces.remove(canidatePosition)
    print("words left:",wordList)
    if len(wordList) == 0:
        return True
    return False


def main():
    #TODO add the ability to read files from a CLI
    wordSearchGridMultiplier = 2 # the larger this number is, the more likely that every  word gets added
    wordList = []
    directions = ["right", "rightDown", "down", "leftDown", "left", "leftUp", "up", "rightUp"]
    wordListFile = open("WordSearchWords.txt","r+")
    wordSearchFile = open("WordSearch.txt","w+")
    for line in wordListFile:
        wordList.append(line.rstrip('\n').upper())
    wordListFile.close()
    print(wordList)

    #set up size of wordSeach
    maxWordLength = len(max(wordList, key = len))
    sumOfWordLengths = len(''.join(wordList))
    nearestSquare = findNearestSquare(sumOfWordLengths)
    wordSearchMinLength = max(maxWordLength,nearestSquare) + 1 #done to increase the speed of a succesful createWordSearch() with every word added
    print("maxWordLength:",maxWordLength,", sumOfWordLengths:",sumOfWordLengths,", nearestSquare:",nearestSquare,", wordSearchMinLength:",wordSearchMinLength)
    wordSearchHeight = random.randint(wordSearchMinLength,(wordSearchGridMultiplier * wordSearchMinLength))
    wordSearchWidth = random.randint(wordSearchMinLength,(wordSearchGridMultiplier * wordSearchMinLength))
    print("wordSearchHeight:",wordSearchHeight,", wordSearchWidth:",wordSearchWidth)
    wordSearchSize = wordSearchHeight * wordSearchWidth

    wordSearch = [[0 for i in range(wordSearchWidth)] for j in range(wordSearchHeight)] 
    openWordSearchSpaces = [i for i in range(wordSearchSize)]

    wordSearchDepth = 1 #Here so that WordSearchInfo could be reused for the 3D version
    wordSearchInfo = WordSearchInfo(wordSearch, wordSearchDepth, wordSearchHeight, wordSearchWidth, wordSearchSize, openWordSearchSpaces)

    allWordsAdded = False
    while(allWordsAdded == False):
        wordListCopy = wordList.copy()
        allWordsAdded = createWordSearch(wordListCopy, wordSearchInfo, directions)
        if allWordsAdded == False:
            wordSearch = [[0 for i in range(wordSearchWidth)] for j in range(wordSearchHeight)] 
            openWordSearchSpaces = [i for i in range(wordSearchSize)]
            wordSearchInfo = WordSearchInfo(wordSearch, wordSearchDepth, wordSearchHeight, wordSearchWidth, wordSearchSize, openWordSearchSpaces)
            print("attempt failed. Trying again")

    fillRestOfWordSearch(wordSearchInfo) # comment this out to see the results without the random letters
    print2DWordSearch(wordSearchInfo)
    write2DWordSearchToFile(wordSearchInfo, wordSearchFile)
    wordSearchFile.close()
    wordListFile.close()


print("generating the word search")
if __name__=="__main__":
    main()  

