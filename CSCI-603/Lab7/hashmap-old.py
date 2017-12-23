__author__ = 'zjb'

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

    def __init__(self,initsz=100,maxload=0.7,hashFunction='hash_func_using_prime_number'):
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

    def put(self,key,value):
        '''
        Adds the given (key,value) to the map, replacing entry with same key if present.
        :param key: Key of new entry
        :param value: Value of new entry
        '''
        if self.hashFunction is 'hash_func_using_prime_number':
            index = self.hash_func_using_prime_number(key) % self.cap
        else:
            index = self.hash_func_using_location_of_character(key) % self.cap
        # index = self.hash_func(key) % self.cap
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
        if self.table[index] is None:
            self.numkeys += 1
        self.table[index] = Entry(key,value)
        if self.numkeys/self.cap > self.maxload:
            # rehashing
            oldtable = self.table
            # refresh the table
            self.cap *= 2
            self.table = [None for _ in range(self.cap)]
            self.numkeys = 0
            # put items in new table
            for entry in oldtable:
                if entry is not None:
                    self.put(entry[0],entry[1])


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
        else:
            index = self.hash_func_using_location_of_character(key) % self.cap
        # index = self.hash_func(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == self.cap:
                index = 0
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
        else:
            index = self.hash_func_using_location_of_character(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == self.cap:
                index = 0
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
            hash += ASCIIValueOfCharacter * ( 26 ** i )
        return hash

    def hash_func(self,key):
        '''
        Not using Python's built in hash function here since we want to
        have repeatable testing...
        However it is terrible.
        Assumes keys have a len() though...
        :param key: Key to store
        :return: Hash value for that key
        '''
        # if we want to switch to Python's hash function, uncomment this:
        #return hash(key)
        return len(key)

def printMap(map):
    for i in range(map.cap):
        print(str(i)+": " + str(map.table[i]))

def testForHashFunctionUsingPrimeNumberHashing():
    map = Hashmap(initsz=5, hashFunction='hash_func_using_prime_number')
    map.put('apple',1)
    map.put('banana',2)
    map.put('orange',15)
    printMap(map)
    print(map.contains('apple'))
    print(map.contains('grape'))
    print(map.get('orange'))
    print(map.numberOfCollisions)
    print(map.numberOfProbes)

    print('--------- adding one more to force table resize ')
    map.put('grape',7)
    printMap(map)

    print('--------- testing remove')
    map.remove('apple')
    printMap(map)

    print('--------- testing add to a DELETED location')
    map.put('peach',16)
    printMap(map)
    print(map.get('grape'))

def testForHashFunctionUsingLocationOfCharacterHashing():
    map = Hashmap(initsz=5, hashFunction='hash_func_using_location_of_character')
    map.put('apple',1)
    map.put('banana',2)
    map.put('orange',15)
    printMap(map)
    print(map.contains('apple'))
    print(map.contains('grape'))
    print(map.get('orange'))
    print(map.numberOfCollisions)
    print(map.numberOfProbes)
    print(map.numberOfCollisions)
    print(map.numberOfProbes)

    print('--------- adding one more to force table resize ')
    map.put('grape',7)
    printMap(map)

    print('--------- testing remove')
    map.remove('apple')
    printMap(map)

    print('--------- testing add to a DELETED location')
    map.put('peach',16)
    printMap(map)
    print(map.get('grape'))


def testMap():
    map = Hashmap(initsz=5, hashFunction='hash_func_using_location_of_character')
    map.put('apple',1)
    map.put('banana',2)
    map.put('orange',15)
    printMap(map)
    print(map.contains('apple'))
    print(map.contains('grape'))
    print(map.get('orange'))
    print(map.numberOfCollisions)
    print(map.numberOfProbes)

    print('--------- adding one more to force table resize ')
    map.put('grape',7)
    printMap(map)

    print('--------- testing remove')
    map.remove('apple')
    printMap(map)

    print('--------- testing add to a DELETED location')
    map.put('peach',16)
    printMap(map)
    print(map.get('grape'))

if __name__ == '__main__':
    # testForHashFunctionUsingLocationOfCharacterHashing()
    testForHashFunctionUsingPrimeNumberHashing()