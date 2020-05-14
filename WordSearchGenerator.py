import random
import math
from WordSearchInfo import WordSearchInfo

# TODO are teh 2D versions needed? Check if a depth of 1 makes the 2D versions work instead

def main():
    print('generating the word search')
    # TODO add the ability to read files from a CLI
    wordSearchGridMultiplier = 2 # the larger this number is, the more likely that every  word gets added
    if wordSearchGridMultiplier < 1:
        print('wordSearchGridMultiplier must be greater than 1')
        return
    directions = ['right', 'rightDown', 'down', 'leftDown', 'left', 'leftUp', 'up', 'rightUp']
    wordListFile = open('WordSearchWords.txt','r+')
    wordSearchFile = open('WordSearch.txt','w+')
    wordList = [line.rstrip('\n').upper() for line in wordListFile]
    wordListFile.close()

    # set up size of wordSeach
    maxWordLength = len(max(wordList, key = len))
    sumOfWordLengths = len(''.join(wordList))
    nearestSquare = findNearestSquare(sumOfWordLengths)
    wordSearchMinLength = max(maxWordLength, nearestSquare) + 1 # done to increase the odds of a succesful createWordSearch() due to a better fitting wordSearch
    print('maxWordLength:', maxWordLength, ', sumOfWordLengths:', sumOfWordLengths, ', nearestSquare:', nearestSquare, ', wordSearchMinLength:', wordSearchMinLength)
    wordSearchDepth = 1
    wordSearchHeight = random.randint(wordSearchMinLength, (wordSearchGridMultiplier * wordSearchMinLength))
    wordSearchWidth = random.randint(wordSearchMinLength, (wordSearchGridMultiplier * wordSearchMinLength))
    print('wordSearchDepth:', wordSearchDepth, 'wordSearchHeight:', wordSearchHeight, ', wordSearchWidth:', wordSearchWidth)

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
    # wordSearchInfo.printWordSearchToFile(wordSearchFile)
    wordSearchFile.close()
    # TODO convert to JSON


def fillRestOfWordSearch(wordSearchInfo):
    LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for row in range(wordSearchInfo.wordSearchHeight):
        for col in range(wordSearchInfo.wordSearchWidth):
            if wordSearchInfo.wordSearch[row][col] == 'a':
                randomLetter = random.choice(LETTERS)
                wordSearchInfo.wordSearch[row][col]=randomLetter


def addWord(heightChange, widthChange, nextWordSearchHeightIndex, nextWordSearchWidthIndex, word, wordSearchInfo):
    # dont need to check if the space exists in wordSearch, as tryWord does that
    for letter in word: # add the word to the word Search
        wordSearchInfo.wordSearch[nextWordSearchHeightIndex][nextWordSearchWidthIndex] = letter # update the correct spot in wordSearch
        nextOpenSpace = (wordSearchInfo.wordSearchWidth * nextWordSearchHeightIndex) + nextWordSearchWidthIndex # remove said spot from openWordSearchSpaces
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
        # print(candidatePosition, candidatePositionHeight, candidatePositionWidth)
        # wordSearchInfo.toString()
        if wordSearchInfo.wordSearch[candidatePositionHeight][candidatePositionWidth] != 'a':
            wordSearchInfo.openWordSearchSpaces.remove(candidatePosition)
            continue
        return candidatePosition


def findNearestSquare(goal):
    # i = 1
    # while i * i < goal:
    #     i += 1
    # return i
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


# # TODO add depth
# def tryWordInDirection(wordSearchInfo, word, direction, startingHeight, startingWidth, heightChange, widthChange, startingDepth = -1, depthChange = 0):
#     nextWordSearchDepthIndex = startingDepth
#     nextWordSearchHeightIndex = startingHeight
#     nextWordSearchWidthIndex = startingWidth
#     directionWorks = True

#     for letter in word[1:]:
#         if directionCheck(wordSearchInfo, direction, nextWordSearchDepthIndex, nextWordSearchHeightIndex, nextWordSearchWidthIndex) and wordSearchInfo.wordSearch[nextWordSearchHeightIndex + heightChange][nextWordSearchWidthIndex + widthChange] == 0: ## TODO depth
#             nextWordSearchDepthIndex += depthChange
#             nextWordSearchHeightIndex += heightChange
#             nextWordSearchWidthIndex += widthChange
#         else:
#             directionWorks = False
#             break
#     if directionWorks:
#         addWord(heightChange, widthChange, startingHeight, startingWidth, word, wordSearchInfo) # TODO starting depth
#         return True
#     return False
    

def tryWord(word, height, width, directions, wordSearchInfo): # TODO depth
    # TODO add a check in try word to see if instead of '0', if the character in wordSearch[height][width] is already the 2nd character of the word. To increase overlap potential
    # candidatePositionHeight = candidatePosition // wordSearchInfo.wordSearchWidth
    # candidatePositionWidth = candidatePosition % wordSearchInfo.wordSearchWidth
    
    candidatePositionHeight = height
    candidatePositionWidth = width

    # get direction to try
    random.shuffle(directions)
    directionWorks = True
    for direction in directions:
        directionWorks = True

        # TODO remove
        candidatePositionHeightCopy = candidatePositionHeight
        candidatePositionWidthCopy = candidatePositionWidth

        if direction == 'right':
            # wordSearchInfo.tryWordInDirection(word = word, direction = 'right',
            #         startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = 0, widthChange = 1)


            for letter in word[1:]:
                if candidatePositionWidthCopy + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[candidatePositionHeightCopy][candidatePositionWidthCopy + 1] == 'a':
                    candidatePositionWidthCopy += 1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(0, 1, candidatePositionHeight, candidatePositionWidth, word, wordSearchInfo)
                break
                    
        elif direction == 'rightDown':
            for letter in word[1:]:
                if candidatePositionHeightCopy + 1 < wordSearchInfo.wordSearchHeight and candidatePositionWidthCopy + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[candidatePositionHeightCopy + 1][candidatePositionWidthCopy + 1] == 'a':
                    candidatePositionHeightCopy += 1
                    candidatePositionWidthCopy += 1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(1, 1, candidatePositionHeight, candidatePositionWidth, word, wordSearchInfo)
                break

        elif direction == 'down':
            for letter in word[1:]:
                if candidatePositionHeightCopy + 1 < wordSearchInfo.wordSearchHeight and wordSearchInfo.wordSearch[candidatePositionHeightCopy + 1][candidatePositionWidthCopy] == 'a':
                    candidatePositionHeightCopy += 1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(1, 0, candidatePositionHeight, candidatePositionWidth, word, wordSearchInfo)
                break

        elif direction == 'leftDown':
            for letter in word[1:]:
                if candidatePositionHeightCopy + 1 < wordSearchInfo.wordSearchHeight and candidatePositionWidthCopy - 1 >= 0 and wordSearchInfo.wordSearch[candidatePositionHeightCopy + 1][candidatePositionWidthCopy - 1] == 'a':
                    candidatePositionHeightCopy += 1
                    candidatePositionWidthCopy += -1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(1, -1, candidatePositionHeight, candidatePositionWidth, word, wordSearchInfo)
                break

        elif direction == 'left':
            for letter in word[1:]:
                if candidatePositionWidthCopy - 1 >= 0 and wordSearchInfo.wordSearch[candidatePositionHeightCopy][candidatePositionWidthCopy - 1] == 'a':
                    candidatePositionWidthCopy += -1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(0, -1, candidatePositionHeight, candidatePositionWidth, word, wordSearchInfo)
                break

        elif direction == 'leftUp':
            for letter in word[1:]:
                if candidatePositionHeightCopy - 1 >= 0 and candidatePositionWidthCopy - 1 >=0 and wordSearchInfo.wordSearch[candidatePositionHeightCopy - 1][candidatePositionWidthCopy - 1] == 'a':
                    candidatePositionHeightCopy += -1
                    candidatePositionWidthCopy += -1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(-1, -1, candidatePositionHeight, candidatePositionWidth, word, wordSearchInfo)
                break

        elif direction == 'up':
            for letter in word[1:]:
                if candidatePositionHeightCopy - 1 >= 0 and wordSearchInfo.wordSearch[candidatePositionHeightCopy - 1][candidatePositionWidthCopy] == 'a':
                    candidatePositionHeightCopy += -1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(-1, 0, candidatePositionHeight, candidatePositionWidth, word, wordSearchInfo)
                break
            
        elif direction == 'rightUp':
            for letter in word[1:]:
                if candidatePositionHeightCopy - 1 >= 0 and candidatePositionWidthCopy + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[candidatePositionHeightCopy - 1][candidatePositionWidthCopy + 1] == 'a':
                    candidatePositionHeightCopy += -1
                    candidatePositionWidthCopy += 1
                else:
                    directionWorks = False
                    break
            if directionWorks:
                addWord(-1, 1, candidatePositionHeight, candidatePositionWidth, word, wordSearchInfo)
                break

    if directionWorks:
        print('added ', word, ' at position [', candidatePositionHeight, '][', candidatePositionWidth, '] in the ', direction, ' direction')
        return True
    else:
        return False

if __name__=='__main__':
    main()  
