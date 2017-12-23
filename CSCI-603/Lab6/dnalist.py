"""
linkedlist.py

A Linked List interface and implementation in Python
This version uses a cursor. Using indices is inherently inefficient and
hides the strengths of the linked list.
Cursors, immutable, are created by list methods.

author: James Heliotis
Rohit Ravishankar      (rr9105@rit.edu)
Parinitha Nagaraja     (pn4972@rit.edu)
"""

class DNAList:

    __slots__ = '__front', '__back', 'gene'

    def __init__( self, gene='' ):
        """ Create an empty list.
        """
        self.__back = None
        self.__front = None

        next = self.__front
        if len(gene) > 1:
            for i in range(len(gene)):
                newNode = LinkedNode(gene[i])
                if i == 0:
                    self.__front = newNode
                    next = self.__front
                else:
                    next.link = newNode
                    next = next.link
                if i is (len(gene) - 1):
                    self.__back = newNode

        else:
            self.gene = gene

    def append( self, item ):
        """ Add value to the end of the list.
            List is modified.
            :param new_value: the value to add
            :return: None
        """
        newNode = LinkedNode( item )
        if self.__front == None and self.__back == None:
            self.__front = newNode
        else:
            self.__back.link = newNode
        self.__back = newNode

    def copy(self):
        """
        Create a copy of the list
        :return: None
        """
        newList = DNAList()
        old = self.__front

        while old != None:
            newList.append(old.value)
            old = old.link
        return newList


    def __str__(self):
        """ Print the contents of a list on a single line, first to last.
        """
        result = ""
        node = DNAList()
        node.__front = self.__front
        if node.__front != None:
            result += str(node.__front.value)
            node.__front = node.__front.link
            while node.__front:
                result += " " + str(node.__front.value)
                node.__front = node.__front.link
        return result

    def snip(self, i1, i2):
        """
        Removes a portion of the gene from index i1 to i2
        :param i1: starting index (inclusive)
        :param i2: ending index (exclusive)
        :return: None
        """
        cursor = self.__front

        previousPointer = self.__front
        subStringBeginning = self.__front
        nextPointer = self.__front

        counter = 0

        while cursor != None:
            if counter <= (i1 - 2):
                previousPointer = previousPointer.link
            if counter <= (i1 - 1):
                subStringBeginning = subStringBeginning.link
            if counter <= (i2 - 1):
                nextPointer = nextPointer.link

            cursor = cursor.link
            counter += 1

        if subStringBeginning.value == previousPointer.value :
            self.__front = nextPointer
        else:
           previousPointer.link = nextPointer
        return self

    def join(self, other):
        """
        :param other:
        :return:
        """
        self.__back.link = other.__front
        self.__back = other.__back


    def replace(self, repstr, other):

        headPointer = LinkedNode(None, self.__front)
        cursor = headPointer
        cursor1 = headPointer
        stringBeginningPointer = headPointer


        # To traverse the string that needs to be replaced
        counter = 0

        while cursor != None:
            if cursor1.link.value == repstr[counter]:
                stringBeginningPointer = cursor1
            elif cursor1.value != repstr[counter]:
                pass
            else:
                pass
            while counter < len(repstr):
                if cursor1 == None:
                    return self
                elif cursor1.value == repstr[counter]:
                    cursor1 = cursor1.link
                    counter += 1
                else:
                    break
            if counter == len(repstr):
                if stringBeginningPointer.link == self.__front:
                    self.__front = other.__front
                else:
                    stringBeginningPointer.link = other.__front
                other.__back.link = cursor1
                break

            counter = 0
            if cursor1.link != None:
                cursor1 = cursor1.link
            cursor = cursor.link
        return self


    def splice(self, ind, other):

        index = 0

        cursor = self.__front
        previousPointer = self.__front
        nextPointer = self.__front

        if ind == 0:

            # If the index is = 0 splice list at the beginning
            previousPointer = other.__front
            other.__back.link = self.__front
            self.__front = previousPointer
        else:
            while cursor != None:

                # For the case where the list isn't being spliced at the end
                if index == ind and cursor.link != None:
                    cursor = cursor.link
                    nextPointer = previousPointer.link
                    previousPointer.link = other.__front
                    other.__back.link = nextPointer

                # For the case where the list is being spliced at the end
                elif index == ind and cursor.link == None:
                    cursor.link = other.__front
                    self.__back = other.__back
                    break

                else:
                    previousPointer = previousPointer.link
                cursor = cursor.link
                index += 1
            cursor = self.__front
        return self

"""
node.py
author: James heliotis
description: A linkable node class for use in stacks, queues, and linked lists
"""

class LinkedNode:

    __slots__ = "value", "link"

    def __init__( self, value, link = None ):
        """ Create a new node and optionally link it to an existing one.
            param value: the value to be stored in the new node
            param link: the node linked to this one
        """
        self.value = value
        self.link = link

    def __str__( self ):
        """ Return a string representation of the contents of
            this node. The link is not included.
        """
        return str( self.value )

    def __repr__( self ):
        """ Return a string that, if evaluated, would recreate
            this node and the node to which it is linked.
            This function should not be called for a circular
            list.
        """
        return "LinkedNode(" + repr( self.value ) + "," + \
               repr( self.link ) + ")"

