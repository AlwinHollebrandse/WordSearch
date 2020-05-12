import numpy as np 
from WordSearchInfo import WordSearchInfo


def main(): 
    print('solving the word search')

    direction = 'error'
    wordListFile = open('WordSearchWords.txt','r') # TODO change to some random default or frontend provided
    wordSearchFile = open('WordSearch.txt','r') # TODO change to json object
    wordList = [line.rstrip('\n').upper() for line in wordListFile]
    wordSearch = np.array([[letter for letter in line.split()] for line in wordSearchFile])
    
    wordSearchDepth = 1
    wordSearchHeight = len(wordSearch)
    wordSearchWidth = len(wordSearch[0])
    wordSearchInfo = WordSearchInfo(wordSearchHeight = wordSearchHeight, wordSearchWidth = wordSearchWidth, 
        wordSearchDepth = wordSearchDepth, wordList = wordList, wordSearch = wordSearch)
    wordSearchInfo.toString()
    
    foundWordSet = set([])
    # TODO parallelize
    for height in range(wordSearchInfo.wordSearchHeight):
        for width in range(wordSearchInfo.wordSearchWidth):
            checkForWord(height, width, wordSearchInfo, wordList, foundWordSet) 
    print('words not found:', list(set(wordList) - foundWordSet))


def checkForWord(height, width, wordSearchInfo, wordList, foundWordSet):
    for word in reversed(wordList): # for each word in the wordList, itereted backwards so that things can be popped cleanly  
        directionsFoundIn = []
        foundWord = False

        if wordSearchInfo.wordSearch[height][width] == word[0]: 

            # check the right direction
            if width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[height][width + 1] == word[1]:
                # wordSearchInfo.checkWordInDirection(foundWord = foundWord, word = word, direction = 'right', startingHeight = height, startingWidth = width, 
                #     heightChange = 0, widthChange = 1)

                nextWordSearchWidthIndex = width
                for letter,realLetter in enumerate(word):
                    if wordSearchInfo.wordSearch[height][nextWordSearchWidthIndex] == word[letter]:
                        foundWord = True
                        direction = 'right'
                    else:
                        foundWord = False
                        break
                    if nextWordSearchWidthIndex + 1 < wordSearchInfo.wordSearchWidth:
                        nextWordSearchWidthIndex += 1
                if foundWord:
                    directionsFoundIn.append(direction)
                    foundWord = False

            # check the right, down direction
            if height + 1 < wordSearchInfo.wordSearchHeight and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[height + 1][width + 1] == word[1]:
                nextWordSearchWidthIndex = width
                nextWordSearchHeightIndex = height
                for letter,realLetter in enumerate(word):
                    if wordSearchInfo.wordSearch[nextWordSearchHeightIndex][nextWordSearchWidthIndex] == word[letter]:
                        foundWord = True
                        direction = 'rightDown'
                    else:
                        foundWord = False
                        break
                    if nextWordSearchHeightIndex + 1 < wordSearchInfo.wordSearchHeight and nextWordSearchWidthIndex + 1 < wordSearchInfo.wordSearchWidth:
                        nextWordSearchWidthIndex += 1
                        nextWordSearchHeightIndex += 1
                if foundWord:
                    directionsFoundIn.append(direction)
                    foundWord = False

            # check the down direction
            if height + 1 < wordSearchInfo.wordSearchHeight and wordSearchInfo.wordSearch[height + 1][width] == word[1]:
                nextWordSearchHeightIndex = height
                for letter,realLetter in enumerate(word):
                    if wordSearchInfo.wordSearch[nextWordSearchHeightIndex][width] == word[letter]:
                        foundWord = True
                        direction = 'down'
                    else:
                        foundWord = False
                        break
                    if nextWordSearchHeightIndex + 1 < wordSearchInfo.wordSearchHeight:
                        nextWordSearchHeightIndex += 1
                if foundWord:
                    directionsFoundIn.append(direction)
                    foundWord = False

            # check the left, down direction
            if height + 1 < wordSearchInfo.wordSearchHeight and width - 1 >= 0 and wordSearchInfo.wordSearch[height + 1][width - 1] == word[1]:
                nextWordSearchWidthIndex = width
                nextWordSearchHeightIndex = height
                for letter,realLetter in enumerate(word):
                    if wordSearchInfo.wordSearch[nextWordSearchHeightIndex][nextWordSearchWidthIndex] == word[letter]:
                        foundWord = True
                        direction = 'leftDown'
                    else:
                        foundWord = False
                        break
                    if nextWordSearchHeightIndex + 1 < wordSearchInfo.wordSearchHeight and nextWordSearchWidthIndex - 1 >= 0:
                        nextWordSearchWidthIndex += -1
                        nextWordSearchHeightIndex += 1
                if foundWord:
                    directionsFoundIn.append(direction)
                    foundWord = False

            # check the left direction
            if width - 1 >= 0 and wordSearchInfo.wordSearch[height][width - 1] == word[1]:
                nextWordSearchWidthIndex = width
                for letter,realLetter in enumerate(word):
                    if wordSearchInfo.wordSearch[height][nextWordSearchWidthIndex] == word[letter]:
                        foundWord = True
                        direction = 'left'
                    else:
                        foundWord = False
                        break
                    if nextWordSearchWidthIndex - 1 >= 0:
                        nextWordSearchWidthIndex += -1
                if foundWord:
                    directionsFoundIn.append(direction)
                    foundWord = False

            # check the left up direction
            if height - 1 >= 0 and width - 1 >= 0 and wordSearchInfo.wordSearch[height - 1][width - 1] == word[1]:
                nextWordSearchWidthIndex = width
                nextWordSearchHeightIndex = height
                for letter,realLetter in enumerate(word):
                    if wordSearchInfo.wordSearch[nextWordSearchHeightIndex][nextWordSearchWidthIndex] == word[letter]:
                        foundWord = True
                        direction = 'leftUp'
                    else:
                        foundWord = False
                        break
                    if nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex - 1 >= 0:
                        nextWordSearchWidthIndex += -1
                        nextWordSearchHeightIndex += -1
                if foundWord:
                    directionsFoundIn.append(direction)
                    foundWord = False

            # check the up direction
            if height - 1 >= 0 and wordSearchInfo.wordSearch[height - 1][width] == word[1]:
                nextWordSearchHeightIndex = height
                for letter,realLetter in enumerate(word):
                    if wordSearchInfo.wordSearch[nextWordSearchHeightIndex][width] == word[letter]:
                        foundWord = True
                        direction = 'up'
                    else:
                        foundWord = False
                        break
                    if nextWordSearchHeightIndex - 1 >= 0:
                        nextWordSearchHeightIndex += -1
                if foundWord:
                    directionsFoundIn.append(direction)
                    foundWord = False

            # check the right, up direction
            if height - 1 >= 0 and width + 1 < wordSearchInfo.wordSearchWidth and wordSearchInfo.wordSearch[height - 1][width + 1] == word[1]:
                nextWordSearchWidthIndex = width
                nextWordSearchHeightIndex = height
                for letter,realLetter in enumerate(word):
                    if wordSearchInfo.wordSearch[nextWordSearchHeightIndex][nextWordSearchWidthIndex] == word[letter]:
                        foundWord = True
                        direction = 'rightUp'
                    else:
                        foundWord = False
                        break
                    if nextWordSearchHeightIndex - 1 >= 0 and nextWordSearchWidthIndex + 1 < wordSearchInfo.wordSearchWidth:
                        nextWordSearchWidthIndex += 1
                        nextWordSearchHeightIndex += -1
                if foundWord:
                    directionsFoundIn.append(direction)
                    foundWord = False

        for direction in directionsFoundIn:
            print(word, 'was found starting at postition [', height, '][', width, '] going in the', direction, 'direction') # NOTE use this if you just want to find every instance of the word. This has a slower average performance 
            foundWordSet.add(word)

if __name__=='__main__':
    main()
