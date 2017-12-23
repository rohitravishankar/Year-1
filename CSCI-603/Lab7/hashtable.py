__author__ = 'zjb'
__author__ = 'Rohit Ravishankar rr9105@rit.edu'
__author__ = 'Parinitha Nagaraja pn4972@rit.edu'

import re
from collections import namedtuple

Entry = namedtuple('Entry', ('key', 'value'))

'''
To make sure that the DELETED sentinel does not match
anything we actually want to have in the table, make it
a unique (content-free!) object.
'''
class _delobj: pass
DELETED = Entry(_delobj(),None)

class Hashmap:

    __slots__ = 'table','numkeys','cap','maxload', 'numberOfProbes', 'numberOfCollisions', 'hashFunction'

    def __init__(self,initsz=100,maxload=0.7,hashFunction='hash_func'):
        '''
        Creates an open-addressed hash map of given size and maximum load factor
        :param initsz: Initial size (default 100)
        :param maxload: Max load factor (default 0.7)
        '''
        self.hashFunction = hashFunction
        self.numberOfCollisions = 0
        self.numberOfProbes = 0
        self.cap = initsz
        self.table = [None for _ in range(self.cap)]
        self.numkeys = 0
        self.maxload = maxload

    def put(self,key, value = 1):
        '''
        Adds the given (key,value) to the map, replacing entry with same key if present.
        :param key: Key of new entry
        :param value: Value of new entry
        '''

        # Based on the command line argument the hash function is picked
        # Default hash function used is the python hash
        if self.hashFunction is 'hash_func_using_prime_number':
            index = self.hash_func_using_prime_number(key) % self.cap
        elif self.hashFunction is 'hash_func_using_location_of_character':
            index = self.hash_func_using_location_of_character(key) % self.cap
        else:
            index = self.hash_func(key) % self.cap
        if self.table[index] is not None and \
                        self.table[index] != DELETED and \
                        self.table[index].key != key:
            self.numberOfCollisions += 1
        while self.table[index] is not None and \
                        self.table[index] != DELETED and \
                        self.table[index].key != key:
            self.numberOfProbes += 1
            index += 1
            if index == len(self.table):
                index = 0
        # To account for when position is found
        self.numberOfProbes += 1
        if self.table[index] is None:
            self.numkeys += 1
        if self.contains(key) == False:
            self.table[index] = Entry(key, value)
        else:
            self.table[index] = Entry(key, self.get(key) + 1 )
        if self.numkeys/self.cap > self.maxload:
            # rehashing
            oldtable = self.table
            # refresh the table
            self.cap *= 2
            self.table = [None for _ in range(self.cap)]
            self.numkeys = 0
            self.numberOfCollisions = 0
            self.numberOfProbes = 0
            # put items in new table
            for entry in oldtable:
                if entry is not None:
                    self.put(entry[0], entry[1])


    def remove(self,key):
        '''
        Remove an item from the table
        :param key: Key of item to remove
        :return: Value of given key
        '''
        if self.hashFunction is 'hash_func_using_prime_number':
            index = self.hash_func_using_prime_number(key) % self.cap
        elif self.hashFunction is 'hash_func_using_location_of_character':
            index = self.hash_func_using_location_of_character(key) % self.cap
        else:
            index = self.hash_func(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is not None:
            self.table[index] = DELETED


    def get(self,key):
        '''
        Return the value associated with the given key
        :param key: Key to look up
        :return: Value (or KeyError if key not present)
        '''
        if self.hashFunction is 'hash_func_using_prime_number':
            index = self.hash_func_using_prime_number(key) % self.cap
        elif self.hashFunction is 'hash_func_using_location_of_character':
            index = self.hash_func_using_location_of_character(key) % self.cap
        else:
            index = self.hash_func(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            self.numberOfProbes += 1
            index += 1
            if index == self.cap:
                index = 0

        # Accounting for the last probe when the keys match or don't match
        self.numberOfProbes += 1
        if self.table[index] is not None:
            return self.table[index].value
        else:
            raise KeyError('Key ' + str(key) + ' not present')

    def contains(self,key):
        '''
        Returns True/False whether key is present in map
        :param key: Key to look up
        :return: Whether key is present (boolean)
        '''
        if self.hashFunction is 'hash_func_using_prime_number':
            index = self.hash_func_using_prime_number(key) % self.cap
        elif self.hashFunction is 'hash_func_using_location_of_character':
            index = self.hash_func_using_location_of_character(key) % self.cap
        else:
            index = self.hash_func(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            self.numberOfProbes += 1
            index += 1
            if index == self.cap:
                index = 0

        # Accounting for the last probe when the keys match
        self.numberOfProbes += 1
        return self.table[index] is not None

    def hash_func_using_prime_number(self, key):
        """
        Hash function using prime numbers to calculate hash
        :param key: The key for which we want to calculate the hash
        :return: Hash value of the key
        """
        hash = 7
        for i in range(0, len(key)):
            hash = hash * 31 + ord(key[i])
        return hash

    def hash_func_using_location_of_character(self, key):
        """
        Hash function using location of characters to calculate hash
        :param key: The key for which we want to calculate the hash
        :return: Hash value of the key
        """
        hash = 0
        keyReversed = key[::-1]
        for i in range(0, len(keyReversed)):
            ASCIIValueOfCharacter = ord(keyReversed[i]) - 97
            hash += ASCIIValueOfCharacter * ( 37 ** i )
        return hash

    def hash_func(self,key):
        '''
        Using Python's built in hash function here since we want to
        have repeatable testing...
        :param key: Key to store
        :return: Hash value for that key
        '''
        # if we want to switch to Python's hash function, uncomment this:
        return hash(key)

def printMap(map):
    for i in range(map.cap):
        print(str(i)+": " + str(map.table[i]))

def testFunctionForHashFunctionUsingLocationOfCharacter(textFile):
    print()
    print("Testing Hash Function when using the location of character to hash a key")
    print("====================================================================")
    print()
    load = 10
    while load in range(10, 100):
        testFunctionForHashFunctionUsingLocationOfCharacterHelper(textFile, load)
        load = load + 10
        print()

def testFunctionForHashFunctionUsingLocationOfCharacterHelper(textFile, load):
    map = Hashmap(initsz=5, maxload=(load / 100), hashFunction='hash_func_using_location_of_character')
    with open(textFile) as textFile:
        for line in textFile:
            line = line.lower()
            listOfWords = re.split('\W+', line)
            for i in range(0, len(listOfWords)):
                map.put(listOfWords[i].strip())
    temp = map
    maximumOccuringWordValue = 0
    maximumOccuringWordKey = ""
    for entry in temp.table:
        if entry is not None and entry[0] != str('') and entry[1] > maximumOccuringWordValue:
                maximumOccuringWordKey = entry[0]
                maximumOccuringWordValue = entry[1]
    print("The number of collisions & probes when the load factor is " + str(load / 100) + " is")
    print("Collisions : " + str(map.numberOfCollisions))
    print("Probes : " + str(map.numberOfProbes))
    print("Maximum Occuring Key : " + str(maximumOccuringWordKey) + "\t|    Maximum Occuring Value : " + str(
        maximumOccuringWordValue))


def testFunctionForHashFunctionUsingPrimeNumbers(textFile):
    print()
    print("Testing Hash Function when using prime numbers to hash a key")
    print("====================================================================")
    print()
    load = 10
    while load in range(10, 100):
        testFunctionForHashFunctionUsingPrimeNumbersHelper(textFile, load)
        load = load + 10
        print()

def testFunctionForHashFunctionUsingPrimeNumbersHelper(textFile, load):
    map = Hashmap(initsz=5, maxload=(load / 100), hashFunction='hash_func_using_prime_number')
    with open(textFile) as textFile:
        for line in textFile:
            line = line.lower()
            listOfWords = re.split('\W+', line)
            for i in range(0, len(listOfWords)):
                map.put(listOfWords[i].strip())
    temp = map
    maximumOccuringWordValue = 0
    maximumOccuringWordKey = ""
    for entry in temp.table:
        if entry is not None and entry[0] != str('') and entry[1] > maximumOccuringWordValue:
                maximumOccuringWordKey = entry[0]
                maximumOccuringWordValue = entry[1]
    print("The number of collisions & probes when the load factor is " + str(load / 100) + " is")
    print("Collisions : " + str(map.numberOfCollisions))
    print("Probes : " + str(map.numberOfProbes))
    print("Maximum Occuring Key : " + str(maximumOccuringWordKey) + "\t|    Maximum Occuring Value : " + str(
        maximumOccuringWordValue))

def testFunctionForHashFunctionUsingPythonHashFunction(textFile):
    print()
    print("Testing Hash Function when using the python hash function")
    print("====================================================================")
    print()
    load = 10
    while load in range(10, 100):
        testFunctionForHashFunctionUsingPythonHashFunctionHelper(textFile, load)
        load = load + 10
        print()

def testFunctionForHashFunctionUsingPythonHashFunctionHelper(textFile, load):
    map = Hashmap(initsz=5, maxload=(load / 100))
    with open(textFile) as textFile:
        for line in textFile:
            line = line.lower()
            listOfWords = re.split('\W+', line)
            for i in range(0, len(listOfWords)):
                map.put(listOfWords[i].strip())
    temp = map
    maximumOccuringWordValue = 0
    maximumOccuringWordKey = ""
    for entry in temp.table:
        if entry is not None and entry[0] != str('') and entry[1] > maximumOccuringWordValue:
                maximumOccuringWordKey = entry[0]
                maximumOccuringWordValue = entry[1]
    print("The number of collisions & probes when the load factor is " + str(load / 100) + " is")
    print("Collisions : " + str(map.numberOfCollisions))
    print("Probes : " + str(map.numberOfProbes))
    print("Maximum Occuring Key : " + str(maximumOccuringWordKey) + "\t|    Maximum Occuring Value : " + str(maximumOccuringWordValue))


def main():
    textFile = input("Enter the filename containing the text information: ")
    testFunctionForHashFunctionUsingLocationOfCharacter(textFile)
    testFunctionForHashFunctionUsingPrimeNumbers(textFile)
    testFunctionForHashFunctionUsingPythonHashFunction(textFile)

if __name__ == '__main__':
    main()
