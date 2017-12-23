"""
A module that represents the valid food types.

Author: Sean Strout @ RITCS
Rohit Ravishankar  (rr9105@rit.edu)
Parinitha Nagaraja (pn4972@rit.edu)
"""

# The set of valid food items
FOODS = {'beef', 'pork', 'chicken', 'onion', 'pepper', 'tomato', 'mushroom'}

# The set vegetables
VEGGIES = {'onion', "pepper", 'tomato','mushroom'}

# The calories for each food item (a dictionary, where 
# key = food name (string) and value = calories (int)
CALORIES = {
    'beef': 200,
    'chicken': 140,
    'pork': 100,
    'onion': 30,
    'pepper': 25,
    'tomato': 10,
    'mushroom': 7
}

# Implement Food class here
class Food:
    __slots__ = "name", "is_veggie" , "numberOfCalories"
    def __init__(self, name):

        self.name = name

        if self.name in VEGGIES:
            self.is_veggie = True
        else:
            self.is_veggie = False

        self.numberOfCalories = CALORIES.get(name)

    def __str__(self):
        return str(self.name)