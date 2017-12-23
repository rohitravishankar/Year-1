_author_ = 'Rohit Ravishankar'
_author_ = 'Parinitha Nagaraja'

import sys
import re

"""
CSCI-603: Lab 4
Author: Rohit Ravishankar (rr9105@rit.edu)
Author: Parinitha Nagaraja (pn4872@rit.edu)

This program carries out transformations
"""

def shift(message, index, exponent):
    """
    Right shift a certain character in a string by an exponent
    :param message: Message to be shifted
    :param index: Index that needs to be shifted
    :param exponent: The number of times the character needs to be shifted
    :return: Message after shifting
    """
    asciiCharacterToShift = ord(message[index])
    absoluteExponent = abs(exponent)
    for x in range(0,absoluteExponent):
        if exponent < 0:
            asciiCharacterToShift -= 1
            if asciiCharacterToShift < ord('A'):
                asciiCharacterToShift += 26
        else:
            asciiCharacterToShift += 1
            if asciiCharacterToShift > ord('Z'):
                asciiCharacterToShift -= 26
    return '%s%s%s' % (message[:index], chr(asciiCharacterToShift), message[index + 1:])

def switchCaseOfLetters(message):
    """
    Function to implement my encryption (Converts the message to lower/uppercase based on input)
    :param message: To encrypt the message
    :return: Converted message
    """
    if message.isupper():
        return message.lower()
    else:
        return message.upper()

def rotate(message, exponent):
    """
    Rotate a message by a given exponent
    :param message: Message to be rotated
    :param exponent: The number of rotations
    :return: Message after rotation
    """
    return message[-exponent:] + message[:-exponent]

def duplicate(message, index, exponent):
    """
    Duplicates the character at index position by exponent number of times
    :param message: Message to be shifted
    :param index: Index that needs to be duplicated
    :param exponent: The number of times the character needs to be duplicated
    :return: Message after duplication
    """
    if exponent < 0:
        return
    characterToDuplicate = message[index]
    for _ in range(0,exponent):
        characterToDuplicate += message[index]
    newString = message[:index] + characterToDuplicate + message[index + 1:]
    return newString

def swap(message, firstIndex, secondIndex):
    """
    Message that needs characters to be swapped
    :param message: Message that will have characters swapped
    :param firstIndex: Index of the first character that needs to be swapped
    :param secondIndex: Index of the second character that needs to be swapped
    :return: Message after swapping the characters
    """
    firstCharacter = message[firstIndex]
    secondCharacter = message[secondIndex]
    return '%s%s%s%s%s' % (message[ : firstIndex], secondCharacter,
                           message[firstIndex + 1 : secondIndex],
                           firstCharacter, message[secondIndex+1 : ])

def swapWithExponent(message, exponent, firstIndex, secondIndex):
    """
    Message that needs characters to be swapped
    :param message: Message that will have characters swapped
    :param firstIndex: Index of the first character that needs to be swapped
    :param secondIndex: Index of the second character that needs to be swapped
    :param exponent: Number of divisions
    :return: Message after swapping the characters
    """
    divisionOfMessage = []
    startIndexOfString = 0
    lengthOfEachDivision = int(len(message)/exponent)
    for i in range(0, len(message)):
        divisionOfMessage.append(message[startIndexOfString : (startIndexOfString + lengthOfEachDivision)])
        startIndexOfString = startIndexOfString + lengthOfEachDivision
    temporaryStore = divisionOfMessage[firstIndex]
    divisionOfMessage[firstIndex] = divisionOfMessage[secondIndex]
    divisionOfMessage[secondIndex] = temporaryStore
    return "".join(divisionOfMessage)

def transformationHelper(transformationsToBeDone, transformationList, i, word):
    if transformationsToBeDone[0] == 'S' and "," not in transformationList[i]:
        transformationOfWord = shift(word, int(transformationsToBeDone[1]), 1)
        return transformationOfWord
    elif transformationsToBeDone[0] == 'S':
        transformationOfWord = shift(word, int(transformationsToBeDone[1]),
                                     int(transformationsToBeDone[3:len(transformationsToBeDone)]))
        return transformationOfWord
    elif transformationsToBeDone[0] == 'D' and "," not in transformationList[i]:
        transformationOfWord = duplicate(word, int(transformationsToBeDone[1]), 1)
        return transformationOfWord
    elif transformationsToBeDone[0] == 'D':
        transformationOfWord = duplicate(word, int(transformationsToBeDone[1]),
                                         int(transformationsToBeDone[3:len(transformationsToBeDone)]))
        return transformationOfWord
    elif transformationsToBeDone[0] == 'T' and transformationsToBeDone[1] != '(' and transformationsToBeDone[1] != '-' and \
                    transformationsToBeDone[3] != '-':
        transformationOfWord = swap(word, int(transformationsToBeDone[1]), int(transformationsToBeDone[3]))
        return transformationOfWord
    elif transformationsToBeDone[0] == 'T' and (
                transformationsToBeDone[2] != '-' or transformationsToBeDone[4] != '-' or transformationsToBeDone[6] != '-'):
        transformationOfWord = swapWithExponent(word, int(transformationsToBeDone[2]), int(transformationsToBeDone[4]),
                                                int(transformationsToBeDone[6]))
        return transformationOfWord
    elif re.search("R(-)?(\d+)",transformationsToBeDone):
        transformationOfWord = rotate(word, int(transformationsToBeDone[1:len(transformationsToBeDone)]))
        return transformationOfWord
    elif re.search("R",transformationsToBeDone):
        transformationOfWord = rotate(word, 1)
        return transformationOfWord
    elif transformationsToBeDone[0] == 'C':
        transformationOfWord = switchCaseOfLetters(word)
        return transformationOfWord
    else:
        return


def main():
    """
    Main calling function
    :return: None
    """
    with open(sys.argv[1]) as wordFile, open(sys.argv[2]) as transformationFile:
        print("Word\tTransformation")
        for word, transformation in zip(wordFile, transformationFile):
            word = word.strip()
            transformation = transformation.strip()
            transformationList = transformation.split(";")
            for i in range(0, len(transformationList)):
                transformationsToBeDone = transformationList[i]
                if i == 0:
                    transformationOfWord = transformationHelper(transformationsToBeDone, transformationList, i, word)
                else:
                    transformationOfWord = transformationHelper(transformationsToBeDone, transformationList, i, transformationOfWord)
            print('%s\t%s' % (word, transformationOfWord))

if __name__ == '__main__':
    main()