"""
A module that represents "spots" on the skewer.

Author: Sean Strout @ RITCS
"""

class KebabSpot:
    """
    Class: KebabSpot
    Description: This class is used to represent an individual
        spot on the skewer.  Each spot contains a food item,
        and a reference to the next spot.  
    """

    def __init__(self, item, next):
        """
        Construct a KebabSpot instance.
        :param item: the item (Food) to store at this spot
        :param next: the next KebabSpot on the skewer
        """
        
        pass

    def size(self):
        """
        Return the number of elements from this KebabSpot instance to the end
        of the skewer.
        :return: the number of elements (int)
        """
        
        return 0

    def is_vegan(self):
        """
        Return whether there are all vegetables from this spot to the end of
        the skewer.
        :return True if there are no vegetables from this spot down, 
        False otherwise.
        """
        
        return False

    def has(self, name):
        """
        Return whether there are any vegetable from this spot to the end of
        the skewer.
        :param name: the name (string) being searched for.
        :return True if any of the spots hold a Food item that equals the
        name, False otherwise.
        """
        
        return False

    def string_em(self):
        """
        Return a string that contains the list of items in the skewer from
        this spot down, with a comma after each entry.
        :return A string containing the names of each of the Food items from
        this spot down.
        """

        return ""
