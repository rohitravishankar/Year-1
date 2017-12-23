"""
A module that represents "spots" on the skewer.

Author:
Sean Strout @ RITCS
Rohit Ravishankar  (rr9105@rit.edu)
Parinitha Nagaraja (pn4972@rit.edu)
"""
import food

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
        self.item = item
        self.next = next

    def size(self):
        """
        Return the number of elements from this KebabSpot instance to the end
        of the skewer.
        :return: the number of elements (int)
        """
        count = 1
        while self.next != None:
            count += 1
            self = self.next
        return count

    def is_vegan(self):
        """
        Return whether there are all vegetables from this spot to the end of
        the skewer.
        :return True if there are no vegetables from this spot down, 
        False otherwise.
        """
        isAllVeggie = False
        while self.next != None:
            if self.item.name in food.VEGGIES:
                isAllVeggie = True
                self = self.next
            else:
                isAllVeggie = False
                return isAllVeggie
        if self.next == None and self.item.name in food.VEGGIES:
            isAllVeggie = True
        return isAllVeggie

    def has(self, name):
        """
        Return whether there are any vegetable from this spot to the end of
        the skewer.
        :param name: the name (string) being searched for.
        :return True if any of the spots hold a Food item that equals the
        name, False otherwise.
        """
        while self.next != None:
            if self.item.name == name:
                return True
            self = self.next
        if self.next == None and self.item.name == name:
            return True
        return False

    def string_em(self):
        """
        Return a string that contains the list of items in the skewer from
        this spot down, with a comma after each entry.
        :return A string containing the names of each of the Food items from
        this spot down.
        """
        listOfItems = []
        while self.next != None:
            listOfItems.append(self.item.name)
            self = self.next
        listOfItems.append(self.item.name)
        return ", ".join(listOfItems)

    def calories(self):
        """
        Return the total calories on the skewer
        :return: the total calories on the skewer
        """
        calories = self.item.numberOfCalories
        while self.next != None:
            self = self.next
            calories += self.item.numberOfCalories
        return calories

