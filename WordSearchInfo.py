import numpy as np 

class WordSearchInfo:
    def __init__(self, wordSearchHeight, wordSearchWidth, wordSearchDepth, wordList, wordSearch = []):
        self.wordSearchHeight = wordSearchHeight
        self.wordSearchWidth = wordSearchWidth
        self.wordSearchDepth = wordSearchDepth
        self.wordList = wordList

        if len(wordSearch) == 0:
            self.wordSearch = np.array([[[0 for i in range(wordSearchWidth)] for j in range(wordSearchHeight)] for k in range(wordSearchDepth)] )
        else:
            self.wordSearch = wordSearch

        self.wordSearchSize = wordSearchHeight * wordSearchWidth * wordSearchDepth
        self.openWordSearchSpaces = np.array([i for i in range(self.wordSearchSize)])


    def toString(self):
        print("wordSearchHeight:", self.wordSearchHeight, ", wordSearchWidth:", self.wordSearchWidth,
            ", wordSearchDepth:", self.wordSearchDepth, ", wordSearchSize:", self.wordSearchSize,
            "\nwordList:", self.wordList,
            "\nopenWordSearchSpaces:", self.openWordSearchSpaces)
        self.printWordSearch()


    def printWordSearch(self):
        if (self.wordSearchDepth < 0):
            print("the provided wordSearch does not have a valid depth")

        elif (self.wordSearchDepth == 0): # 1D
            print(*self.wordSearch[0])

        elif (self.wordSearchDepth == 1): # 2D
            for i in range(self.wordSearchHeight):
                print(*self.wordSearch[i])

        elif (self.wordSearchDepth > 1): # 3D
            for k in range((self.wordSearchDepth)):
                for j in range(self.wordSearchHeight):
                    print(*self.wordSearch[k][j])
                print('\n')
        

    def checkWordInDirection(self, foundWord, word, direction, directionsFoundIn, startingHeight, startingWidth, heightChange, widthChange, startingDepth = -1, depthChange = 0):
        nextWordSearchDepthIndex = startingDepth
        nextWordSearchHeightIndex = startingHeight
        nextWordSearchWidthIndex = startingWidth

        for letter in word:

            # 2D
            if startingDepth == -1 and self.wordSearch[nextWordSearchHeightIndex][nextWordSearchWidthIndex] == letter:
                foundWord = True

            # 3D
            elif self.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == letter:
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
            foundWord = False


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
        return nextWordSearchDepthIndex + 1 < self.wordSearchDepth and nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex + 1 < self.nextWordSearchWidthIndex
