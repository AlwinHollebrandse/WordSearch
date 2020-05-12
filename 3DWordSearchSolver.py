import numpy as np 
from WordSearchInfo import WordSearchInfo


def main(): 
    print('solving the word search')

    direction = 'error'
    wordListFile = open('WordSearchWords.txt','r') # TODO change to some random default or frontend provided
    wordSearchFile = open('WordSearch.txt','r') # TODO change to json object
    wordList = [line.rstrip('\n').upper() for line in wordListFile]
    wordSearch = parse3DWordSearchFromFile(wordSearchFile) # TODO read from json object too

    wordSearchDepth = len(wordSearch)
    wordSearchHeight = len(wordSearch[0])
    wordSearchWidth = len(wordSearch[0][0])
    wordSearchInfo = WordSearchInfo(wordSearchHeight = wordSearchHeight, wordSearchWidth = wordSearchWidth, 
        wordSearchDepth = wordSearchDepth, wordList = wordList, wordSearch = wordSearch)
    wordSearchInfo.toString()

    foundWordSet = set([])
    # TODO parallelize
    for depth in range(len(wordSearch)):
        for height in range(len(wordSearch[depth])):
            for width in range(len(wordSearch[depth][height])):
               # print("d:", depth, ", h:", height, ", w:", width, ", Value:", wordSearchInfo.wordSearch[depth][height][width])
                checkForWord(depth, height, width, wordSearchInfo, wordList, foundWordSet)  
    print('words not found:', list(set(wordList) - foundWordSet))


def parse3DWordSearchFromFile(wordSearchFile):
    wordSearch3DIn2D = [[letter for letter in line.split()] for line in wordSearchFile] # wordSearch3DIn2D has the right characters, but wrong dimensions, which is why the rest is needed
    print(wordSearch3DIn2D)
    height = find3DWordSearchHeight(wordSearch3DIn2D) 
    width = find3DWordSearchWidth(wordSearch3DIn2D)
    totalNumberOfLines = getTotalNumberOfWordSearchFileLines(wordSearch3DIn2D)
    depth = totalNumberOfLines // (height + 2) # NOTE the 2 is from the double blank lines that seperates sections of the 3D word search
    print("d:", depth, ", h:", height, ", w:", width, "total:", totalNumberOfLines)

    wordSearch = np.array([[[0 for _ in range(width)] for _ in range(height)] for _ in range(depth)])
    wordSearch3DIn2DHeight = 0
    wordSearch3DIn2DWidth = 0
    for k in range(depth):
        for j in range(height):
            for i in range(width):
                wordSearch[k][j][i] = wordSearch3DIn2D[wordSearch3DIn2DHeight][wordSearch3DIn2DWidth]

                if wordSearch3DIn2DWidth == width - 1:
                    if wordSearch3DIn2D[wordSearch3DIn2DHeight + 1] == []:
                        wordSearch3DIn2DHeight += 3
                    else:
                        wordSearch3DIn2DHeight += 1
                    wordSearch3DIn2DWidth = -1
                wordSearch3DIn2DWidth += 1

    return wordSearch


# finds the height of each layer in the wordSearch by incrementing a counter until the first "layer break" is encountered
def find3DWordSearchHeight(wordSearch3DIn2D):
    height = 0
    for line in wordSearch3DIn2D:
        if line:
            height += 1
        else:
            break
    return height


def find3DWordSearchWidth(wordSearch3DIn2D):
    for line in wordSearch3DIn2D:
        return len(line)


def getTotalNumberOfWordSearchFileLines(wordSearch3DIn2D):
    return len(wordSearch3DIn2D)


def checkForWord(depth, height, width, wordSearchInfo, wordList, foundWordSet):
    for word in reversed(wordList): # for each word in the wordList, itereted backwards so that things can be popped cleanly  
        directionsFoundIn = []
        foundWord = False

        if wordSearchInfo.wordSearch[depth][height][width] == wordList[word][0]:      

# NOTE the following direction checks are for when the depth remains the same
            # check the right direction
            if width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth][height][width + 1] == wordList[word][1]:
                wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'right', directionsFoundIn = directionsFoundIn, 
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = 0, widthChange = 1)

            # check the right, down direction
            if height + 1 < wordSearchInfo.wordSearchHeight and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth][height + 1][width + 1] == wordList[word][1]:
                wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'rightDown', directionsFoundIn = directionsFoundIn, 
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = 1, widthChange = 1)

            # check the down direction
            if height + 1 < wordSearchInfo.wordSearchHeight and wordSearchInfo.wordSearch[depth][height + 1][width] == wordList[word][1]:
                wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'down', directionsFoundIn = directionsFoundIn, 
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = 1, widthChange = 0)

            # check the left, down direction
            if height + 1 < wordSearchInfo.wordSearchHeight and width - 1 >= 0 and wordSearchInfo.wordSearch[depth][height + 1][width - 1] == wordList[word][1]:
                wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'leftDown', directionsFoundIn = directionsFoundIn, 
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = 1, widthChange = -1)

            # check the left direction
            if width - 1 >= 0 and wordSearchInfo.wordSearch[depth][height][width - 1] == wordList[word][1]:
                wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'left', directionsFoundIn = directionsFoundIn, 
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = 0, widthChange = -1)

            # check the left up direction
            if height - 1 >= 0 and width - 1 >= 0 and wordSearchInfo.wordSearch[depth][height - 1][width - 1] == wordList[word][1]:
                wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'leftUp', directionsFoundIn = directionsFoundIn, 
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = -1, widthChange = -1)

            # check the up direction
            if height - 1 >= 0 and wordSearchInfo.wordSearch[depth][height - 1][width] == wordList[word][1]:
                wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'up', directionsFoundIn = directionsFoundIn, 
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = -1, widthChange = 0)

            # check the right, up direction
            if height - 1 >= 0 and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth][height - 1][width + 1] == wordList[word][1]:
                wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'rightUp', directionsFoundIn = directionsFoundIn, 
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = -1, widthChange = 1)

        # NOTE the following direction checks are for when the depth goes out (to the user)
            # check the right direction
            if depth - 1 >= 0 and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth - 1][height][width + 1] == wordList[word][1]:
                wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'rightOut', directionsFoundIn = directionsFoundIn, 
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = 0, widthChange = 1)

            # check the right, down direction
            if depth - 1 >= 0 and height + 1 < wordSearchInfo.wordSearchHeight and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth - 1][height + 1][width + 1] == wordList[word][1]:
                wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'rightDownOut', directionsFoundIn = directionsFoundIn, 
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = 1, widthChange = 1)

            # check the down direction
            if depth - 1 >= 0 and height + 1 < wordSearchInfo.wordSearchHeight and wordSearchInfo.wordSearch[depth - 1][height + 1][width] == wordList[word][1]:
                wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'downOut', directionsFoundIn = directionsFoundIn, 
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = 1, widthChange = 0)

            # check the left, down direction
            if depth - 1 >= 0 and height + 1 < wordSearchInfo.wordSearchHeight and width - 1 >= 0 and wordSearchInfo.wordSearch[depth - 1][height + 1][width - 1] == wordList[word][1]:
                wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'leftDownOut', directionsFoundIn = directionsFoundIn, 
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = 1, widthChange = -1)

            # check the left direction
            if depth - 1 >= 0 and  width - 1 >= 0 and wordSearchInfo.wordSearch[depth - 1][height][width - 1] == wordList[word][1]:
                wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'leftOut', directionsFoundIn = directionsFoundIn, 
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = 0, widthChange = -1)

            # check the left up direction
            if depth - 1 >= 0 and  height - 1 >= 0 and width - 1 >= 0 and wordSearchInfo.wordSearch[depth - 1][height - 1][width - 1] == wordList[word][1]:
                wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'leftUpOut', directionsFoundIn = directionsFoundIn, 
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = -1, widthChange = -1)

            # check the up direction
            if depth - 1 >= 0 and  height - 1 >= 0 and wordSearchInfo.wordSearch[depth - 1][height - 1][width] == wordList[word][1]:
                wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'upOut', directionsFoundIn = directionsFoundIn, 
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = -1, widthChange = 0)

            # check the right, up direction
            if depth - 1 >= 0 and height - 1 >= 0 and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth - 1][height - 1][width + 1] == wordList[word][1]:
                wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'rightUpOut', directionsFoundIn = directionsFoundIn, 
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = -1, widthChange = 1)

        # NOTE the following direction checks are for when the depth goes in (away from the user)
            # check the right direction
            if depth + 1 < wordSearchInfo.wordSearchDepth and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth + 1][height][width + 1] == wordList[word][1]:
                wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'rightIn', directionsFoundIn = directionsFoundIn, 
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = 0, widthChange = 1)
            
            # check the right, down direction
            if depth + 1 < wordSearchInfo.wordSearchDepth and height + 1 < wordSearchInfo.wordSearchHeight and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth + 1][height + 1][width + 1] == wordList[word][1]:
                wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'rightDownIn', directionsFoundIn = directionsFoundIn, 
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = 1, widthChange = 1)

            # check the down direction
            if depth + 1 < wordSearchInfo.wordSearchDepth and height + 1 < wordSearchInfo.wordSearchHeight and wordSearchInfo.wordSearch[depth + 1][height + 1][width] == wordList[word][1]:
                wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'downIn', directionsFoundIn = directionsFoundIn, 
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = 1, widthChange = 0)

            # check the left, down direction
            if depth + 1 < wordSearchInfo.wordSearchDepth and height + 1 < wordSearchInfo.wordSearchHeight and width - 1 >= 0 and wordSearchInfo.wordSearch[depth + 1][height + 1][width - 1] == wordList[word][1]:
                wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'leftDownIn', directionsFoundIn = directionsFoundIn, 
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = 1, widthChange = -1)

            # check the left direction
            if depth + 1 < wordSearchInfo.wordSearchDepth and  width - 1 >= 0 and wordSearchInfo.wordSearch[depth + 1][height][width - 1] == wordList[word][1]:
                wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'leftIn', directionsFoundIn = directionsFoundIn, 
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = 0, widthChange = -1)

            # check the left up direction
            if depth + 1 < wordSearchInfo.wordSearchDepth and  height - 1 >= 0 and width - 1 >= 0 and wordSearchInfo.wordSearch[depth + 1][height - 1][width - 1] == wordList[word][1]:
                wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'leftUpIn', directionsFoundIn = directionsFoundIn, 
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = -1, widthChange = -1)

            # check the up direction
            if depth + 1 < wordSearchInfo.wordSearchDepth and  height - 1 >= 0 and wordSearchInfo.wordSearch[depth + 1][height - 1][width] == wordList[word][1]:
                wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'upIn', directionsFoundIn = directionsFoundIn, 
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = -1, widthChange = 0)

            # check the right, up direction
            if depth + 1 < wordSearchInfo.wordSearchDepth and height - 1 >= 0 and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth + 1][height - 1][width + 1] == wordList[word][1]:
                wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'rightUpIn', directionsFoundIn = directionsFoundIn, 
                    startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = -1, widthChange = 1)








        # # NOTE the following direction checks are for when the depth remains the same
        #     # check the right direction
        #     if width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth][height][width + 1] == wordList[word][1]:
        #         wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'right', directionsFoundIn = directionsFoundIn, 
        #             startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = 0, widthChange = 1) 

        #         nextWordSearchWidthIndex = width
        #         for letter in range(len(wordList[word])):
        #             if wordSearchInfo.wordSearch[depth][height][nextWordSearchWidthIndex] == wordList[word][letter]:
        #                 foundWord = True
        #                 direction = "right"
        #             else:
        #                 foundWord = False
        #                 break
        #             if nextWordSearchWidthIndex + 1 < wordSearchInfo.wordSearchWidth:
        #                 nextWordSearchWidthIndex += 1
            
        #     # check the right, down direction
        #     if height + 1 < wordSearchInfo.wordSearchHeight and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth][height + 1][width + 1] == wordList[word][1]:
        #         nextWordSearchWidthIndex = width
        #         nextWordSearchHeightIndex = height
        #         for letter in range(len(wordList[word])):
        #             if wordSearchInfo.wordSearch[depth][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
        #                 foundWord = True
        #                 direction = "rightDown"
        #             else:
        #                 foundWord = False
        #                 break
        #             if nextWordSearchHeightIndex + 1 < wordSearchInfo.wordSearchHeight and nextWordSearchWidthIndex + 1 < wordSearchInfo.wordSearchWidth:
        #                 nextWordSearchWidthIndex += 1
        #                 nextWordSearchHeightIndex += 1

        #     # check the down direction
        #     if height + 1 < wordSearchInfo.wordSearchHeight and wordSearchInfo.wordSearch[depth][height + 1][width] == wordList[word][1]:
        #         nextWordSearchHeightIndex = height
        #         for letter in range(len(wordList[word])):
        #             if wordSearchInfo.wordSearch[depth][nextWordSearchHeightIndex][width] == wordList[word][letter]:
        #                 foundWord = True
        #                 direction = "down"
        #             else:
        #                 foundWord = False
        #                 break
        #             if nextWordSearchHeightIndex + 1 < wordSearchInfo.wordSearchHeight:
        #                 nextWordSearchHeightIndex += 1

        #     # check the left, down direction
        #     if height + 1 < wordSearchInfo.wordSearchHeight and width - 1 >= 0 and wordSearchInfo.wordSearch[depth][height + 1][width - 1] == wordList[word][1]:
        #         nextWordSearchWidthIndex = width
        #         nextWordSearchHeightIndex = height
        #         for letter in range(len(wordList[word])):
        #             if wordSearchInfo.wordSearch[depth][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
        #                 foundWord = True
        #                 direction = "leftDown"
        #             else:
        #                 foundWord = False
        #                 break
        #             if nextWordSearchHeightIndex + 1 < wordSearchInfo.wordSearchHeight and nextWordSearchWidthIndex - 1 >= 0:
        #                 nextWordSearchWidthIndex -= 1
        #                 nextWordSearchHeightIndex += 1

        #     # check the left direction
        #     if width - 1 >= 0 and wordSearchInfo.wordSearch[depth][height][width - 1] == wordList[word][1]:
        #         nextWordSearchWidthIndex = width
        #         for letter in range(len(wordList[word])):
        #             if wordSearchInfo.wordSearch[depth][height][nextWordSearchWidthIndex] == wordList[word][letter]:
        #                 foundWord = True
        #                 direction = "left"
        #             else:
        #                 foundWord = False
        #                 break
        #             if nextWordSearchWidthIndex - 1 >= 0:
        #                 nextWordSearchWidthIndex -= 1

        #     # check the left up direction
        #     if height - 1 >= 0 and width - 1 >= 0 and wordSearchInfo.wordSearch[depth][height - 1][width - 1] == wordList[word][1]:
        #         nextWordSearchWidthIndex = width
        #         nextWordSearchHeightIndex = height
        #         for letter in range(len(wordList[word])):
        #             if wordSearchInfo.wordSearch[depth][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
        #                 foundWord = True
        #                 direction = "leftUp"
        #             else:
        #                 foundWord = False
        #                 break
        #             if nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex - 1 >= 0:
        #                 nextWordSearchWidthIndex -= 1
        #                 nextWordSearchHeightIndex -= 1

        #     # check the up direction
        #     if height - 1 >= 0 and wordSearchInfo.wordSearch[depth][height - 1][width] == wordList[word][1]:
        #         nextWordSearchHeightIndex = height
        #         for letter in range(len(wordList[word])):
        #             if wordSearchInfo.wordSearch[depth][nextWordSearchHeightIndex][width] == wordList[word][letter]:
        #                 foundWord = True
        #                 direction = "up"
        #             else:
        #                 foundWord = False
        #                 break
        #             if nextWordSearchHeightIndex - 1 >= 0:
        #                 nextWordSearchHeightIndex -= 1

        #     # check the right, up direction
        #     if height - 1 >= 0 and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth][height - 1][width + 1] == wordList[word][1]:
        #         nextWordSearchWidthIndex = width
        #         nextWordSearchHeightIndex = height
        #         for letter in range(len(wordList[word])):
        #             if wordSearchInfo.wordSearch[depth][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
        #                 foundWord = True
        #                 direction = "rightUp"
        #             else:
        #                 foundWord = False
        #                 break
        #             if nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex + 1 < wordSearchInfo.wordSearchWidth:
        #                 nextWordSearchWidthIndex += 1
        #                 nextWordSearchHeightIndex -= 1

        # # NOTE the following direction checks are for when the depth goes out (to the user)
        #     # check the right direction
        #     if depth - 1 >= 0 and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth - 1][height][width + 1] == wordList[word][1]:
        #         nextWordSearchDepthIndex = depth
        #         nextWordSearchWidthIndex = width
        #         for letter in range(len(wordList[word])):
        #             if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][height][nextWordSearchWidthIndex] == wordList[word][letter]:
        #                 foundWord = True
        #                 direction = "rightOut"
        #             else:
        #                 foundWord = False
        #                 break
        #             if depth - 1 >= 0 and nextWordSearchWidthIndex + 1 < wordSearchInfo.wordSearchWidth:
        #                 nextWordSearchDepthIndex += -1
        #                 nextWordSearchWidthIndex += 1
            
        #     # check the right, down direction
        #     if depth - 1 >= 0 and height + 1 < wordSearchInfo.wordSearchHeight and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth - 1][height + 1][width + 1] == wordList[word][1]:
        #         nextWordSearchDepthIndex = depth
        #         nextWordSearchWidthIndex = width
        #         nextWordSearchHeightIndex = height
        #         for letter in range(len(wordList[word])):
        #             if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
        #                 foundWord = True
        #                 direction = "rightDownOut"
        #             else:
        #                 foundWord = False
        #                 break
        #             if depth - 1 >= 0 and nextWordSearchHeightIndex + 1 < wordSearchInfo.wordSearchHeight and nextWordSearchWidthIndex + 1 < wordSearchInfo.wordSearchWidth:
        #                 nextWordSearchDepthIndex += -1
        #                 nextWordSearchWidthIndex += 1
        #                 nextWordSearchHeightIndex += 1

        #     # check the down direction
        #     if depth - 1 >= 0 and height + 1 < wordSearchInfo.wordSearchHeight and wordSearchInfo.wordSearch[depth - 1][height + 1][width] == wordList[word][1]:
        #         nextWordSearchDepthIndex = depth
        #         nextWordSearchHeightIndex = height
        #         for letter in range(len(wordList[word])):
        #             if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][width] == wordList[word][letter]:
        #                 foundWord = True
        #                 direction = "downOut"
        #             else:
        #                 foundWord = False
        #                 break
        #             if depth - 1 >= 0 and nextWordSearchHeightIndex + 1 < wordSearchInfo.wordSearchHeight:
        #                 nextWordSearchDepthIndex += -1
        #                 nextWordSearchHeightIndex += 1

        #     # check the left, down direction
        #     if depth - 1 >= 0 and height + 1 < wordSearchInfo.wordSearchHeight and width - 1 >= 0 and wordSearchInfo.wordSearch[depth - 1][height + 1][width - 1] == wordList[word][1]:
        #         nextWordSearchDepthIndex = depth
        #         nextWordSearchWidthIndex = width
        #         nextWordSearchHeightIndex = height
        #         for letter in range(len(wordList[word])):
        #             if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
        #                 foundWord = True
        #                 direction = "leftDownOut"
        #             else:
        #                 foundWord = False
        #                 break
        #             if depth - 1 >= 0 and nextWordSearchHeightIndex + 1 < wordSearchInfo.wordSearchHeight and nextWordSearchWidthIndex - 1 >= 0:
        #                 nextWordSearchDepthIndex += -1
        #                 nextWordSearchWidthIndex -= 1
        #                 nextWordSearchHeightIndex += 1

        #     # check the left direction
        #     if depth - 1 >= 0 and  width - 1 >= 0 and wordSearchInfo.wordSearch[depth - 1][height][width - 1] == wordList[word][1]:
        #         nextWordSearchDepthIndex = depth
        #         nextWordSearchWidthIndex = width
        #         for letter in range(len(wordList[word])):
        #             if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][height][nextWordSearchWidthIndex] == wordList[word][letter]:
        #                 foundWord = True
        #                 direction = "leftOut"
        #             else:
        #                 foundWord = False
        #                 break
        #             if depth - 1 >= 0 and nextWordSearchWidthIndex - 1 >= 0:
        #                 nextWordSearchDepthIndex += -1
        #                 nextWordSearchWidthIndex -= 1

        #     # check the left up direction
        #     if depth - 1 >= 0 and  height - 1 >= 0 and width - 1 >= 0 and wordSearchInfo.wordSearch[depth - 1][height - 1][width - 1] == wordList[word][1]:
        #         nextWordSearchDepthIndex = depth
        #         nextWordSearchWidthIndex = width
        #         nextWordSearchHeightIndex = height
        #         for letter in range(len(wordList[word])):
        #             if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
        #                 foundWord = True
        #                 direction = "leftUpOut"
        #             else:
        #                 foundWord = False
        #                 break
        #             if depth - 1 >= 0 and nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex - 1 >= 0:
        #                 nextWordSearchDepthIndex += -1
        #                 nextWordSearchWidthIndex -= 1
        #                 nextWordSearchHeightIndex -= 1

        #     # check the up direction
        #     if depth - 1 >= 0 and  height - 1 >= 0 and wordSearchInfo.wordSearch[depth - 1][height - 1][width] == wordList[word][1]:
        #         nextWordSearchDepthIndex = depth
        #         nextWordSearchHeightIndex = height
        #         for letter in range(len(wordList[word])):
        #             if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][width] == wordList[word][letter]:
        #                 foundWord = True
        #                 direction = "upOut"
        #             else:
        #                 foundWord = False
        #                 break
        #             if depth - 1 >= 0 and nextWordSearchHeightIndex - 1 >= 0:
        #                 nextWordSearchDepthIndex += -1
        #                 nextWordSearchHeightIndex -= 1

        #     # check the right, up direction
        #     if depth - 1 >= 0 and height - 1 >= 0 and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth - 1][height - 1][width + 1] == wordList[word][1]:
        #         nextWordSearchDepthIndex = depth
        #         nextWordSearchWidthIndex = width
        #         nextWordSearchHeightIndex = height
        #         for letter in range(len(wordList[word])):
        #             if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
        #                 foundWord = True
        #                 direction = "rightUpOut"
        #             else:
        #                 foundWord = False
        #                 break
        #             if depth - 1 >= 0 and nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex + 1 < wordSearchInfo.wordSearchWidth: # TODO shouldnt these depths be nextWordSearchDepthIndex?
        #                 nextWordSearchDepthIndex += -1
        #                 nextWordSearchWidthIndex += 1
        #                 nextWordSearchHeightIndex -= 1

        # # NOTE the following direction checks are for when the depth goes in (away from the user)
        #     # check the right direction
        #     if depth + 1 < wordSearchInfo.wordSearchDepth and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth + 1][height][width + 1] == wordList[word][1]:
        #         nextWordSearchDepthIndex = depth
        #         nextWordSearchWidthIndex = width
        #         for letter in range(len(wordList[word])):
        #             if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][height][nextWordSearchWidthIndex] == wordList[word][letter]:
        #                 foundWord = True
        #                 direction = "rightIn"
        #             else:
        #                 foundWord = False
        #                 break
        #             if nextWordSearchDepthIndex + 1 < wordSearchInfo.wordSearchDepth and nextWordSearchWidthIndex + 1 < wordSearchInfo.wordSearchWidth:
        #                 nextWordSearchDepthIndex += 1
        #                 nextWordSearchWidthIndex += 1
            
        #     # check the right, down direction
        #     if depth + 1 < wordSearchInfo.wordSearchDepth and height + 1 < wordSearchInfo.wordSearchHeight and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth + 1][height + 1][width + 1] == wordList[word][1]:
        #         nextWordSearchDepthIndex = depth
        #         nextWordSearchWidthIndex = width
        #         nextWordSearchHeightIndex = height
        #         for letter in range(len(wordList[word])):
        #             if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
        #                 foundWord = True
        #                 direction = "rightDownIn"
        #             else:
        #                 foundWord = False
        #                 break
        #             if nextWordSearchDepthIndex + 1 < wordSearchInfo.wordSearchDepth and nextWordSearchHeightIndex + 1 < wordSearchInfo.wordSearchHeight and nextWordSearchWidthIndex + 1 < wordSearchInfo.wordSearchWidth:
        #                 nextWordSearchDepthIndex += 1
        #                 nextWordSearchWidthIndex += 1
        #                 nextWordSearchHeightIndex += 1

        #     # check the down direction
        #     if depth + 1 < wordSearchInfo.wordSearchDepth and height + 1 < wordSearchInfo.wordSearchHeight and wordSearchInfo.wordSearch[depth + 1][height + 1][width] == wordList[word][1]:
        #         nextWordSearchDepthIndex = depth
        #         nextWordSearchHeightIndex = height
        #         for letter in range(len(wordList[word])):
        #             if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][width] == wordList[word][letter]:
        #                 foundWord = True
        #                 direction = "downIn"
        #             else:
        #                 foundWord = False
        #                 break
        #             if nextWordSearchDepthIndex + 1 < wordSearchInfo.wordSearchDepth and nextWordSearchHeightIndex + 1 < wordSearchInfo.wordSearchHeight:
        #                 nextWordSearchDepthIndex += 1
        #                 nextWordSearchHeightIndex += 1

        #     # check the left, down direction
        #     if depth + 1 < wordSearchInfo.wordSearchDepth and height + 1 < wordSearchInfo.wordSearchHeight and width - 1 >= 0 and wordSearchInfo.wordSearch[depth + 1][height + 1][width - 1] == wordList[word][1]:
        #         nextWordSearchDepthIndex = depth
        #         nextWordSearchWidthIndex = width
        #         nextWordSearchHeightIndex = height
        #         for letter in range(len(wordList[word])):
        #             if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
        #                 foundWord = True
        #                 direction = "leftDownIn"
        #             else:
        #                 foundWord = False
        #                 break
        #             if nextWordSearchDepthIndex + 1 < wordSearchInfo.wordSearchDepth and nextWordSearchHeightIndex + 1 < wordSearchInfo.wordSearchHeight and nextWordSearchWidthIndex - 1 >= 0:
        #                 nextWordSearchDepthIndex += 1
        #                 nextWordSearchWidthIndex -= 1
        #                 nextWordSearchHeightIndex += 1

        #     # check the left direction
        #     if depth + 1 < wordSearchInfo.wordSearchDepth and  width - 1 >= 0 and wordSearchInfo.wordSearch[depth + 1][height][width - 1] == wordList[word][1]:
        #         nextWordSearchDepthIndex = depth
        #         nextWordSearchWidthIndex = width
        #         for letter in range(len(wordList[word])):
        #             if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][height][nextWordSearchWidthIndex] == wordList[word][letter]:
        #                 foundWord = True
        #                 direction = "leftIn"
        #             else:
        #                 foundWord = False
        #                 break
        #             if nextWordSearchDepthIndex + 1 < wordSearchInfo.wordSearchDepth and nextWordSearchWidthIndex - 1 >= 0:
        #                 nextWordSearchDepthIndex += 1
        #                 nextWordSearchWidthIndex -= 1

        #     # check the left up direction
        #     if depth + 1 < wordSearchInfo.wordSearchDepth and  height - 1 >= 0 and width - 1 >= 0 and wordSearchInfo.wordSearch[depth + 1][height - 1][width - 1] == wordList[word][1]:
        #         nextWordSearchDepthIndex = depth
        #         nextWordSearchWidthIndex = width
        #         nextWordSearchHeightIndex = height
        #         for letter in range(len(wordList[word])):
        #             if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
        #                 foundWord = True
        #                 direction = "leftUpIn"
        #             else:
        #                 foundWord = False
        #                 break
        #             if nextWordSearchDepthIndex + 1 < wordSearchInfo.wordSearchDepth and nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex - 1 >= 0:
        #                 nextWordSearchDepthIndex += 1
        #                 nextWordSearchWidthIndex -= 1
        #                 nextWordSearchHeightIndex -= 1

        #     # check the up direction
        #     if depth + 1 < wordSearchInfo.wordSearchDepth and  height - 1 >= 0 and wordSearchInfo.wordSearch[depth + 1][height - 1][width] == wordList[word][1]:
        #         nextWordSearchDepthIndex = depth
        #         nextWordSearchHeightIndex = height
        #         for letter in range(len(wordList[word])):
        #             if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][width] == wordList[word][letter]:
        #                 foundWord = True
        #                 direction = "upIn"
        #             else:
        #                 foundWord = False
        #                 break
        #             if nextWordSearchDepthIndex + 1 < wordSearchInfo.wordSearchDepth and nextWordSearchHeightIndex - 1 >= 0:
        #                 nextWordSearchDepthIndex += 1
        #                 nextWordSearchHeightIndex -= 1

        #     # check the right, up direction
        #     if depth + 1 < wordSearchInfo.wordSearchDepth and height - 1 >= 0 and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth + 1][height - 1][width + 1] == wordList[word][1]:
        #         nextWordSearchDepthIndex = depth
        #         nextWordSearchWidthIndex = width
        #         nextWordSearchHeightIndex = height
        #         for letter in range(len(wordList[word])):
        #             if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
        #                 foundWord = True
        #                 direction = "rightUpIn"
        #             else:
        #                 foundWord = False
        #                 break
        #             if nextWordSearchDepthIndex + 1 < wordSearchInfo.wordSearchDepth and nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex + 1 < wordSearchInfo.wordSearchWidth:
        #                 nextWordSearchDepthIndex += 1
        #                 nextWordSearchWidthIndex += 1
        #                 nextWordSearchHeightIndex -= 1

        for direction in directionsFoundIn:
            print(wordList[word], "was found starting at postition [", depth, "][", height, "][", width, "] going in the", direction, "direction")
            foundWordSet.add(word)

if __name__=="__main__":
    main()
