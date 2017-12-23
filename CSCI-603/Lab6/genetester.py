from dnalist import DNAList

def initializeGeneForTest():
    # Create a list.
    seq = DNAList()

    # Add values using append.
    for x in "ABCDEF":
        seq.append(x)

    print(seq)
    return seq

def testForAppend():
    print()
    print()
    print("Test for Append")
    print("======================================")
    seq = initializeGeneForTest()

    # print the list(seq)
    print(seq)

    print()
    print("When the entire gene is provided as input")
    seq = DNAList("ACCGT")

    # print the list(seq)
    print(seq)

    print("======================================")

def testForJoin():
    print()
    print()
    print("Test for Join")
    print("======================================")
    seq = initializeGeneForTest()
    newSeq = DNAList()
    for odd in 'U', 'V','W', 'X', 'Y', 'Z':
        newSeq.append(odd)
    print(newSeq)
    # print the list(seq)
    seq.join(newSeq)
    print(seq)

    print("======================================")

def testForCopy():
    print()
    print()
    print("Test for Copy")
    print("======================================")
    seq = initializeGeneForTest()

    newSeq = seq.copy()
    print(newSeq)
    print("======================================")

def testForSnip():
    print()
    print()
    print("Test for Snip")
    print("======================================")

    print("Snip a list at a start index = 1 & end index = 3")
    seq = initializeGeneForTest()

    #Snip a list at a start index & end index lie within the list
    seq.snip(1, 4)
    print(seq)
    print()
    print("Snip a list at a start index = 0 & end index = 2")
    seq = initializeGeneForTest()

    # Snip a list at a start index lies at the beginning of the list
    seq.snip(0, 2)
    print(seq)
    print("======================================")

def testForSplice():
    print()
    print()
    print("Test for Splice")
    print("======================================")

    print("Splice a list at the beginning of the current list")
    seq = initializeGeneForTest()

    newSeq = DNAList()
    # Add values using append.
    for odd in 'U', 'V','W', 'X', 'Y', 'Z':
        newSeq.append(odd)
    print(newSeq)

    #Splice a string
    seq.splice(0,newSeq)
    print(seq)

    print()
    print("Splice a list in the middle of the current list")
    seq = initializeGeneForTest()

    newSeq = DNAList()
    # Add values using append.
    for odd in 'U', 'V','W', 'X', 'Y', 'Z':
        newSeq.append(odd)
    print(newSeq)

    #Splice a string
    seq.splice(2,newSeq)
    print(seq)

    print()
    print("Splice a list at the end of the current list")
    seq = initializeGeneForTest()

    newSeq = DNAList()
    # Add values using append.
    for odd in 'U', 'V','W', 'X', 'Y', 'Z':
        newSeq.append(odd)
    print(newSeq)

    #Splice a string
    seq.splice(5,newSeq)
    print(seq)

    print("======================================")

def testForReplace():
    print()
    print()
    print("Test for Replace")
    print("======================================")

    print()
    print("Replace a string with another list at the beginning of the list")
    seq = initializeGeneForTest()

    newSeq = DNAList()
    # Add values using append.
    for odd in 'W','X', 'Y', 'Z':
        newSeq.append(odd)
    print(newSeq)

    #Replace a string
    seq.replace('ABC',newSeq)
    print(seq)

    print()
    print("Replace a string with another list in the end of the list")
    seq = initializeGeneForTest()
    newSeq = DNAList()
    # Add values using append.
    for odd in 'W','X', 'Y', 'Z':
        newSeq.append(odd)
    print(newSeq)

    #Replace a string
    seq.replace('BCD',newSeq)
    print(seq)

    print()
    print("Replace a string with another list at the end of the list")
    seq = initializeGeneForTest()
    newSeq = DNAList()
    # Add values using append.
    for odd in 'W','X', 'Y', 'Z':
        newSeq.append(odd)
    print(newSeq)

    #Replace a string
    seq.replace('DEF',newSeq)
    print(seq)

    print("======================================")

def main():
    testForAppend()
    testForCopy()
    testForJoin()
    testForSnip()
    testForSplice()
    testForReplace()

if __name__ == "__main__":
    main()