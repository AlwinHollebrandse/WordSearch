class WordSearchInfo:
    def __init__(self, wordSearch, wordSearchDepth, wordSearchHeight, wordSearchWidth, wordSearchSize, openWordSearchSpaces):
        self.wordSearch = wordSearch
        self.wordSearchDepth = wordSearchDepth
        self.wordSearchHeight = wordSearchHeight
        self.wordSearchWidth = wordSearchWidth
        self.wordSearchSize = wordSearchSize
        self.openWordSearchSpaces = openWordSearchSpaces

    def toString(self):
        print("wordSearch:",self.wordSearch,", wordSearchDepth:",self.wordSearchDepth,", wordSearchHeight:",self.wordSearchHeight,", wordSearchWidth:",self.wordSearchWidth,", wordSearchSize:",self.wordSearchSize,"\nopenWordSearchSpaces:",self.openWordSearchSpaces)