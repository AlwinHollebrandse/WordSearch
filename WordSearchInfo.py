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
        