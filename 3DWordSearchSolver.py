from WordSearchInfo import WordSearchInfo

def checkForWord(depth, height, width, wordSearchInfo, wordList):
    for word in range(len(wordList) - 1, -1, -1):  # for each word in the wordList, itereted backwards so that things can be popped cleanly  
        foundWord = False
        #print("looking for word:",wordList[word])
        if wordSearchInfo.wordSearch[depth][height][width] == wordList[word][0]:      
        #Depth does not change
            if foundWord == False and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth][height][width + 1] == wordList[word][1]: # check the right direction
                nextWordSearchWidthIndex = width
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[depth][height][nextWordSearchWidthIndex] == wordList[word][letter]:
                        #print("wordSearchValue:",wordSearchInfo.wordSearch[depth][height][nextWordSearchWidthIndex],", wordValue:",wordList[word][letter])
                        foundWord = True
                        direction = "right"
                    else:
                        foundWord = False
                        break
                    if nextWordSearchWidthIndex + 1 < wordSearchInfo.wordSearchWidth:
                        nextWordSearchWidthIndex += 1
            
            if foundWord == False and height + 1 < wordSearchInfo.wordSearchHeight and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth][height + 1][width + 1] == wordList[word][1]: # check the right, down direction
                nextWordSearchWidthIndex = width
                nextWordSearchHeightIndex = height
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[depth][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
                        foundWord = True
                        direction = "rightDown"
                    else:
                        foundWord = False
                        break
                    if nextWordSearchHeightIndex + 1 < wordSearchInfo.wordSearchHeight and nextWordSearchWidthIndex + 1 < wordSearchInfo.wordSearchWidth:
                        nextWordSearchWidthIndex += 1
                        nextWordSearchHeightIndex += 1

            if foundWord == False and height + 1 < wordSearchInfo.wordSearchHeight and wordSearchInfo.wordSearch[depth][height + 1][width] == wordList[word][1]: # check the down direction
                nextWordSearchHeightIndex = height
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[depth][nextWordSearchHeightIndex][width] == wordList[word][letter]:
                        foundWord = True
                        direction = "down"
                    else:
                        foundWord = False
                        break
                    if nextWordSearchHeightIndex + 1 < wordSearchInfo.wordSearchHeight:
                        nextWordSearchHeightIndex += 1

            if foundWord == False and height + 1 < wordSearchInfo.wordSearchHeight and width - 1 >= 0 and wordSearchInfo.wordSearch[depth][height + 1][width - 1] == wordList[word][1]: # check the left, down direction
                nextWordSearchWidthIndex = width
                nextWordSearchHeightIndex = height
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[depth][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
                        foundWord = True
                        direction = "leftDown"
                    else:
                        foundWord = False
                        break
                    if nextWordSearchHeightIndex + 1 < wordSearchInfo.wordSearchHeight and nextWordSearchWidthIndex - 1 >= 0:
                        nextWordSearchWidthIndex -= 1
                        nextWordSearchHeightIndex += 1

            if foundWord == False and width - 1 >= 0 and wordSearchInfo.wordSearch[depth][height][width - 1] == wordList[word][1]: # check the left direction
                nextWordSearchWidthIndex = width
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[depth][height][nextWordSearchWidthIndex] == wordList[word][letter]:
                        foundWord = True
                        direction = "left"
                    else:
                        foundWord = False
                        break
                    if nextWordSearchWidthIndex - 1 >= 0:
                        nextWordSearchWidthIndex -= 1

            if foundWord == False and height - 1 >= 0 and width - 1 >= 0 and wordSearchInfo.wordSearch[depth][height - 1][width - 1] == wordList[word][1]: # check the left up direction
                nextWordSearchWidthIndex = width
                nextWordSearchHeightIndex = height
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[depth][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
                        foundWord = True
                        direction = "leftUp"
                    else:
                        foundWord = False
                        break
                    if nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex - 1 >= 0:
                        nextWordSearchWidthIndex -= 1
                        nextWordSearchHeightIndex -= 1

            if foundWord == False and height - 1 >= 0 and wordSearchInfo.wordSearch[depth][height - 1][width] == wordList[word][1]: # check the up direction
                nextWordSearchHeightIndex = height
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[depth][nextWordSearchHeightIndex][width] == wordList[word][letter]:
                        foundWord = True
                        direction = "up"
                    else:
                        foundWord = False
                        break
                    if nextWordSearchHeightIndex - 1 >= 0:
                        nextWordSearchHeightIndex -= 1

            if foundWord == False and height - 1 >= 0 and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth][height - 1][width + 1] == wordList[word][1]: # check the right, up direction
                nextWordSearchWidthIndex = width
                nextWordSearchHeightIndex = height
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[depth][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
                        foundWord = True
                        direction = "rightUp"
                    else:
                        foundWord = False
                        break
                    if nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex + 1 < wordSearchInfo.wordSearchWidth:
                        nextWordSearchWidthIndex += 1
                        nextWordSearchHeightIndex -= 1

        #depth goes out (to the user)
            if foundWord == False and depth - 1 >= 0 and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth - 1][height][width + 1] == wordList[word][1]: # check the right direction
                nextWordSearchDepthIndex = depth
                nextWordSearchWidthIndex = width
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][height][nextWordSearchWidthIndex] == wordList[word][letter]:
                        foundWord = True
                        direction = "rightOut"
                    else:
                        foundWord = False
                        break
                    if depth - 1 >= 0 and nextWordSearchWidthIndex + 1 < wordSearchInfo.wordSearchWidth:
                        nextWordSearchDepthIndex += -1
                        nextWordSearchWidthIndex += 1
            
            if foundWord == False and depth - 1 >= 0 and height + 1 < wordSearchInfo.wordSearchHeight and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth - 1][height + 1][width + 1] == wordList[word][1]: # check the right, down direction
                nextWordSearchDepthIndex = depth
                nextWordSearchWidthIndex = width
                nextWordSearchHeightIndex = height
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
                        foundWord = True
                        direction = "rightDownOut"
                    else:
                        foundWord = False
                        break
                    if depth - 1 >= 0 and nextWordSearchHeightIndex + 1 < wordSearchInfo.wordSearchHeight and nextWordSearchWidthIndex + 1 < wordSearchInfo.wordSearchWidth:
                        nextWordSearchDepthIndex += -1
                        nextWordSearchWidthIndex += 1
                        nextWordSearchHeightIndex += 1

            if foundWord == False and depth - 1 >= 0 and height + 1 < wordSearchInfo.wordSearchHeight and wordSearchInfo.wordSearch[depth - 1][height + 1][width] == wordList[word][1]: # check the down direction
                nextWordSearchDepthIndex = depth
                nextWordSearchHeightIndex = height
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][width] == wordList[word][letter]:
                        foundWord = True
                        direction = "downOut"
                    else:
                        foundWord = False
                        break
                    if depth - 1 >= 0 and nextWordSearchHeightIndex + 1 < wordSearchInfo.wordSearchHeight:
                        nextWordSearchDepthIndex += -1
                        nextWordSearchHeightIndex += 1

            if foundWord == False and depth - 1 >= 0 and height + 1 < wordSearchInfo.wordSearchHeight and width - 1 >= 0 and wordSearchInfo.wordSearch[depth - 1][height + 1][width - 1] == wordList[word][1]: # check the left, down direction
                nextWordSearchDepthIndex = depth
                nextWordSearchWidthIndex = width
                nextWordSearchHeightIndex = height
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
                        foundWord = True
                        direction = "leftDownOut"
                    else:
                        foundWord = False
                        break
                    if depth - 1 >= 0 and nextWordSearchHeightIndex + 1 < wordSearchInfo.wordSearchHeight and nextWordSearchWidthIndex - 1 >= 0:
                        nextWordSearchDepthIndex += -1
                        nextWordSearchWidthIndex -= 1
                        nextWordSearchHeightIndex += 1

            if foundWord == False and depth - 1 >= 0 and  width - 1 >= 0 and wordSearchInfo.wordSearch[depth - 1][height][width - 1] == wordList[word][1]: # check the left direction
                nextWordSearchDepthIndex = depth
                nextWordSearchWidthIndex = width
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][height][nextWordSearchWidthIndex] == wordList[word][letter]:
                        foundWord = True
                        direction = "leftOut"
                    else:
                        foundWord = False
                        break
                    if depth - 1 >= 0 and nextWordSearchWidthIndex - 1 >= 0:
                        nextWordSearchDepthIndex += -1
                        nextWordSearchWidthIndex -= 1

            if foundWord == False and depth - 1 >= 0 and  height - 1 >= 0 and width - 1 >= 0 and wordSearchInfo.wordSearch[depth - 1][height - 1][width - 1] == wordList[word][1]: # check the left up direction
                nextWordSearchDepthIndex = depth
                nextWordSearchWidthIndex = width
                nextWordSearchHeightIndex = height
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
                        foundWord = True
                        direction = "leftUpOut"
                    else:
                        foundWord = False
                        break
                    if depth - 1 >= 0 and nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex - 1 >= 0:
                        nextWordSearchDepthIndex += -1
                        nextWordSearchWidthIndex -= 1
                        nextWordSearchHeightIndex -= 1

            if foundWord == False and depth - 1 >= 0 and  height - 1 >= 0 and wordSearchInfo.wordSearch[depth - 1][height - 1][width] == wordList[word][1]: # check the up direction
                nextWordSearchDepthIndex = depth
                nextWordSearchHeightIndex = height
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][width] == wordList[word][letter]:
                        foundWord = True
                        direction = "upOut"
                    else:
                        foundWord = False
                        break
                    if depth - 1 >= 0 and nextWordSearchHeightIndex - 1 >= 0:
                        nextWordSearchDepthIndex += -1
                        nextWordSearchHeightIndex -= 1

            if foundWord == False and depth - 1 >= 0 and height - 1 >= 0 and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth - 1][height - 1][width + 1] == wordList[word][1]: # check the right, up direction
                nextWordSearchDepthIndex = depth
                nextWordSearchWidthIndex = width
                nextWordSearchHeightIndex = height
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
                        foundWord = True
                        direction = "rightUpOut"
                    else:
                        foundWord = False
                        break
                    if depth - 1 >= 0 and nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex + 1 < wordSearchInfo.wordSearchWidth:
                        nextWordSearchDepthIndex += -1
                        nextWordSearchWidthIndex += 1
                        nextWordSearchHeightIndex -= 1

        #depth goes in (away from the user)
            if foundWord == False and depth + 1 < wordSearchInfo.wordSearchDepth and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth + 1][height][width + 1] == wordList[word][1]: # check the right direction
                nextWordSearchDepthIndex = depth
                nextWordSearchWidthIndex = width
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][height][nextWordSearchWidthIndex] == wordList[word][letter]:
                        foundWord = True
                        direction = "rightIn"
                    else:
                        foundWord = False
                        break
                    if nextWordSearchDepthIndex + 1 < wordSearchInfo.wordSearchDepth and nextWordSearchWidthIndex + 1 < wordSearchInfo.wordSearchWidth:
                        nextWordSearchDepthIndex += 1
                        nextWordSearchWidthIndex += 1
            
            if foundWord == False and depth + 1 < wordSearchInfo.wordSearchDepth and height + 1 < wordSearchInfo.wordSearchHeight and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth + 1][height + 1][width + 1] == wordList[word][1]: # check the right, down direction
                nextWordSearchDepthIndex = depth
                nextWordSearchWidthIndex = width
                nextWordSearchHeightIndex = height
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
                        foundWord = True
                        direction = "rightDownIn"
                    else:
                        foundWord = False
                        break
                    if nextWordSearchDepthIndex + 1 < wordSearchInfo.wordSearchDepth and nextWordSearchHeightIndex + 1 < wordSearchInfo.wordSearchHeight and nextWordSearchWidthIndex + 1 < wordSearchInfo.wordSearchWidth:
                        nextWordSearchDepthIndex += 1
                        nextWordSearchWidthIndex += 1
                        nextWordSearchHeightIndex += 1

            if foundWord == False and depth + 1 < wordSearchInfo.wordSearchDepth and height + 1 < wordSearchInfo.wordSearchHeight and wordSearchInfo.wordSearch[depth + 1][height + 1][width] == wordList[word][1]: # check the down direction
                nextWordSearchDepthIndex = depth
                nextWordSearchHeightIndex = height
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][width] == wordList[word][letter]:
                        foundWord = True
                        direction = "downIn"
                    else:
                        foundWord = False
                        break
                    if nextWordSearchDepthIndex + 1 < wordSearchInfo.wordSearchDepth and nextWordSearchHeightIndex + 1 < wordSearchInfo.wordSearchHeight:
                        nextWordSearchDepthIndex += 1
                        nextWordSearchHeightIndex += 1

            if foundWord == False and depth + 1 < wordSearchInfo.wordSearchDepth and height + 1 < wordSearchInfo.wordSearchHeight and width - 1 >= 0 and wordSearchInfo.wordSearch[depth + 1][height + 1][width - 1] == wordList[word][1]: # check the left, down direction
                nextWordSearchDepthIndex = depth
                nextWordSearchWidthIndex = width
                nextWordSearchHeightIndex = height
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
                        foundWord = True
                        direction = "leftDownIn"
                    else:
                        foundWord = False
                        break
                    if nextWordSearchDepthIndex + 1 < wordSearchInfo.wordSearchDepth and nextWordSearchHeightIndex + 1 < wordSearchInfo.wordSearchHeight and nextWordSearchWidthIndex - 1 >= 0:
                        nextWordSearchDepthIndex += 1
                        nextWordSearchWidthIndex -= 1
                        nextWordSearchHeightIndex += 1

            if foundWord == False and depth + 1 < wordSearchInfo.wordSearchDepth and  width - 1 >= 0 and wordSearchInfo.wordSearch[depth + 1][height][width - 1] == wordList[word][1]: # check the left direction
                nextWordSearchDepthIndex = depth
                nextWordSearchWidthIndex = width
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][height][nextWordSearchWidthIndex] == wordList[word][letter]:
                        foundWord = True
                        direction = "leftIn"
                    else:
                        foundWord = False
                        break
                    if nextWordSearchDepthIndex + 1 < wordSearchInfo.wordSearchDepth and nextWordSearchWidthIndex - 1 >= 0:
                        nextWordSearchDepthIndex += 1
                        nextWordSearchWidthIndex -= 1

            if foundWord == False and depth + 1 < wordSearchInfo.wordSearchDepth and  height - 1 >= 0 and width - 1 >= 0 and wordSearchInfo.wordSearch[depth + 1][height - 1][width - 1] == wordList[word][1]: # check the left up direction
                nextWordSearchDepthIndex = depth
                nextWordSearchWidthIndex = width
                nextWordSearchHeightIndex = height
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
                        foundWord = True
                        direction = "leftUpIn"
                    else:
                        foundWord = False
                        break
                    if nextWordSearchDepthIndex + 1 < wordSearchInfo.wordSearchDepth and nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex - 1 >= 0:
                        nextWordSearchDepthIndex += 1
                        nextWordSearchWidthIndex -= 1
                        nextWordSearchHeightIndex -= 1

            if foundWord == False and depth + 1 < wordSearchInfo.wordSearchDepth and  height - 1 >= 0 and wordSearchInfo.wordSearch[depth + 1][height - 1][width] == wordList[word][1]: # check the up direction
                nextWordSearchDepthIndex = depth
                nextWordSearchHeightIndex = height
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][width] == wordList[word][letter]:
                        foundWord = True
                        direction = "upIn"
                    else:
                        foundWord = False
                        break
                    if nextWordSearchDepthIndex + 1 < wordSearchInfo.wordSearchDepth and nextWordSearchHeightIndex - 1 >= 0:
                        nextWordSearchDepthIndex += 1
                        nextWordSearchHeightIndex -= 1

            if foundWord == False and depth + 1 < wordSearchInfo.wordSearchDepth and height - 1 >= 0 and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[depth + 1][height - 1][width + 1] == wordList[word][1]: # check the right, up direction
                nextWordSearchDepthIndex = depth
                nextWordSearchWidthIndex = width
                nextWordSearchHeightIndex = height
                for letter in range(len(wordList[word])):
                    if wordSearchInfo.wordSearch[nextWordSearchDepthIndex][nextWordSearchHeightIndex][nextWordSearchWidthIndex] == wordList[word][letter]:
                        foundWord = True
                        direction = "rightUpIn"
                    else:
                        foundWord = False
                        break
                    if nextWordSearchDepthIndex + 1 < wordSearchInfo.wordSearchDepth and nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex + 1 < wordSearchInfo.wordSearchWidth:
                        nextWordSearchDepthIndex += 1
                        nextWordSearchWidthIndex += 1
                        nextWordSearchHeightIndex -= 1

        if foundWord:
            print(wordList.pop(word),"was found starting at postition [",depth,"][",height,"][",width,"] going in the",direction,"direction") #use this if you just want to find the first instance of the word
            #print(wordList[word],"was found starting at postition [",depth,"][",height,"][",width,"] going in the",direction,"direction") #use this if you just want to find every instance of the word. This has a slower performance



def find3DWordSearchHeight(tempWordsearch):
    height = 0
    for line in tempWordsearch:
        if line:
            height += 1
        else:
            break
    return height


def find3DWordSearchWidth(tempWordsearch):
    for line in tempWordsearch:
        return len(line)


def getTotalNumberOfWordSearchFileLines(tempWordsearch):
    return len(tempWordsearch)

def parse3DWordSearchFromFile(wordSearchFile):
    tempWordSearch = [[n for n in line.split()] for line in wordSearchFile] #tempWordsearch has the right characters, but wrong dimensions, which is why the rest is needed
    print(tempWordSearch)
    height = find3DWordSearchHeight(tempWordSearch) 
    width = find3DWordSearchWidth(tempWordSearch)
    totalNumberOfLines = getTotalNumberOfWordSearchFileLines(tempWordSearch)
    depth = totalNumberOfLines // (height + 2) #the 2 is from the double blank lines that seperates sections of the 3D word search
    print("d:",depth,", h:",height,", w:",width,"total:",totalNumberOfLines)

    wordSearch = [[[0 for _ in range(width)] for _ in range(height)] for _ in range(depth)]
    tempWordSearchHeight = 0
    tempWordSearchWidth = 0
    for k in range(depth):
        for j in range(height):
            for i in range(width):
                wordSearch[k][j][i] = tempWordSearch[tempWordSearchHeight][tempWordSearchWidth]
                if tempWordSearchWidth == width - 1:
                    if tempWordSearch[tempWordSearchHeight + 1] == []:
                        tempWordSearchHeight += 3
                    else:
                        tempWordSearchHeight += 1
                    tempWordSearchWidth = -1
                tempWordSearchWidth += 1

    return wordSearch


def print3DWordSearch(wordSearchInfo):
    for k in range((wordSearchInfo.wordSearchDepth)):
        for j in range(wordSearchInfo.wordSearchHeight):
            print(*wordSearchInfo.wordSearch[k][j])
        print('\n')


def main(): 
    direction = "error"
    wordList = []
    wordListFile = open("WordSearchWords.txt","r")
    wordSearchFile = open("WordSearch.txt","r")
    for line in wordListFile:
        #print(line.rstrip('\n'))
        wordList.append(line.rstrip('\n').upper())  
    wordSearch = parse3DWordSearchFromFile(wordSearchFile)
    wordSearchDepth = len(wordSearch)
    wordSearchHeight = len(wordSearch[0])
    wordSearchWidth = len(wordSearch[0][0])
    wordSearchSize = wordSearchDepth * wordSearchHeight * wordSearchWidth
    openWordSearchSpaces = []
    print("wordSearchDepth:",wordSearchDepth,", wordSearchHeight:",wordSearchHeight,", wordSearchWidth:",wordSearchWidth)
    wordSearchInfo = WordSearchInfo(wordSearch, wordSearchDepth, wordSearchHeight, wordSearchWidth, wordSearchSize, openWordSearchSpaces)
    print3DWordSearch(wordSearchInfo)
    
    #TODO add threads
    for depth in range(len(wordSearch)):
        for height in range(len(wordSearch[depth])):
            for width in range(len(wordSearch[depth][height])):
               # print("d:",depth,", h:",height,", w:",width,", Value:", wordSearchInfo.wordSearch[depth][height][width])
                checkForWord(depth, height, width, wordSearchInfo, wordList)  
    print("words left:",wordList)    

print("solving the word search")
if __name__=="__main__":
    main()  