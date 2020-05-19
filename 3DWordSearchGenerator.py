import random
import math
from WordSearchInfo import WordSearchInfo

# was 449 lines

def main():
    twoDimensional = False # TODO get from front end. depth = 1 == 2D

    print('generating the word search')
    # TODO add the ability to read files from a CLI
    wordSearchGridMultiplier = 2 # the larger this number is, the more likely that every  word gets added
    if wordSearchGridMultiplier < 1:
        print('wordSearchGridMultiplier must be greater than 1')
        return
    with open('WordSearchWords.txt','r+') as wordListFile:
        wordList = [line.rstrip('\n').upper() for line in wordListFile]

    #set up size of wordSeach
    maxWordLength = len(max(wordList, key = len))
    sumOfWordLengths = len(''.join(wordList))
    nearestCube = findNearestCube(sumOfWordLengths)
    wordSearchMinLength = max(maxWordLength, nearestCube) + 1 # done to increase the odds of a succesful createWordSearch() due to a better fitting wordSearch

    # TODO add front end option to pick which directions to allow
    if (twoDimensional):
        directions = ['right', 'rightDown', 'down', 'leftDown', 'left', 'leftUp', 'up', 'rightUp']
        wordSearchDepth = 1
    else:
        directions = ['right', 'rightDown', 'down', 'leftDown', 'left', 'leftUp', 'up', 'rightUp', 'rightOut',
            'rightDownOut', 'downOut', 'leftDownOut', 'leftOut', 'leftUpOut', 'upOut', 'rightUpOut', 'out', 'rightIn',
            'rightDownIn', 'downIn', 'leftDownIn', 'leftIn', 'leftUpIn', 'upIn', 'rightUpIn', 'in']
        wordSearchDepth = random.randint(wordSearchMinLength,(wordSearchGridMultiplier * maxWordLength))

    wordSearchHeight = random.randint(wordSearchMinLength, (wordSearchGridMultiplier * wordSearchMinLength))
    wordSearchWidth = random.randint(wordSearchMinLength, (wordSearchGridMultiplier * wordSearchMinLength))

    wordSearchInfo = WordSearchInfo(wordSearchHeight = wordSearchHeight, wordSearchWidth = wordSearchWidth, 
        wordSearchDepth = wordSearchDepth, wordList = wordList)

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
    with open('WordSearch.txt','w+') as wordSearchFile:     
        wordSearchInfo.printWordSearchToFile(wordSearchFile)
    # TODO convert to JSON


def fillRestOfWordSearch(wordSearchInfo):
    LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for k in range(wordSearchInfo.wordSearchDepth):
        for j in range(wordSearchInfo.wordSearchHeight):
            for i in range(wordSearchInfo.wordSearchWidth):
                if wordSearchInfo.wordSearch[k][j][i] == 'a':
                    randomLetter = random.choice(LETTERS)
                    wordSearchInfo.wordSearch[k][j][i] = randomLetter


def addWord(depthChange, heightChange, widthChange, nextWordSearchDepthIndex, nextWordSearchHeightIndex, nextWordSearchWidthIndex, word, wordSearchInfo):
    for letter in word:
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
            print('there is no place to put the remaining words. Please try again.')
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
    print('words left:',wordList)
    if len(wordList) == 0:
        return True
    return False



def tryWordInDirection(wordSearchInfo, word, direction, startingDepth, startingHeight, startingWidth, depthChange, heightChange, widthChange):
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
            if direction == 'right':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'right',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = 0, widthChange = 1)
                
            elif direction == 'rightDown':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightDown',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = 1, widthChange = 1)

            elif direction == 'down':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightDown',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = 1, widthChange = 0)
                
            elif direction == 'leftDown':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftDown',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = 1, widthChange = -1)

            elif direction == 'left':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'left',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = 0, widthChange = -1)
  
            elif direction == 'leftUp':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftUp',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = -1, widthChange = -1)

            elif direction == 'up':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'up',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = -1, widthChange = 0)

            elif direction == 'rightUp':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightUp',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = -1, widthChange = 1)

        # depth goes out (to the user)
            elif direction == 'rightOut':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightOut',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = 0, widthChange = 1)
                
            elif direction == 'rightDownOut':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightDownOut',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = 1, widthChange = 1)

            elif direction == 'downOut':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightDownOut',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = 1, widthChange = 0)
                
            elif direction == 'leftDownOut':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftDownOut',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = 1, widthChange = -1)

            elif direction == 'leftOut':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftOut',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = 0, widthChange = -1)
  
            elif direction == 'leftUpOut':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftUpOut',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = -1, widthChange = -1)

            elif direction == 'upOut':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'upOut',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = -1, widthChange = 0)

            elif direction == 'rightUpOut':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightUpOut',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = -1, widthChange = 1)

            elif direction == 'out':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'out',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = 0, widthChange = 0)

        #depth goes in (away from user)
            elif direction == 'rightIn':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightIn',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = 0, widthChange = 1)
                
            elif direction == 'rightDownIn':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightDownIn',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = 1, widthChange = 1)

            elif direction == 'downIn':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightDownIn',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = 1, widthChange = 0)
                
            elif direction == 'leftDownIn':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftDownIn',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = 1, widthChange = -1)

            elif direction == 'leftIn':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftIn',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = 0, widthChange = -1)
  
            elif direction == 'leftUpIn':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftUpIn',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = -1, widthChange = -1)

            elif direction == 'upIn':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'upIn',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = -1, widthChange = 0)

            elif direction == 'rightUpIn':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightUpIn',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = -1, widthChange = 1)
            
            elif direction == 'in':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'in',
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = 0, widthChange = 0)
        else:
            break

    if wordAdded:
        print('added ', word, ' at position [', depth, '][', height, '][', width, '] in the ', direction, ' direction')
        return True
    else:
        return False

if __name__=='__main__':
    main()  
