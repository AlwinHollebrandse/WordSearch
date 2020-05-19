import numpy as np 

class WordSearchInfo:
    def __init__(self, wordSearchHeight, wordSearchWidth, wordSearchDepth, wordList, wordSearch = []):
        self.wordSearchHeight = wordSearchHeight
        self.wordSearchWidth = wordSearchWidth
        self.wordSearchDepth = wordSearchDepth
        self.wordList = wordList
        self.wordSearchSize = wordSearchHeight * wordSearchWidth * wordSearchDepth

        if len(wordSearch) == 0:
            self.wordSearch = np.array([[['a' for i in range(wordSearchWidth)] for j in range(wordSearchHeight)] for k in range(wordSearchDepth)])
            self.openWordSearchSpaces = [i for i in range(self.wordSearchSize)]
        else:
            self.wordSearch = wordSearch
            self.openWordSearchSpaces = []


    def toString(self):
        print("wordSearchDepth:", self.wordSearchDepth, ", wordSearchHeight:", self.wordSearchHeight,
            ", wordSearchWidth:", self.wordSearchWidth, ", wordSearchSize:", self.wordSearchSize,
            "\nwordList:", self.wordList,
            "\nopenWordSearchSpaces:", self.openWordSearchSpaces)
        self.printWordSearch()


    # TODO make 'JSON tostring'


    def printWordSearch(self):
        if (self.wordSearchDepth <= 0):
            print("the provided wordSearch does not have a valid depth")

        elif (self.wordSearchDepth > 0):
            for k in range((self.wordSearchDepth)):
                for j in range(self.wordSearchHeight):
                    print(*self.wordSearch[k][j])
                print('\n')


    def printWordSearchToFile(self, wordSearchFile):
        if (self.wordSearchDepth <= 0):
            print("the provided wordSearch does not have a valid depth", file=wordSearchFile)

        elif (self.wordSearchDepth > 1):
            for k in range((self.wordSearchDepth)):
                for j in range(self.wordSearchHeight):
                    print(*self.wordSearch[k][j], file=wordSearchFile)
                print('\n', file=wordSearchFile)

        
    # TODO if 3D depth = 1 then this could move to the solver file
    def checkWordInDirection(self, word, direction, directionsFoundIn, startingHeight, startingWidth, heightChange, widthChange, startingDepth = -1, depthChange = 0):
        nextWordSearchDepthIndex = startingDepth
        nextWordSearchHeightIndex = startingHeight
        nextWordSearchWidthIndex = startingWidth
        foundWord = False

        for letter in word:

            if self.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == letter:
                foundWord = True
                
            else:
                foundWord = False
                break
           
            if directionCheck(self, direction, nextWordSearchDepthIndex, nextWordSearchHeightIndex, nextWordSearchWidthIndex):
                nextWordSearchDepthIndex += depthChange
                nextWordSearchHeightIndex += heightChange
                nextWordSearchWidthIndex += widthChange

        if foundWord:
            directionsFoundIn.append(direction)


    def directionCheck(self, direction, nextWordSearchDepthIndex, nextWordSearchHeightIndex, nextWordSearchWidthIndex):
    # NOTE the following direction checks are for when the depth remains the same
        # check the right direction
        if direction == "right":
            return nextWordSearchWidthIndex + 1 < self.wordSearchWidth

        # check the right, down direction
        if direction == "rightDown":
            return nextWordSearchHeightIndex + 1 < self.wordSearchHeight and nextWordSearchWidthIndex + 1 < self.wordSearchWidth

        # check the down direction
        if direction == "down":
            return nextWordSearchHeightIndex + 1 < self.wordSearchHeight

        # check the left, down direction
        if direction == "leftDown":
            return nextWordSearchHeightIndex + 1 < self.wordSearchHeight and nextWordSearchWidthIndex - 1 >= 0

        # check the left direction
        if direction == "left":
            return nextWordSearchWidthIndex - 1 >= 0

        # check the left up direction
        if direction == "leftUp":
            return nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex - 1 >= 0

        # check the up direction
        if direction == "up":
            return nextWordSearchHeightIndex - 1 >= 0

        # check the right, up direction
        if direction == "rightUp":
            return nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex + 1 < self.wordSearchWidth

    # NOTE the following direction checks are for when the depth goes out (to the user)
        # check the right direction
        if direction == "rightOut":
            return nextWordSearchDepthIndex - 1 >= 0 and nextWordSearchWidthIndex + 1 < self.wordSearchWidth

        # check the right, down direction
        if direction == "rightDownOut":
            return nextWordSearchDepthIndex - 1 >= 0 and nextWordSearchHeightIndex + 1 < self.wordSearchHeight and nextWordSearchWidthIndex + 1 < self.wordSearchWidth

        # check the down direction
        if direction == "downOut":
            return nextWordSearchDepthIndex - 1 >= 0 and nextWordSearchHeightIndex + 1 < self.wordSearchHeight

        # check the left, down direction
        if direction == "leftDownOut":
            return nextWordSearchDepthIndex - 1 >= 0 and nextWordSearchHeightIndex + 1 < self.wordSearchHeight and nextWordSearchWidthIndex - 1 >= 0

        # check the left direction
        if direction == "leftOut":
            return nextWordSearchDepthIndex - 1 >= 0 and nextWordSearchWidthIndex - 1 >= 0

        # check the left up direction
        if direction == "leftUpOut":
            return nextWordSearchDepthIndex - 1 >= 0 and nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex - 1 >= 0

        # check the up direction
        if direction == "upOut":
            return nextWordSearchDepthIndex - 1 >= 0 and nextWordSearchHeightIndex - 1 >= 0

        # check the right, up direction
        if direction == "rightUpOut":
            return nextWordSearchDepthIndex - 1 >= 0 and nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex + 1 < self.wordSearchWidth

    # NOTE the following direction checks are for when the depth goes in (away from the user)
        # check the right direction
        if direction == "rightIn":
            return nextWordSearchDepthIndex + 1 < self.wordSearchDepth and nextWordSearchWidthIndex + 1 < self.wordSearchWidth
        
        # check the right, down direction
        if direction == "rightDownIn":
            return nextWordSearchDepthIndex + 1 < self.wordSearchDepth and nextWordSearchHeightIndex + 1 < self.wordSearchHeight and nextWordSearchWidthIndex + 1 < self.wordSearchWidth

        # check the down direction
        if direction == "downIn":
            return nextWordSearchDepthIndex + 1 < self.wordSearchDepth and nextWordSearchHeightIndex + 1 < self.wordSearchHeight

        # check the left, down direction
        if direction == "leftDownIn":
            return nextWordSearchDepthIndex + 1 < self.wordSearchDepth and nextWordSearchHeightIndex + 1 < self.wordSearchHeight and nextWordSearchWidthIndex - 1 >= 0

        # check the left direction
        if direction == "leftIn":
            return nextWordSearchDepthIndex + 1 < self.wordSearchDepth and nextWordSearchWidthIndex - 1 >= 0

        # check the left up direction
        if direction == "leftUpIn":
            return nextWordSearchDepthIndex + 1 < self.wordSearchDepth and nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex - 1 >= 0

        # check the up direction
        if direction == "upIn":
            return nextWordSearchDepthIndex + 1 < self.wordSearchDepth and nextWordSearchHeightIndex - 1 >= 0

        # check the right, up direction
        if direction == "rightUpIn":
            return nextWordSearchDepthIndex + 1 < self.wordSearchDepth and nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex + 1 < self.wordSearchWidth
