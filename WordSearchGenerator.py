import random
import math
from WordSearchInfo import WordSearchInfo

# TODO are the 2D versions needed? Check if a depth of 1 makes the 2D versions work instead

def main():
    print('generating the word search')
    # TODO add the ability to read files from a CLI
    wordSearchGridMultiplier = 2 # the larger this number is, the more likely that every  word gets added
    if wordSearchGridMultiplier < 1:
        print('wordSearchGridMultiplier must be greater than 1')
        return
    directions = ['right', 'rightDown', 'down', 'leftDown', 'left', 'leftUp', 'up', 'rightUp']
    with open('WordSearchWords.txt','r+') as wordListFile:
        wordList = [line.rstrip('\n').upper() for line in wordListFile]

    # set up size of wordSeach
    maxWordLength = len(max(wordList, key = len))
    sumOfWordLengths = len(''.join(wordList))
    nearestSquare = findNearestSquare(sumOfWordLengths)
    wordSearchMinLength = max(maxWordLength, nearestSquare) + 1 # done to increase the odds of a succesful createWordSearch() due to a better fitting wordSearch
    wordSearchDepth = 1
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
    # with open('WordSearch.txt','w+') as wordSearchFile:     
        # wordSearchInfo.printWordSearchToFile(wordSearchFile)
    # TODO convert to JSON


def fillRestOfWordSearch(wordSearchInfo):
    LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for row in range(wordSearchInfo.wordSearchHeight):
        for col in range(wordSearchInfo.wordSearchWidth):
            if wordSearchInfo.wordSearch[row][col] == 'a':
                randomLetter = random.choice(LETTERS)
                wordSearchInfo.wordSearch[row][col]=randomLetter


def addWord(heightChange, widthChange, nextWordSearchHeightIndex, nextWordSearchWidthIndex, word, wordSearchInfo):
    for letter in word:
        wordSearchInfo.wordSearch[nextWordSearchHeightIndex][nextWordSearchWidthIndex] = letter
        nextOpenSpace = (wordSearchInfo.wordSearchWidth * nextWordSearchHeightIndex) + nextWordSearchWidthIndex
        if nextOpenSpace in wordSearchInfo.openWordSearchSpaces:
            wordSearchInfo.openWordSearchSpaces.remove(nextOpenSpace)
        nextWordSearchHeightIndex += heightChange
        nextWordSearchWidthIndex += widthChange


def getCandidatePosition(wordSearchInfo):
    while True: 
        if len(wordSearchInfo.openWordSearchSpaces) == 0:
            print('there is no place to put the remaining words. Please try again.')
            return -1
        candidatePosition = random.choice(wordSearchInfo.openWordSearchSpaces)
        candidatePositionHeight = candidatePosition // wordSearchInfo.wordSearchWidth
        candidatePositionWidth = candidatePosition % wordSearchInfo.wordSearchWidth
        if wordSearchInfo.wordSearch[candidatePositionHeight][candidatePositionWidth] != 'a':
            wordSearchInfo.openWordSearchSpaces.remove(candidatePosition)
            continue
        return candidatePosition


def findNearestSquare(goal):
    return math.ceil(math.sqrt(goal))


def createWordSearch(wordList, wordSearchInfo, directions):
    wordAdded = False
    candidatePosition = -1
    while len(wordList) > 0 and len(wordSearchInfo.openWordSearchSpaces) > 0:
        candidatePosition = getCandidatePosition(wordSearchInfo)
        if candidatePosition == -1:
            break
        random.shuffle(wordList)
        for word in wordList:
            candidatePositionHeight = candidatePosition // wordSearchInfo.wordSearchWidth
            candidatePositionWidth = candidatePosition % wordSearchInfo.wordSearchWidth
            wordAdded = tryWord(word, candidatePositionHeight, candidatePositionWidth, directions, wordSearchInfo) # TODO depth
            if wordAdded:
                wordList.remove(word)
                break
        if wordAdded == False:
            wordSearchInfo.openWordSearchSpaces.remove(candidatePosition)
    print('words left:', wordList)
    if len(wordList) == 0:
        return True
    return False


# TODO add depth
def tryWordInDirection(wordSearchInfo, word, direction, startingHeight, startingWidth, heightChange, widthChange, startingDepth = -1, depthChange = 0):
    nextWordSearchDepthIndex = startingDepth
    nextWordSearchHeightIndex = startingHeight
    nextWordSearchWidthIndex = startingWidth
    directionWorks = True

    for letter in word[1:]:
        nextSpotExists = wordSearchInfo.directionCheck(direction, nextWordSearchDepthIndex, nextWordSearchHeightIndex, nextWordSearchWidthIndex)
        if nextSpotExists and wordSearchInfo.wordSearch[nextWordSearchHeightIndex + heightChange][nextWordSearchWidthIndex + widthChange] == 'a': # TODO depth
            nextWordSearchDepthIndex += depthChange
            nextWordSearchHeightIndex += heightChange
            nextWordSearchWidthIndex += widthChange
        else:
            directionWorks = False
            break
    if directionWorks:
        addWord(heightChange, widthChange, startingHeight, startingWidth, word, wordSearchInfo) # TODO starting depth
        return True
    return False
    

def tryWord(word, height, width, directions, wordSearchInfo): # TODO depth
    # TODO add a check in try word to see if instead of '0', if the character in wordSearch[height][width] is already the 2nd character of the word. To increase overlap potential
    # get direction to try
    random.shuffle(directions)
    wordAdded = False
    usedDirection = None

    for direction in directions:
        if not wordAdded:
            usedDirection = direction

            if direction == 'right':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'right',
                    startingHeight = height, startingWidth = width, heightChange = 0, widthChange = 1)

            elif direction == 'rightDown':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightDown',
                    startingHeight = height, startingWidth = width, heightChange = 1, widthChange = 1)

            elif direction == 'down':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'down',
                    startingHeight = height, startingWidth = width, heightChange = 1, widthChange = 0)

            elif direction == 'leftDown':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftDown',
                    startingHeight = height, startingWidth = width, heightChange = 1, widthChange = -1)

            elif direction == 'left':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'left',
                    startingHeight = height, startingWidth = width, heightChange = 0, widthChange = -1)

            elif direction == 'leftUp':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftUp',
                    startingHeight = height, startingWidth = width, heightChange = -1, widthChange = -1)

            elif direction == 'up':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'up',
                    startingHeight = height, startingWidth = width, heightChange = -1, widthChange = 0)

            elif direction == 'rightUp':
                wordAdded = tryWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightUp',
                    startingHeight = height, startingWidth = width, heightChange = -1, widthChange = 1)
        else:
            break

    if wordAdded:
        print('added ', word, ' at position [', height, '][', width, '] in the ', usedDirection, ' direction')
        return True
    else:
        return False

if __name__=='__main__':
    main()  
