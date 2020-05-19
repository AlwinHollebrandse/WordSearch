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
        print('wordSearchDepth:', self.wordSearchDepth, ', wordSearchHeight:', self.wordSearchHeight,
            ', wordSearchWidth:', self.wordSearchWidth, ', wordSearchSize:', self.wordSearchSize,
            '\nwordList:', self.wordList,
            '\nopenWordSearchSpaces:', self.openWordSearchSpaces)
        self.printWordSearch()


    # TODO make 'JSON tostring'


    def printWordSearch(self):
        if (self.wordSearchDepth <= 0):
            print('the provided wordSearch does not have a valid depth')

        elif (self.wordSearchDepth > 0):
            for k in range((self.wordSearchDepth)):
                for j in range(self.wordSearchHeight):
                    print(*self.wordSearch[k][j])
                print('\n')


    def printWordSearchToFile(self, wordSearchFile):
        if (self.wordSearchDepth <= 0):
            print('the provided wordSearch does not have a valid depth', file=wordSearchFile)

        elif (self.wordSearchDepth > 1):
            for k in range((self.wordSearchDepth)):
                for j in range(self.wordSearchHeight):
                    print(*self.wordSearch[k][j], file=wordSearchFile)
                print('\n', file=wordSearchFile)


    def directionCheck(self, direction, nextWordSearchDepthIndex, nextWordSearchHeightIndex, nextWordSearchWidthIndex):
    # depth does not change
        if direction == 'right':
            return nextWordSearchWidthIndex + 1 < self.wordSearchWidth

        elif direction == 'rightDown':
            return nextWordSearchHeightIndex + 1 < self.wordSearchHeight and nextWordSearchWidthIndex + 1 < self.wordSearchWidth

        elif direction == 'down':
            return nextWordSearchHeightIndex + 1 < self.wordSearchHeight

        elif direction == 'leftDown':
            return nextWordSearchHeightIndex + 1 < self.wordSearchHeight and nextWordSearchWidthIndex - 1 >= 0

        elif direction == 'left':
            return nextWordSearchWidthIndex - 1 >= 0

        elif direction == 'leftUp':
            return nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex - 1 >= 0

        elif direction == 'up':
            return nextWordSearchHeightIndex - 1 >= 0

        elif direction == 'rightUp':
            return nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex + 1 < self.wordSearchWidth

    # depth goes out (to the user)
        elif direction == 'rightOut':
            return nextWordSearchDepthIndex - 1 >= 0 and nextWordSearchWidthIndex + 1 < self.wordSearchWidth

        elif direction == 'rightDownOut':
            return nextWordSearchDepthIndex - 1 >= 0 and nextWordSearchHeightIndex + 1 < self.wordSearchHeight and nextWordSearchWidthIndex + 1 < self.wordSearchWidth

        elif direction == 'downOut':
            return nextWordSearchDepthIndex - 1 >= 0 and nextWordSearchHeightIndex + 1 < self.wordSearchHeight

        elif direction == 'leftDownOut':
            return nextWordSearchDepthIndex - 1 >= 0 and nextWordSearchHeightIndex + 1 < self.wordSearchHeight and nextWordSearchWidthIndex - 1 >= 0

        elif direction == 'leftOut':
            return nextWordSearchDepthIndex - 1 >= 0 and nextWordSearchWidthIndex - 1 >= 0

        elif direction == 'leftUpOut':
            return nextWordSearchDepthIndex - 1 >= 0 and nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex - 1 >= 0

        elif direction == 'upOut':
            return nextWordSearchDepthIndex - 1 >= 0 and nextWordSearchHeightIndex - 1 >= 0

        elif direction == 'rightUpOut':
            return nextWordSearchDepthIndex - 1 >= 0 and nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex + 1 < self.wordSearchWidth

    # depth goes in (away from user)
        elif direction == 'rightIn':
            return nextWordSearchDepthIndex + 1 < self.wordSearchDepth and nextWordSearchWidthIndex + 1 < self.wordSearchWidth
        
        elif direction == 'rightDownIn':
            return nextWordSearchDepthIndex + 1 < self.wordSearchDepth and nextWordSearchHeightIndex + 1 < self.wordSearchHeight and nextWordSearchWidthIndex + 1 < self.wordSearchWidth

        elif direction == 'downIn':
            return nextWordSearchDepthIndex + 1 < self.wordSearchDepth and nextWordSearchHeightIndex + 1 < self.wordSearchHeight

        elif direction == 'leftDownIn':
            return nextWordSearchDepthIndex + 1 < self.wordSearchDepth and nextWordSearchHeightIndex + 1 < self.wordSearchHeight and nextWordSearchWidthIndex - 1 >= 0

        elif direction == 'leftIn':
            return nextWordSearchDepthIndex + 1 < self.wordSearchDepth and nextWordSearchWidthIndex - 1 >= 0

        elif direction == 'leftUpIn':
            return nextWordSearchDepthIndex + 1 < self.wordSearchDepth and nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex - 1 >= 0

        elif direction == 'upIn':
            return nextWordSearchDepthIndex + 1 < self.wordSearchDepth and nextWordSearchHeightIndex - 1 >= 0

        elif direction == 'rightUpIn':
            return nextWordSearchDepthIndex + 1 < self.wordSearchDepth and nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex + 1 < self.wordSearchWidth
