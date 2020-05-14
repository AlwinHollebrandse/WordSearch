import random
import math
from WordSearchInfo import WordSearchInfo

# was 449 lines
# TODO missing pure 'IN' and 'OUT' directions

def main():
    print("generating the word search")
    # TODO add the ability to read files from a CLI
    wordSearchGridMultiplier = 2 # the larger this number is, the more likely that every  word gets added
    if wordSearchGridMultiplier < 1:
        print('wordSearchGridMultiplier must be greater than 1')
        return
    directions = ["right", "rightDown", "down", "leftDown", "left", "leftUp", "up", "rightUp","rightOut", "rightDownOut", "downOut", "leftDownOut", "leftOut", "leftUpOut", "upOut", "rightUpOut", "rightIn", "rightDownIn", "downIn", "leftDownIn", "leftIn", "leftUpIn", "upIn", "rightUpIn"]
    with open('WordSearchWords.txt','r+') as wordListFile:
        wordList = [line.rstrip('\n').upper() for line in wordListFile]

    #set up size of wordSeach
    maxWordLength = len(max(wordList, key = len))
    sumOfWordLengths = len(''.join(wordList))
    nearestCube = findNearestCube(sumOfWordLengths)
    wordSearchMinLength = max(maxWordLength, nearestCube) + 1 # done to increase the odds of a succesful createWordSearch() due to a better fitting wordSearch
    wordSearchDepth = random.randint(wordSearchMinLength,(wordSearchGridMultiplier * maxWordLength))
    wordSearchHeight = random.randint(wordSearchMinLength, (wordSearchGridMultiplier * wordSearchMinLength))
    wordSearchWidth = random.randint(wordSearchMinLength, (wordSearchGridMultiplier * wordSearchMinLength))

    wordSearchInfo = WordSearchInfo(wordSearchHeight = wordSearchHeight, wordSearchWidth = wordSearchWidth, 
        wordSearchDepth = wordSearchDepth, wordList = wordList)

    wordSearchInfo.toString()

    allWordsAdded = False
    while(allWordsAdded == False):
        wordListCopy = wordList.copy()
        allWordsAdded = createWordSearch(wordListCopy, wordSearchInfo, directions)
        
        # If the word search attempt failed, start over
        if allWordsAdded == False:
            wordSearchInfo = WordSearchInfo(wordSearchHeight = wordSearchHeight, wordSearchWidth = wordSearchWidth, 
                wordSearchDepth = wordSearchDepth, wordList = wordList)
            print('attempt failed. Trying again')

    fillRestOfWordSearch(wordSearchInfo)
    wordSearchInfo.printWordSearch()
    # with open('WordSearch.txt','w+') as wordSearchFile:     
        # wordSearchInfo.printWordSearchToFile(wordSearchFile)
    # TODO convert to JSON


def fillRestOfWordSearch(wordSearchInfo):
    LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for k in range(wordSearchInfo.wordSearchDepth):
        for j in range(wordSearchInfo.wordSearchHeight):
            for i in range(wordSearchInfo.wordSearchWidth):
                if wordSearchInfo.wordSearch[k][j][i] == 'a':
                    randomLetter = random.choice(LETTERS)
                    wordSearchInfo.wordSearch[k][j][i]=randomLetter


def addWord(depthChange, heightChange, widthChange, nextWordSearchDepthIndex, nextWordSearchWidthIndex, nextWordSearchHeightIndex, word, wordSearchInfo):
    for letter in word:
        print('\nHERE actual Size DHW', wordSearchInfo.wordSearchDepth, wordSearchInfo.wordSearchHeight, wordSearchInfo.wordSearchWidth)
        print('used DHW', nextWordSearchDepthIndex, nextWordSearchHeightIndex, nextWordSearchWidthIndex) # TODO BUG sometimes
        wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][nextWordSearchWidthIndex] = letter
        nextOpenSpace = nextWordSearchWidthIndex + (nextWordSearchHeightIndex * wordSearchInfo.wordSearchWidth) + (nextWordSearchDepthIndex * wordSearchInfo.wordSearchWidth * wordSearchInfo.wordSearchHeight)
        if nextOpenSpace in wordSearchInfo.openWordSearchSpaces:
            wordSearchInfo.openWordSearchSpaces.remove(nextOpenSpace)
        nextWordSearchWidthIndex += widthChange
        nextWordSearchHeightIndex += heightChange
        nextWordSearchDepthIndex += depthChange


def getCanidatePosition(wordSearchInfo):
    while True: 
        tempOpenWordSearchSpaces = wordSearchInfo.openWordSearchSpaces
        if len(tempOpenWordSearchSpaces) == 0:
            print("there is no place to put the remaining words. Please try again.")
            return -1
        canidatePosition = random.choice(tempOpenWordSearchSpaces)
        candidatePositionDepth = canidatePosition // (wordSearchInfo.wordSearchWidth * wordSearchInfo.wordSearchHeight)
        candidatePositionHeight = (canidatePosition // wordSearchInfo.wordSearchWidth) % wordSearchInfo.wordSearchHeight
        candidatePositionWidth = canidatePosition % wordSearchInfo.wordSearchWidth
        if wordSearchInfo.wordSearch[candidatePositionDepth][candidatePositionHeight][candidatePositionWidth] != 'a':
            wordSearchInfo.openWordSearchSpaces.remove(canidatePosition)
            continue
        return canidatePosition


def findNearestCube(goal):
    return math.ceil(math.pow(goal,1/3.))


def createWordSearch(wordList, wordSearchInfo, directions):
    wordAdded = False
    canidatePosition = -1
    while len(wordList) > 0 and len(wordSearchInfo.openWordSearchSpaces) > 0:
        canidatePosition = getCanidatePosition(wordSearchInfo)
        if canidatePosition == -1:
            break
        random.shuffle(wordList)
        for word in wordList:
            candidatePositionDepth = canidatePosition // (wordSearchInfo.wordSearchWidth * wordSearchInfo.wordSearchHeight)
            candidatePositionHeight = (canidatePosition // wordSearchInfo.wordSearchWidth) % wordSearchInfo.wordSearchHeight
            candidatePositionWidth = canidatePosition % wordSearchInfo.wordSearchWidth
            wordAdded = tryWord(word, candidatePositionDepth, candidatePositionHeight, candidatePositionWidth, directions, wordSearchInfo)
            if wordAdded:
                wordList.remove(word)
                break
        if wordAdded == False:
            wordSearchInfo.openWordSearchSpaces.remove(canidatePosition)
    print("words left:",wordList)
    if len(wordList) == 0:
        return True
    return False



def tryWordInDirection(wordSearchInfo, word, direction, startingHeight, startingWidth, heightChange, widthChange, startingDepth = -1, depthChange = 0):
    # TODO BUG I think these below might be changing the starting values...
    print('BUG DHW:', startingDepth, startingHeight, startingWidth)
    nextWordSearchDepthIndex = startingDepth
    nextWordSearchHeightIndex = startingHeight
    nextWordSearchWidthIndex = startingWidth
    directionWorks = True

    for letter in word[1:]:
        nextSpotExists = wordSearchInfo.directionCheck(direction, nextWordSearchDepthIndex, nextWordSearchHeightIndex, nextWordSearchWidthIndex)
        if nextSpotExists and wordSearchInfo.wordSearch[nextWordSearchDepthIndex + depthChange][nextWordSearchHeightIndex + heightChange][nextWordSearchWidthIndex + widthChange] == 'a': # TODO depth
            nextWordSearchDepthIndex += depthChange
            nextWordSearchHeightIndex += heightChange
            nextWordSearchWidthIndex += widthChange
        else:
            directionWorks = False
            break
    if directionWorks:
        addWord(depthChange, heightChange, widthChange, startingDepth, startingHeight, startingWidth, word, wordSearchInfo)
        return True
    return False


def tryWord(word, depth, height, width, directions, wordSearchInfo):
    # TODO add a check in try word to see if instead of '0', if the character in wordSearch[height][width] is already the 2nd character of the word. To increase overlap potential
    # get direction to try
    random.shuffle(directions)
    wordAdded = False
    usedDirection = None

    for direction in directions:
        if not wordAdded:
            usedDirection = direction

        # Depth does not change
            if direction == "right":
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'right',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = 0, widthChange = 1)
                
            elif direction == "rightDown":
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightDown',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = 1, widthChange = 1)

            elif direction == "down":
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightDown',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = 1, widthChange = 0)
                
            elif direction == "leftDown":
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftDown',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = 1, widthChange = -1)

            elif direction == "left":
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'left',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = 0, widthChange = -1)
  
            elif direction == "leftUp":
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftUp',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = -1, widthChange = -1)

            elif direction == "up":
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'up',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = -1, widthChange = 0)

            elif direction == "rightUp":
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightUp',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = -1, widthChange = 1)

        # depth goes out (to the user)
            elif direction == "rightOut":
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightOut',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = 0, widthChange = 1)
                
            elif direction == "rightDownOut":
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightDownOut',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = 1, widthChange = 1)

            elif direction == "downOut":
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightDownOut',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = 1, widthChange = 0)
                
            elif direction == "leftDownOut":
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftDownOut',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = 1, widthChange = -1)

            elif direction == "leftOut":
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftOut',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = 0, widthChange = -1)
  
            elif direction == "leftUpOut":
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftUpOut',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = -1, widthChange = -1)

            elif direction == "upOut":
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'upOut',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = -1, widthChange = 0)

            elif direction == "rightUpOut":
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightUpOut',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = -1, widthChange = 1)

        #depth goes in (away from user)
            elif direction == "rightIn":
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightIn',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = 0, widthChange = 1)
                
            elif direction == "rightDownIn":
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightDownIn',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = 1, widthChange = 1)

            elif direction == "downIn":
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightDownIn',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = 1, widthChange = 0)
                
            elif direction == "leftDownIn":
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftDownIn',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = 1, widthChange = -1)

            elif direction == "leftIn":
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftIn',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = 0, widthChange = -1)
  
            elif direction == "leftUpIn":
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftUpIn',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = -1, widthChange = -1)

            elif direction == "upIn":
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'upIn',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = -1, widthChange = 0)

            elif direction == "rightUpIn":
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightUpIn',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = -1, widthChange = 1)
        else:
            break

    if wordAdded:
        print("added ", word, " at position [", depth, "][", height, "][", width, "] in the ", direction, " direction")
        return True
    else:
        return False



    # nextWordSearchWidthIndex = canidatePosition % wordSearchInfo.wordSearchWidth#TODO this is already calculated in gcp
    # nextWordSearchHeightIndex = (canidatePosition // wordSearchInfo.wordSearchWidth) % wordSearchInfo.wordSearchHeight
    # nextWordSearchDepthIndex = canidatePosition // (wordSearchInfo.wordSearchWidth * wordSearchInfo.wordSearchHeight)
    # #get direction to try
    # random.shuffle(directions)
    # directionWorks = True
    # for direction in directions:
    #     directionWorks = True
    #     nextWordSearchWidthIndexCopy = nextWordSearchWidthIndex
    #     nextWordSearchHeightIndexCopy = nextWordSearchHeightIndex
    #     nextWordSearchDepthIndexCopy = nextWordSearchDepthIndex

    # #Depth does not change
    #     if direction == "right":
    #         for letter in word[1:]: #the first element is skipped because it is already checked in getCanidatePosition
    #             if nextWordSearchWidthIndexCopy + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[nextWordSearchDepthIndexCopy][nextWordSearchHeightIndexCopy][nextWordSearchWidthIndexCopy + 1] == 0:
    #                 nextWordSearchWidthIndexCopy += 1
    #             else:
    #                 directionWorks = False
    #                 break
    #         if directionWorks:
    #             addWord(0, 0, 1, nextWordSearchDepthIndex,  nextWordSearchHeightIndex,  nextWordSearchWidthIndex, word, wordSearchInfo)
    #             break
            
    #     elif direction == "rightDown":
    #         for letter in word[1:]:
    #             if nextWordSearchHeightIndexCopy + 1 < wordSearchInfo.wordSearchHeight and nextWordSearchWidthIndexCopy + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[nextWordSearchDepthIndexCopy][nextWordSearchHeightIndexCopy + 1][nextWordSearchWidthIndexCopy + 1] == 0:
    #                 nextWordSearchHeightIndexCopy += 1
    #                 nextWordSearchWidthIndexCopy += 1
    #             else:
    #                 directionWorks = False
    #                 break
    #         if directionWorks:
    #             addWord(0, 1, 1, nextWordSearchDepthIndex,  nextWordSearchHeightIndex,  nextWordSearchWidthIndex, word, wordSearchInfo)
    #             break

    #     elif direction == "down":
    #         for letter in word[1:]:
    #             if nextWordSearchHeightIndexCopy + 1 < wordSearchInfo.wordSearchHeight and wordSearchInfo.wordSearch[nextWordSearchDepthIndexCopy][nextWordSearchHeightIndexCopy + 1][nextWordSearchWidthIndexCopy] == 0:
    #                 nextWordSearchHeightIndexCopy += 1
    #             else:
    #                 directionWorks = False
    #                 break
    #         if directionWorks:
    #             addWord(0, 1, 0, nextWordSearchDepthIndex,  nextWordSearchHeightIndex,  nextWordSearchWidthIndex, word, wordSearchInfo)
    #             break

    #     elif direction == "leftDown":
    #         for letter in word[1:]:
    #             if nextWordSearchHeightIndexCopy + 1 < wordSearchInfo.wordSearchHeight and nextWordSearchWidthIndexCopy - 1 >= 0 and wordSearchInfo.wordSearch[nextWordSearchDepthIndexCopy][nextWordSearchHeightIndexCopy + 1][nextWordSearchWidthIndexCopy - 1] == 0:
    #                 nextWordSearchHeightIndexCopy += 1
    #                 nextWordSearchWidthIndexCopy += -1
    #             else:
    #                 directionWorks = False
    #                 break
    #         if directionWorks:
    #             addWord(0, 1, -1, nextWordSearchDepthIndex,  nextWordSearchHeightIndex,  nextWordSearchWidthIndex, word, wordSearchInfo)
    #             break

    #     elif direction == "left":
    #         for letter in word[1:]:
    #             if nextWordSearchWidthIndexCopy - 1 >= 0 and wordSearchInfo.wordSearch[nextWordSearchDepthIndexCopy][nextWordSearchHeightIndexCopy][nextWordSearchWidthIndexCopy - 1] == 0:
    #                 nextWordSearchWidthIndexCopy += -1
    #             else:
    #                 directionWorks = False
    #                 break
    #         if directionWorks:
    #             addWord(0, 0, -1, nextWordSearchDepthIndex,  nextWordSearchHeightIndex,  nextWordSearchWidthIndex, word, wordSearchInfo)
    #             break

    #     elif direction == "leftUp":
    #         for letter in word[1:]:
    #             if nextWordSearchHeightIndexCopy - 1 >= 0 and nextWordSearchWidthIndexCopy - 1 >= 0 and wordSearchInfo.wordSearch[nextWordSearchDepthIndexCopy][nextWordSearchHeightIndexCopy - 1][nextWordSearchWidthIndexCopy - 1] == 0:
    #                 nextWordSearchHeightIndexCopy += -1
    #                 nextWordSearchWidthIndexCopy += -1
    #             else:
    #                 directionWorks = False
    #                 break
    #         if directionWorks:
    #             addWord(0, -1, -1, nextWordSearchDepthIndex,  nextWordSearchHeightIndex,  nextWordSearchWidthIndex, word, wordSearchInfo)
    #             break

    #     elif direction == "up":
    #         for letter in word[1:]:
    #             if nextWordSearchHeightIndexCopy - 1 >= 0 and wordSearchInfo.wordSearch[nextWordSearchDepthIndexCopy][nextWordSearchHeightIndexCopy - 1][nextWordSearchWidthIndexCopy] == 0:
    #                 nextWordSearchHeightIndexCopy += -1
    #             else:
    #                 directionWorks = False
    #                 break
    #         if directionWorks:
    #             addWord(0, -1, 0, nextWordSearchDepthIndex,  nextWordSearchHeightIndex,  nextWordSearchWidthIndex, word, wordSearchInfo)
    #             break
            
    #     elif direction == "rightUp":
    #         for letter in word[1:]:
    #             if nextWordSearchHeightIndexCopy - 1 >= 0 and nextWordSearchWidthIndexCopy + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[nextWordSearchDepthIndexCopy][nextWordSearchHeightIndexCopy - 1][nextWordSearchWidthIndexCopy + 1] == 0:
    #                 nextWordSearchHeightIndexCopy += -1
    #                 nextWordSearchWidthIndexCopy += 1
    #             else:
    #                 directionWorks = False
    #                 break
    #         if directionWorks:
    #             addWord(0, -1, 1, nextWordSearchDepthIndex,  nextWordSearchHeightIndex,  nextWordSearchWidthIndex, word, wordSearchInfo)
    #             break

    # #depth goes out (to the user)
    #     elif direction == "rightOut":
    #         for letter in word[1:]: #the first element is skipped because it is already checked in getCanidatePosition
    #             if nextWordSearchDepthIndexCopy - 1 >= 0 and nextWordSearchWidthIndexCopy + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[nextWordSearchDepthIndexCopy - 1][nextWordSearchHeightIndexCopy][nextWordSearchWidthIndexCopy + 1] == 0:
    #                 nextWordSearchDepthIndexCopy += -1
    #                 nextWordSearchWidthIndexCopy += 1
    #             else:
    #                 directionWorks = False
    #                 break
    #         if directionWorks:
    #             addWord(-1, 0, 1, nextWordSearchDepthIndex,  nextWordSearchHeightIndex,  nextWordSearchWidthIndex, word, wordSearchInfo)
    #             break
            
    #     elif direction == "rightDownOut":
    #         for letter in word[1:]:
    #             if nextWordSearchDepthIndexCopy - 1 >= 0 and nextWordSearchHeightIndexCopy + 1 < wordSearchInfo.wordSearchHeight and nextWordSearchWidthIndexCopy + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[nextWordSearchDepthIndexCopy - 1][nextWordSearchHeightIndexCopy + 1][nextWordSearchWidthIndexCopy + 1] == 0:
    #                 nextWordSearchDepthIndexCopy += -1
    #                 nextWordSearchHeightIndexCopy += 1
    #                 nextWordSearchWidthIndexCopy += 1
    #             else:
    #                 directionWorks = False
    #                 break
    #         if directionWorks:
    #             addWord(-1, 1, 1, nextWordSearchDepthIndex,  nextWordSearchHeightIndex,  nextWordSearchWidthIndex, word, wordSearchInfo)
    #             break

    #     elif direction == "downOut":
    #         for letter in word[1:]:
    #             if nextWordSearchDepthIndexCopy - 1 >= 0 and nextWordSearchHeightIndexCopy + 1 < wordSearchInfo.wordSearchHeight and wordSearchInfo.wordSearch[nextWordSearchDepthIndexCopy - 1][nextWordSearchHeightIndexCopy + 1][nextWordSearchWidthIndexCopy] == 0:
    #                 nextWordSearchDepthIndexCopy += -1
    #                 nextWordSearchHeightIndexCopy += 1
    #             else:
    #                 directionWorks = False
    #                 break
    #         if directionWorks:
    #             addWord(-1, 1, 0, nextWordSearchDepthIndex,  nextWordSearchHeightIndex,  nextWordSearchWidthIndex, word, wordSearchInfo)
    #             break

    #     elif direction == "leftDownOut":
    #         for letter in word[1:]:
    #             if nextWordSearchDepthIndexCopy - 1 >= 0 and nextWordSearchHeightIndexCopy + 1 < wordSearchInfo.wordSearchHeight and nextWordSearchWidthIndexCopy - 1 >= 0 and wordSearchInfo.wordSearch[nextWordSearchDepthIndexCopy - 1][nextWordSearchHeightIndexCopy + 1][nextWordSearchWidthIndexCopy - 1] == 0:
    #                 nextWordSearchDepthIndexCopy += -1
    #                 nextWordSearchHeightIndexCopy += 1
    #                 nextWordSearchWidthIndexCopy += -1
    #             else:
    #                 directionWorks = False
    #                 break
    #         if directionWorks:
    #             addWord(-1, 1, -1, nextWordSearchDepthIndex,  nextWordSearchHeightIndex,  nextWordSearchWidthIndex, word, wordSearchInfo)
    #             break

    #     elif direction == "leftOut":
    #         for letter in word[1:]:
    #             if nextWordSearchDepthIndexCopy - 1 >= 0 and nextWordSearchWidthIndexCopy - 1 >= 0 and wordSearchInfo.wordSearch[nextWordSearchDepthIndexCopy - 1][nextWordSearchHeightIndexCopy][nextWordSearchWidthIndexCopy - 1] == 0:
    #                 nextWordSearchDepthIndexCopy += -1
    #                 nextWordSearchWidthIndexCopy += -1
    #             else:
    #                 directionWorks = False
    #                 break
    #         if directionWorks:
    #             addWord(-1, 0, -1, nextWordSearchDepthIndex,  nextWordSearchHeightIndex,  nextWordSearchWidthIndex, word, wordSearchInfo)
    #             break

    #     elif direction == "leftUpOut":
    #         for letter in word[1:]:
    #             if nextWordSearchDepthIndexCopy - 1 >= 0 and nextWordSearchHeightIndexCopy - 1 >= 0 and nextWordSearchWidthIndexCopy - 1 >= 0 and wordSearchInfo.wordSearch[nextWordSearchDepthIndexCopy - 1][nextWordSearchHeightIndexCopy - 1][nextWordSearchWidthIndexCopy - 1] == 0:
    #                 nextWordSearchDepthIndexCopy += -1
    #                 nextWordSearchHeightIndexCopy += -1
    #                 nextWordSearchWidthIndexCopy += -1
    #             else:
    #                 directionWorks = False
    #                 break
    #         if directionWorks:
    #             addWord(-1, -1, -1, nextWordSearchDepthIndex,  nextWordSearchHeightIndex,  nextWordSearchWidthIndex, word, wordSearchInfo)
    #             break

    #     elif direction == "upOut":
    #         for letter in word[1:]:
    #             if nextWordSearchDepthIndexCopy - 1 >= 0 and nextWordSearchHeightIndexCopy - 1 >= 0 and wordSearchInfo.wordSearch[nextWordSearchDepthIndexCopy - 1][nextWordSearchHeightIndexCopy - 1][nextWordSearchWidthIndexCopy] == 0:
    #                 nextWordSearchDepthIndexCopy += -1
    #                 nextWordSearchHeightIndexCopy += -1
    #             else:
    #                 directionWorks = False
    #                 break
    #         if directionWorks:
    #             addWord(-1, -1, 0, nextWordSearchDepthIndex,  nextWordSearchHeightIndex,  nextWordSearchWidthIndex, word, wordSearchInfo)
    #             break
            
    #     elif direction == "rightUpOut":
    #         for letter in word[1:]:
    #             if nextWordSearchDepthIndexCopy - 1 >= 0 and nextWordSearchHeightIndexCopy - 1 >= 0 and nextWordSearchWidthIndexCopy + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[nextWordSearchDepthIndexCopy - 1][nextWordSearchHeightIndexCopy - 1][nextWordSearchWidthIndexCopy + 1] == 0:
    #                 nextWordSearchDepthIndexCopy += -1
    #                 nextWordSearchHeightIndexCopy += -1
    #                 nextWordSearchWidthIndexCopy += 1
    #             else:
    #                 directionWorks = False
    #                 break
    #         if directionWorks:
    #             addWord(-1, -1, 1, nextWordSearchDepthIndex,  nextWordSearchHeightIndex,  nextWordSearchWidthIndex, word, wordSearchInfo)
    #             break

    # #depth goes in (away from user)
    #     elif direction == "rightIn":
    #         for letter in word[1:]: #the first element is skipped because it is already checked in getCanidatePosition
    #             if nextWordSearchDepthIndexCopy + 1 < wordSearchInfo.wordSearchDepth and nextWordSearchWidthIndexCopy + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[nextWordSearchDepthIndexCopy + 1][nextWordSearchHeightIndexCopy][nextWordSearchWidthIndexCopy + 1] == 0:
    #                 nextWordSearchDepthIndexCopy += 1
    #                 nextWordSearchWidthIndexCopy += 1
    #             else:
    #                 directionWorks = False
    #                 break
    #         if directionWorks:
    #             addWord(1, 0, 1, nextWordSearchDepthIndex,  nextWordSearchHeightIndex,  nextWordSearchWidthIndex, word, wordSearchInfo)
    #             break
            
    #     elif direction == "rightDownIn":
    #         for letter in word[1:]:
    #             if nextWordSearchDepthIndexCopy + 1 < wordSearchInfo.wordSearchDepth and nextWordSearchHeightIndexCopy + 1 < wordSearchInfo.wordSearchHeight and nextWordSearchWidthIndexCopy + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[nextWordSearchDepthIndexCopy + 1][nextWordSearchHeightIndexCopy + 1][nextWordSearchWidthIndexCopy + 1] == 0:
    #                 nextWordSearchDepthIndexCopy += 1
    #                 nextWordSearchHeightIndexCopy += 1
    #                 nextWordSearchWidthIndexCopy += 1
    #             else:
    #                 directionWorks = False
    #                 break
    #         if directionWorks:
    #             addWord(1, 1, 1, nextWordSearchDepthIndex,  nextWordSearchHeightIndex,  nextWordSearchWidthIndex, word, wordSearchInfo)
    #             break

    #     elif direction == "downIn":
    #         for letter in word[1:]:
    #             if nextWordSearchDepthIndexCopy + 1 < wordSearchInfo.wordSearchDepth and nextWordSearchHeightIndexCopy + 1 < wordSearchInfo.wordSearchHeight and wordSearchInfo.wordSearch[nextWordSearchDepthIndexCopy + 1][nextWordSearchHeightIndexCopy + 1][nextWordSearchWidthIndexCopy] == 0:
    #                 nextWordSearchDepthIndexCopy += 1
    #                 nextWordSearchHeightIndexCopy += 1
    #             else:
    #                 directionWorks = False
    #                 break
    #         if directionWorks:
    #             addWord(1, 1, 0, nextWordSearchDepthIndex,  nextWordSearchHeightIndex,  nextWordSearchWidthIndex, word, wordSearchInfo)
    #             break

    #     elif direction == "leftDownIn":
    #         for letter in word[1:]:
    #             if nextWordSearchDepthIndexCopy + 1 < wordSearchInfo.wordSearchDepth and nextWordSearchHeightIndexCopy + 1 < wordSearchInfo.wordSearchHeight and nextWordSearchWidthIndexCopy - 1 >= 0 and wordSearchInfo.wordSearch[nextWordSearchDepthIndexCopy + 1][nextWordSearchHeightIndexCopy + 1][nextWordSearchWidthIndexCopy - 1] == 0:
    #                 nextWordSearchDepthIndexCopy += 1
    #                 nextWordSearchHeightIndexCopy += 1
    #                 nextWordSearchWidthIndexCopy += -1
    #             else:
    #                 directionWorks = False
    #                 break
    #         if directionWorks:
    #             addWord(1, 1, -1, nextWordSearchDepthIndex,  nextWordSearchHeightIndex,  nextWordSearchWidthIndex, word, wordSearchInfo)
    #             break

    #     elif direction == "leftIn":
    #         for letter in word[1:]:
    #             if nextWordSearchDepthIndexCopy + 1 < wordSearchInfo.wordSearchDepth and nextWordSearchWidthIndexCopy - 1 >= 0 and wordSearchInfo.wordSearch[nextWordSearchDepthIndexCopy + 1][nextWordSearchHeightIndexCopy][nextWordSearchWidthIndexCopy - 1] == 0:
    #                 nextWordSearchDepthIndexCopy += 1
    #                 nextWordSearchWidthIndexCopy += -1
    #             else:
    #                 directionWorks = False
    #                 break
    #         if directionWorks:
    #             addWord(1, 0, -1, nextWordSearchDepthIndex,  nextWordSearchHeightIndex,  nextWordSearchWidthIndex, word, wordSearchInfo)
    #             break

    #     elif direction == "leftUpIn":
    #         for letter in word[1:]:
    #             if nextWordSearchDepthIndexCopy + 1 < wordSearchInfo.wordSearchDepth and nextWordSearchHeightIndexCopy - 1 >= 0 and nextWordSearchWidthIndexCopy - 1 >= 0 and wordSearchInfo.wordSearch[nextWordSearchDepthIndexCopy + 1][nextWordSearchHeightIndexCopy - 1][nextWordSearchWidthIndexCopy - 1] == 0:
    #                 nextWordSearchDepthIndexCopy += 1
    #                 nextWordSearchHeightIndexCopy += -1
    #                 nextWordSearchWidthIndexCopy += -1
    #             else:
    #                 directionWorks = False
    #                 break
    #         if directionWorks:
    #             addWord(1, -1, -1, nextWordSearchDepthIndex,  nextWordSearchHeightIndex,  nextWordSearchWidthIndex, word, wordSearchInfo)
    #             break

    #     elif direction == "upIn":
    #         for letter in word[1:]:
    #             if nextWordSearchDepthIndexCopy + 1 < wordSearchInfo.wordSearchDepth and nextWordSearchHeightIndexCopy - 1 >= 0 and wordSearchInfo.wordSearch[nextWordSearchDepthIndexCopy + 1][nextWordSearchHeightIndexCopy - 1][nextWordSearchWidthIndexCopy] == 0:
    #                 nextWordSearchDepthIndexCopy += 1
    #                 nextWordSearchHeightIndexCopy += -1
    #             else:
    #                 directionWorks = False
    #                 break
    #         if directionWorks:
    #             addWord(1, -1, 0, nextWordSearchDepthIndex,  nextWordSearchHeightIndex,  nextWordSearchWidthIndex, word, wordSearchInfo)
    #             break
            
    #     elif direction == "rightUpIn":
    #         for letter in word[1:]:
    #             if nextWordSearchDepthIndexCopy + 1 < wordSearchInfo.wordSearchDepth and nextWordSearchHeightIndexCopy - 1 >= 0 and nextWordSearchWidthIndexCopy + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[nextWordSearchDepthIndexCopy + 1][nextWordSearchHeightIndexCopy - 1][nextWordSearchWidthIndexCopy + 1] == 0:
    #                 nextWordSearchDepthIndexCopy += 1
    #                 nextWordSearchHeightIndexCopy += -1
    #                 nextWordSearchWidthIndexCopy += 1
    #             else:
    #                 directionWorks = False
    #                 break
    #         if directionWorks:
    #             addWord(1, -1, 1, nextWordSearchDepthIndex,  nextWordSearchHeightIndex,  nextWordSearchWidthIndex, word, wordSearchInfo)
    #             break

    # if directionWorks:
    #     print("added ", word, " at position [",nextWordSearchDepthIndex,"][",nextWordSearchHeightIndex,"][",nextWordSearchWidthIndex,"] in the ",direction," direction")
    #     return True
    # else:
    #     return False


if __name__=="__main__":
    main()  
