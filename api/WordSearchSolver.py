import numpy as np 
import json
from WordSearchInfo import WordSearchInfo

class WordSearchSolver:
    def solveWordSearch(self, wordSearchInfoJSON = {}): 
        print('solving the word search')

        direction = 'error'
        wordListFile = open('WordSearchWords.txt','r') # TODO change to some random default or frontend provided
        wordSearchFile = open('WordSearch.txt','r') # TODO change to json object
        wordList = [line.rstrip('\n').upper() for line in wordListFile]

        if (wordSearchInfoJSON == {}):
            wordSearch, wordSearchDepth, wordSearchHeight, wordSearchWidth = self.parseWordSearchFromFile(wordSearchFile)
        else:
            wordSearch, wordSearchDepth, wordSearchHeight, wordSearchWidth = self.parseWordSearchFromJSON(wordSearchInfoJSON)

        wordSearchInfo = WordSearchInfo(wordSearchHeight = wordSearchHeight, wordSearchWidth = wordSearchWidth, 
            wordSearchDepth = wordSearchDepth, wordList = wordList, wordSearch = wordSearch)
        wordSearchInfo.toString()

        foundWordSet = set([])
        foundStatementsList = []
        # TODO parallelize
        for depth in range(len(wordSearch)):
            for height in range(len(wordSearch[depth])):
                for width in range(len(wordSearch[depth][height])):
                    self.checkForWord(depth, height, width, wordSearchInfo, wordList, foundWordSet, foundStatementsList)  
        responseJSON = self.createResponseJSON(wordList, foundWordSet, foundStatementsList)
        return responseJSON


    def createResponseJSON(self, wordList, foundWordSet, foundStatementsList):
        notFoundStatement = 'words not found:' + str(list(set(wordList) - foundWordSet))
        print(notFoundStatement)
        response = {}
        response['found'] = foundStatementsList
        response['notFound'] = notFoundStatement
        return json.dumps(response)


    def parseWordSearchFromJSON(self, wordSearchInfoJSON):
        wordSearchInfoDict = json.loads(wordSearchInfoJSON)
        depth = wordSearchInfoDict['wordSearchDepth']
        height = wordSearchInfoDict['wordSearchHeight']
        width = wordSearchInfoDict['wordSearchWidth']
        wordSearch = wordSearchInfoDict['wordSearch']

        for currentField in [depth, height, width, wordSearch]:
            if (currentField == None):
                raise ValueError(currentField + ' was None')

        return wordSearch, depth, height, width


    def parseWordSearchFromFile(self, wordSearchFile):
        wordSearch3DIn2D = [[letter for letter in line.split()] for line in wordSearchFile] # wordSearch3DIn2D has the right characters, but wrong dimensions, which is why the rest is needed
        height = self.find3DWordSearchHeight(wordSearch3DIn2D) 
        width = self.find3DWordSearchWidth(wordSearch3DIn2D)
        totalNumberOfLines = self.getTotalNumberOfWordSearchFileLines(wordSearch3DIn2D)
        depth = totalNumberOfLines // (height + 2) # NOTE the 2 is from the double blank lines that seperates sections of the 3D word search

        wordSearch = np.array([[['a' for _ in range(width)] for _ in range(height)] for _ in range(depth)])
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

        return wordSearch, depth, height, width


    # finds the height of each layer in the wordSearch by incrementing a counter until the first "layer break" is encountered
    def find3DWordSearchHeight(self, wordSearch3DIn2D):
        height = 0
        for line in wordSearch3DIn2D:
            if line:
                height += 1
            else:
                break
        return height


    def find3DWordSearchWidth(self, wordSearch3DIn2D):
        for line in wordSearch3DIn2D:
            return len(line)


    def getTotalNumberOfWordSearchFileLines(self, wordSearch3DIn2D):
        return len(wordSearch3DIn2D)


    def checkWordInDirection(self, wordSearchInfo, word, direction, directionsFoundIn, startingDepth, startingHeight, startingWidth, depthChange, heightChange, widthChange):
        nextWordSearchDepthIndex = startingDepth
        nextWordSearchHeightIndex = startingHeight
        nextWordSearchWidthIndex = startingWidth
        foundWord = False

        for letter in word:

            if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == letter:
                foundWord = True
                
            else:
                foundWord = False
                break
            
            if wordSearchInfo.directionCheck(direction, nextWordSearchDepthIndex, nextWordSearchHeightIndex, nextWordSearchWidthIndex):
                nextWordSearchDepthIndex += depthChange
                nextWordSearchHeightIndex += heightChange
                nextWordSearchWidthIndex += widthChange

        if foundWord:
            directionsFoundIn.append(direction)


    def checkForWord(self, depth, height, width, wordSearchInfo, wordList, foundWordSet, foundStatementsList):
        for word in wordList:
            directionsFoundIn = []

            if wordSearchInfo.wordSearch[depth][height][width] == word[0]:  

            # depth does not change
                if width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth][height][width + 1] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'right', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = 0, widthChange = 1)

                if height + 1 < wordSearchInfo.wordSearchHeight and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth][height + 1][width + 1] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightDown', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = 1, widthChange = 1)

                if height + 1 < wordSearchInfo.wordSearchHeight and wordSearchInfo.wordSearch[depth][height + 1][width] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'down', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = 1, widthChange = 0)

                if height + 1 < wordSearchInfo.wordSearchHeight and width - 1 >= 0 and wordSearchInfo.wordSearch[depth][height + 1][width - 1] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftDown', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = 1, widthChange = -1)

                if width - 1 >= 0 and wordSearchInfo.wordSearch[depth][height][width - 1] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'left', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = 0, widthChange = -1)

                if height - 1 >= 0 and width - 1 >= 0 and wordSearchInfo.wordSearch[depth][height - 1][width - 1] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftUp', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = -1, widthChange = -1)

                if height - 1 >= 0 and wordSearchInfo.wordSearch[depth][height - 1][width] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'up', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = -1, widthChange = 0)

                if height - 1 >= 0 and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth][height - 1][width + 1] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightUp', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 0, heightChange = -1, widthChange = 1)

            # depth goes out (to the user)
                if depth - 1 >= 0 and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth - 1][height][width + 1] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightOut', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = 0, widthChange = 1)

                if depth - 1 >= 0 and height + 1 < wordSearchInfo.wordSearchHeight and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth - 1][height + 1][width + 1] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightDownOut', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = 1, widthChange = 1)

                if depth - 1 >= 0 and height + 1 < wordSearchInfo.wordSearchHeight and wordSearchInfo.wordSearch[depth - 1][height + 1][width] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'downOut', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = 1, widthChange = 0)

                if depth - 1 >= 0 and height + 1 < wordSearchInfo.wordSearchHeight and width - 1 >= 0 and wordSearchInfo.wordSearch[depth - 1][height + 1][width - 1] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftDownOut', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = 1, widthChange = -1)

                if depth - 1 >= 0 and  width - 1 >= 0 and wordSearchInfo.wordSearch[depth - 1][height][width - 1] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftOut', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = 0, widthChange = -1)

                if depth - 1 >= 0 and  height - 1 >= 0 and width - 1 >= 0 and wordSearchInfo.wordSearch[depth - 1][height - 1][width - 1] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftUpOut', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = -1, widthChange = -1)

                if depth - 1 >= 0 and  height - 1 >= 0 and wordSearchInfo.wordSearch[depth - 1][height - 1][width] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'upOut', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = -1, widthChange = 0)

                if depth - 1 >= 0 and height - 1 >= 0 and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth - 1][height - 1][width + 1] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightUpOut', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = -1, widthChange = 1)

                if depth - 1 >= 0 and wordSearchInfo.wordSearch[depth - 1][height][width] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'out', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = -1, heightChange = 0, widthChange = 0)

            # depth goes in (away from user)
                if depth + 1 < wordSearchInfo.wordSearchDepth and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth + 1][height][width + 1] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightIn', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = 0, widthChange = 1)
                
                if depth + 1 < wordSearchInfo.wordSearchDepth and height + 1 < wordSearchInfo.wordSearchHeight and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth + 1][height + 1][width + 1] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightDownIn', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = 1, widthChange = 1)

                if depth + 1 < wordSearchInfo.wordSearchDepth and height + 1 < wordSearchInfo.wordSearchHeight and wordSearchInfo.wordSearch[depth + 1][height + 1][width] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'downIn', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = 1, widthChange = 0)

                if depth + 1 < wordSearchInfo.wordSearchDepth and height + 1 < wordSearchInfo.wordSearchHeight and width - 1 >= 0 and wordSearchInfo.wordSearch[depth + 1][height + 1][width - 1] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftDownIn', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = 1, widthChange = -1)

                if depth + 1 < wordSearchInfo.wordSearchDepth and  width - 1 >= 0 and wordSearchInfo.wordSearch[depth + 1][height][width - 1] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftIn', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = 0, widthChange = -1)

                if depth + 1 < wordSearchInfo.wordSearchDepth and  height - 1 >= 0 and width - 1 >= 0 and wordSearchInfo.wordSearch[depth + 1][height - 1][width - 1] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'leftUpIn', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = -1, widthChange = -1)

                if depth + 1 < wordSearchInfo.wordSearchDepth and  height - 1 >= 0 and wordSearchInfo.wordSearch[depth + 1][height - 1][width] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'upIn', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = -1, widthChange = 0)

                if depth + 1 < wordSearchInfo.wordSearchDepth and height - 1 >= 0 and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth + 1][height - 1][width + 1] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'rightUpIn', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = -1, widthChange = 1)

                if depth + 1 < wordSearchInfo.wordSearchDepth and wordSearchInfo.wordSearch[depth + 1][height][width] == word[1]:
                    self.checkWordInDirection(wordSearchInfo = wordSearchInfo, word = word, direction = 'in', directionsFoundIn = directionsFoundIn, 
                        startingDepth = depth, startingHeight = height, startingWidth = width, depthChange = 1, heightChange = 0, widthChange = 0)

            for direction in directionsFoundIn:
                foundWordSet.add(word)
                foundStatement = word, "was found starting at postition [", depth, "][", height, "][", width, "] going in the", direction, "direction"
                print(foundStatement)
                foundStatementsList.append(foundStatement)

if __name__=="__main__":
    wordSearchSolver = WordSearchSolver()
    wordSearchSolver.solveWordSearch()

