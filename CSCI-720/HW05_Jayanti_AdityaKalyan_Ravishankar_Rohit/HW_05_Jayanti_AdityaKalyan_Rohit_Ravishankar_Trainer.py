__author__ = "Aditya Kalyan Jayanti & Rohit Ravishankar"
__email__ = "aj8582@rit.edu & rr9105@rit.edu"

import csv
import math


# Stopping condition
PURITY = 0.95

# Classes for attributes
CUPCAKE = "0"
MUFFIN = "1"


# 2.a)
def read_input(filename):
    """
    To read the input of the file
    :param filename: File path of the input file
    :return: Data for the attributes, attribute names, row indices
    """
    # A flag to get all only the headers
    flag = 1

    # To store all the data
    columns_with_data = {}

    # List of names of the attributes
    attributes = []
    with open(filename) as file:
        file_reader = csv.reader(file, delimiter=",")
        for rows in file_reader:
            if flag:
                for row in rows:

                    # Creating lists for column names in the dictionary
                    if row != "":
                        temp = row.strip()
                        columns_with_data[temp] = []
                        attributes.append(temp)
                    flag = 0
            else:

                # Appending values to the list corresponding to the column names in the dictionary
                for values in range(len(attributes)):
                    if values == 0:
                        columns_with_data[attributes[values]].append(rows[values])
                    else:
                        quantity = float(rows[values])
                        columns_with_data[attributes[values]].append(quantity)

    #  To create a list of indices for the rows
    no_of_rows = [x for x in range(len(columns_with_data[attributes[1]]))]

    return columns_with_data, attributes, no_of_rows


# 2.b)
def emit_header(filename):
    """
    Opens up a file pointer to classifier file and writes header
    :param filename: Filename of the file to write to
    :return: file pointer
    """
    file = open(filename, "w")
    file.write('__author__= "Aditya Kalyan Jayanti & Rohit Ravishankar"\n__email__= "aj8582@rit.edu & rr9105@rit.edu" ')
    file.write("\n\n\ndef classifier(csv_file):\n")
    file.write("\n\t# To write the result of classification\n")
    file.write("\tfile = open('HW_05_Jayanti_AdityaKalyan_Ravishankar_Rohit_MyClassifications.csv','w')\n")
    file.write("\trows = csv_file.readlines()\n")
    file.write("\n\t# Dictionary to store each row of data\n")
    file.write("\tcolumns_with_data = {}\n")
    file.write("\n\t# To store column headers in a list\n")
    file.write("\tattributes = []\n")
    file.write("\tattributes_name = rows[0].split(',')\n")
    file.write("\tfor attribute in attributes_name:\n")
    file.write("\t\tcolumns_with_data[attribute]=0\n")
    file.write("\t\tattributes.append(attribute)\n")
    file.write("\n\t# Iterating from 1 through all rows because the first row has only headers \n")
    file.write("\tfor index in range(1,len(rows)):\n")
    file.write("\t\tline = rows[index].split(',')\n")
    file.write("\t\tline=line[0:len(rows[0])]\n")
    file.write("\t\tfor i in range(1,len(line)):\n")
    file.write("\t\t\tcolumns_with_data[attributes[i]]= float(line[i])\n")

    return file


# 2.c)
def emit_classifier(file):
    """
    Opens up a file pointer to classifier file and writes classifier
    :param file: Filename of the file to write to
    :return: None
    """
    file.write("\t\tmy_classifier_function(file, columns_with_data)\n")
    file.write("\n\ndef my_classifier_function(file, columns_with_data):\n")


# 2.d)
def emit_trailer(file):
    """
    Opens up a file pointer to classifier file and writes trailer
    :param file: Filename of the file to write to
    :return: None
    """
    file.write("\n\ndef main():\n")
    file.write("\n\t# for any new validation set, the path must be entered here\n")
    file.write("\tcsv_file = open('Recipes_For_VALIDATION_2181_RELEASED_v202.csv', 'r')\n")
    file.write("\tclassifier(csv_file)\n\n")
    file.write("\nif __name__ == '__main__':\n")
    file.write("\tmain()\n")


# 2.e)
def emit_decision_tree(file, columns_with_data, attributes, no_of_rows, level=2, left_or_right="N"):
    """
    To emit the decision tree code by recursively splitting
    :param file: File object to which the decision tree writes
    :param columns_with_data: Dictionary containing all the data
    :param attributes: The names of the attributes
    :param no_of_rows: The list of indices for each subtree
    :param level: The level of the tree the current recursive call is at
    :param left_or_right: The attribute which tells which subtree the call is for. By default it is "N" for neither.
    :return: None
    """
    # To store the best Gini Index, threshold value and attribute name
    best_gini = math.inf
    best_threshold = math.inf
    best_attribute_name = ""

    # The alternative names for the classes
    cupcake = "cupcake"
    Cupcake = "Cupcake"
    muffin = "muffin"
    Muffin = "Muffin"

    # To store the number of cupcakes and muffins greater and lesser than the threshold
    greater_cupcake = 0
    greater_muffin = 0
    smaller_cupcake = 0
    smaller_muffin = 0

    # To store the different splits of the data
    smaller_indices = []
    greater_indices = []

    # Type of item, muffin or cupcake
    item_type = columns_with_data[attributes[0]]

    # Iterate over all the attributes to find the attribute with the least weighted gini index to split on
    for index in range(1, len(attributes)):
        gini_impurity, gini_threshold = calculate_weighted_gini_index(item_type, columns_with_data[attributes[index]],
                                                                      no_of_rows)
        # To find the best gini and best threshold
        if best_gini >= gini_impurity:
            best_gini = gini_impurity
            best_threshold = gini_threshold
            best_attribute_name = attributes[index]

    # Getting the entire column of data for the best attribute
    best_attribute_column = columns_with_data[best_attribute_name]

    # Finding the number of muffins and cupcakes above and below the threshold
    for rows in no_of_rows:
        if best_attribute_column[rows] <= best_threshold:
            if item_type[rows] == cupcake or item_type[rows] == Cupcake:
                smaller_cupcake += 1
            elif item_type[rows] == muffin or item_type[rows] == Muffin:
                smaller_muffin += 1
            smaller_indices.append(rows)
        else:
            if item_type[rows] == cupcake or item_type[rows] == Cupcake:
                greater_cupcake += 1
            elif item_type[rows] == muffin or item_type[rows] == Muffin:
                greater_muffin += 1
            greater_indices.append(rows)

    # To decide the level the of indentation
    spaces = "\t" * level

    file.write(spaces + 'if columns_with_data["' + str(best_attribute_name) + '"]<=' + str(best_threshold) + ":\n")

    recurse_further, winner = should_recurse_further(smaller_cupcake, smaller_muffin)

    # Decision to recurse the left subtree further or not
    if recurse_further:
        emit_decision_tree(file, columns_with_data, attributes, smaller_indices, level + 1, "L")
    else:
        file.write(spaces + "\t" + "file.write('" + winner + "\\n')\n")

    file.write(spaces + "else:\n")

    recurse_further, winner = should_recurse_further(greater_cupcake, greater_muffin)

    # Decision to recurse the right subtree further or not
    if recurse_further:
        emit_decision_tree(file, columns_with_data, attributes, greater_indices, level + 1, "R")
    else:
        file.write(spaces + "\t" + "file.write('" + winner + "\\n')\n")


def should_recurse_further(cupcake_count, muffin_count):
    """
    To define the stopping condition
    :param cupcake_count: The number of cupcakes
    :param muffin_count: The number of muffins
    :return: Should recurse further or not based on purity and the winner
    """
    # To get the purity for each node
    purity = max(cupcake_count, muffin_count)/(cupcake_count + muffin_count)

    # To decide the winner
    if cupcake_count > muffin_count:
        winner = CUPCAKE
    else:
        winner = MUFFIN

    if purity > PURITY:
        return False, winner
    else:
        return True, winner


def calculate_weighted_gini_index(item_type, data, no_of_rows):
    """
    To find the weighted gini index for a given attribute
    :param item_type: Contains name of the attribute
    :param data: Contains data for the
    :param no_of_rows: Contains the number of rows in terms of indices
    :return: Weighted gini index and the threshold value
    """
    cupcake = "cupcake"
    Cupcake = "Cupcake"

    best_gini = math.inf
    best_threshold = 0

    for index in range(int(min(data)), int(max(data)) + 1):

        # To store the number of values below and above the threshold
        number_type_below_1 = 0
        number_type_below_2 = 0
        number_type_above_1 = 0
        number_type_above_2 = 0

        threshold = index

        # To calculate the number of points below and and number of points above the threshold
        for row_idx in no_of_rows:
            if data[row_idx] <= threshold:
                if item_type[row_idx] == cupcake or item_type[row_idx] == Cupcake:
                    number_type_below_1 += 1
                else:
                    number_type_below_2 += 1
            else:
                if item_type[row_idx] == cupcake or item_type[row_idx] == Cupcake:
                    number_type_above_1 += 1
                else:
                    number_type_above_2 += 1

        # To calculate fraction of points below the threshold and above the threshold for the gini index
        if (number_type_below_1 + number_type_below_2) != 0:
            probability_points_below = (number_type_below_1/(number_type_below_1 + number_type_below_2)) ** 2 + \
                             (number_type_below_2/(number_type_below_1 + number_type_below_2)) ** 2
        else:
            probability_points_below = 0.5

        if (number_type_above_1 + number_type_above_2) != 0:
            probability_points_above = (number_type_above_1/(number_type_above_1 + number_type_above_2)) ** 2 + \
                             (number_type_above_2 / (number_type_above_1 + number_type_above_2)) ** 2
        else:
            probability_points_above = 0.5

        # To find the gini indices for the fraction of points above and below the threshold
        gini_above = 1 - probability_points_above
        gini_below = 1 - probability_points_below

        total_points = number_type_below_2 + number_type_below_1 + number_type_above_1 + number_type_above_2

        if total_points != len(no_of_rows):
            return False

        weighted_gini = (((number_type_above_2 + number_type_above_1)/total_points) * gini_above) +  \
                        (((number_type_below_1 + number_type_below_2)/total_points) * gini_below)

        if weighted_gini <= best_gini:
            best_gini = weighted_gini
            best_threshold = threshold

    return best_gini, best_threshold


def main():
    """
    Main calling function of the program
    :return: None
    """
    # The file name of the training data
    file_name = "Recipes_For_Release_2181_v202.csv"

    # Emitted file
    emit_filename = "HW_05_Jayanti_AdityaKalyan_Ravishankar_Rohit_Classifier.py"

    # To emit the header
    emit_file = emit_header(emit_filename)

    # To emit the classifier code
    emit_classifier(emit_file)

    # To return the columns of data as a dictionary, attribute names and row indices
    columns_with_data, attributes, no_of_rows = read_input(file_name)

    # To emit the decision tree
    emit_decision_tree(emit_file, columns_with_data, attributes, no_of_rows)

    # To emit the trailer to the file
    emit_trailer(emit_file)


if __name__ == "__main__":
    main()


