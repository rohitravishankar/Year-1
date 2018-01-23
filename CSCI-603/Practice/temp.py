import sys

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


def main():
    with open(sys.argv[1]) as wordFile, open(sys.argv[2]) as transformationFile:
        for x, y in zip(wordFile, transformationFile):
            x = x.strip()
            y = y.strip()
            transformationList = y.split(";")
            for i in range(0, len(transformationList)):
                transformationsInList = transformationList[i]
                if transformationsInList[0] == 'S' and "," not in transformationList[i] :
                    print(shift(x,int(transformationsInList[1]),1))



if __name__ == '__main__':
    main()