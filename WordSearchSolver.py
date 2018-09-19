from WordSearchInfo import WordSearchInfo

def checkForWord(height, width, wordSearchInfo, wordList):
    for word in range(len(wordList) - 1, -1, -1):  # for each word in the wordList, itereted backwards so that things can be popped cleanly  
        foundWord = False
        if wordSearchInfo.wordSearch[height][width] == wordList[word][0]: 
            if foundWord == False and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[height][width + 1] == wordList[word][1]: # check the right direction
                nextWordSearchWidthIndex = width
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[height][nextWordSearchWidthIndex] == wordList[word][letter]:
                        foundWord = True
                        direction = "right"
                    else:
                        foundWord = False
                        break
                    if nextWordSearchWidthIndex + 1 < wordSearchInfo.wordSearchWidth:
                        nextWordSearchWidthIndex += 1

            if foundWord == False and height + 1 < wordSearchInfo.wordSearchHeight and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[height + 1][width + 1] == wordList[word][1]: # check the right, down direction
                nextWordSearchWidthIndex = width
                nextWordSearchHeightIndex = height
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
                        foundWord = True
                        direction = "rightDown"
                    else:
                        foundWord = False
                        break
                    if nextWordSearchHeightIndex + 1 < wordSearchInfo.wordSearchHeight and nextWordSearchWidthIndex + 1 < wordSearchInfo.wordSearchWidth:
                        nextWordSearchWidthIndex += 1
                        nextWordSearchHeightIndex += 1

            if foundWord == False and height + 1 < wordSearchInfo.wordSearchHeight and wordSearchInfo.wordSearch[height + 1][width] == wordList[word][1]: # check the down direction
                nextWordSearchHeightIndex = height
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[nextWordSearchHeightIndex][width] == wordList[word][letter]:
                        foundWord = True
                        direction = "down"
                    else:
                        foundWord = False
                        break
                    if nextWordSearchHeightIndex + 1 < wordSearchInfo.wordSearchHeight:
                        nextWordSearchHeightIndex += 1

            if foundWord == False and height + 1 < wordSearchInfo.wordSearchHeight and width - 1 >= 0 and wordSearchInfo.wordSearch[height + 1][width - 1] == wordList[word][1]: # check the left, down direction
                nextWordSearchWidthIndex = width
                nextWordSearchHeightIndex = height
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
                        foundWord = True
                        direction = "leftDown"
                    else:
                        foundWord = False
                        break
                    if nextWordSearchHeightIndex + 1 < wordSearchInfo.wordSearchHeight and nextWordSearchWidthIndex - 1 >= 0:
                        nextWordSearchWidthIndex += -1
                        nextWordSearchHeightIndex += 1

            if foundWord == False and width - 1 >= 0 and wordSearchInfo.wordSearch[height][width - 1] == wordList[word][1]: # check the left direction
                nextWordSearchWidthIndex = width
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[height][nextWordSearchWidthIndex] == wordList[word][letter]:
                        foundWord = True
                        direction = "left"
                    else:
                        foundWord = False
                        break
                    if nextWordSearchWidthIndex - 1 >= 0:
                        nextWordSearchWidthIndex += -1

            if foundWord == False and height - 1 >= 0 and width - 1 >= 0 and wordSearchInfo.wordSearch[height - 1][width - 1] == wordList[word][1]: # check the left up direction
                nextWordSearchWidthIndex = width
                nextWordSearchHeightIndex = height
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
                        foundWord = True
                        direction = "leftUp"
                    else:
                        foundWord = False
                        break
                    if nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex - 1 >= 0:
                        nextWordSearchWidthIndex += -1
                        nextWordSearchHeightIndex += -1

            if foundWord == False and height - 1 >= 0 and wordSearchInfo.wordSearch[height - 1][width] == wordList[word][1]: # check the up direction
                nextWordSearchHeightIndex = height
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[nextWordSearchHeightIndex][width] == wordList[word][letter]:
                        foundWord = True
                        direction = "up"
                    else:
                        foundWord = False
                        break
                    if nextWordSearchHeightIndex - 1 >= 0:
                        nextWordSearchHeightIndex += -1

            if foundWord == False and height - 1 >= 0 and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[height - 1][width + 1] == wordList[word][1]: # check the right, up direction
                nextWordSearchWidthIndex = width
                nextWordSearchHeightIndex = height
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
                        foundWord = True
                        direction = "rightUp"
                    else:
                        foundWord = False
                        break
                    if nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex + 1 < wordSearchInfo.wordSearchWidth:
                        nextWordSearchWidthIndex += 1
                        nextWordSearchHeightIndex += -1

        if foundWord: #TODO, if 2 words start in the same locaion, only 1 will be found. Fix this. 
            print(wordList.pop(word),"was found starting at postition [",height,"][",width,"] going in the",direction,"direction") #use this if you just want to find the first instance of the word
            #print(wordList[word],"was found starting at postition [",height,"][",width,"] going in the",direction,"direction") #use this if you just want to find every instance of the word. This has a slower performance


def print2DWordSearch(wordSearchInfo):
    for i in range(wordSearchInfo.wordSearchHeight):
        print(*wordSearchInfo.wordSearch[i])


def main(): 
    direction = "error"
    wordList = []
    wordListFile = open("WordSearchWords.txt","r")
    wordSearchFile = open("WordSearch.txt","r")
    for line in wordListFile:
        #print(line.rstrip('\n'))
        wordList.append(line.rstrip('\n').upper())  
    wordSearch = [[n for n in line.split()] for line in wordSearchFile]
    wordSearchDepth = 1
    wordSearchHeight = len(wordSearch)
    wordSearchWidth = len(wordSearch[0])
    wordSearchSize = wordSearchHeight * wordSearchWidth
    openWordSearchSpaces = []
    print("wordSearchHeight:",wordSearchHeight,", wordSearchWidth:",wordSearchWidth)
    wordSearchInfo = WordSearchInfo(wordSearch, wordSearchDepth, wordSearchHeight, wordSearchWidth, wordSearchSize, openWordSearchSpaces)
    wordSearchInfo.toString()
    print2DWordSearch(wordSearchInfo)
    
    #TODO check if the plural words are found before singular ones. If not, they should be. Ex: check for an 's' at the end of a found word if wordList has a plural version
    #TODO add threads
    for height in range(wordSearchInfo.wordSearchHeight):
        for width in range(wordSearchInfo.wordSearchWidth):
            checkForWord(height, width, wordSearchInfo, wordList) 
    print("words left:",wordList)    

print("solving the word search")
if __name__=="__main__":
    main()  