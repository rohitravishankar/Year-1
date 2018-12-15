__author__ = "Rohit Ravishankar"
__email__ = "rr9105@rit.edu"

import csv
import math
import numpy as np
import matplotlib.pyplot as plt

np.warnings.filterwarnings('ignore')


# Bin Size
BIN_SIZE = 1

# SPEED RANGE
LOW = 41
HIGH = 85


def data_cleaning(file_path):
    """
    The main function to clean data.
    :param file_path: File path of input file
    :return:
    """
    # Lists to store cleaned data
    speed = []
    car_not_truck = []
    distracted = []
    want_to_speed = []
    commercial = []

    with open(file_path) as input_file:
        input_file_reader = csv.reader(input_file)

        # To skip the header while reading
        next(input_file_reader)

        for row in input_file_reader:

            # Append the cleaned data in a float format to the list
            speed.append(float(row[0]))
            car_not_truck.append(int(row[1]))
            distracted.append(int(row[2]))
            commercial.append(int(row[3]))
            want_to_speed.append(int(row[4]))

    return speed, car_not_truck, distracted, commercial, want_to_speed


def quantize_bins(list_of_speeds):
    """
    To quantize the list of speeds into bins
    :param list_of_speeds: List of speeds
    :return: Speeds quantized into bins
    """
    list_new_speeds = []

    for i in list_of_speeds:

        # To calculate the list of speeds quantized into bins
        new_speed = round(i/BIN_SIZE) * BIN_SIZE
        list_new_speeds.append(new_speed)
    return list_new_speeds


def less_than_threshold(threshold, list_of_new_speeds, want_to_speed):
    """
    To find speeds less than threshold
    :param threshold: Threshold speed
    :param list_of_new_speeds: list of speeds quanitized into bins
    :return: List of speeds less than threshold and want to speed values corresponding to the speeds
    """
    # Lists to store speeds below threshold and want to speed values corresponding to the speeds
    list_of_speeds_below_threshold = []
    list_of_want_to_speeds_below_threshold = []

    for i in range(len(list_of_new_speeds)):

        # To find all speeds less than threshold and append it to a list
        if list_of_new_speeds[i] < threshold:
            list_of_speeds_below_threshold.append(list_of_new_speeds[i])
            list_of_want_to_speeds_below_threshold.append(want_to_speed[i])

    return list_of_speeds_below_threshold, list_of_want_to_speeds_below_threshold


def greater_than_threshold(threshold, list_of_new_speeds, want_to_speed):
    """
    To find speeds greater than threshold
    :param threshold: Threshold speed
    :param list_of_new_speeds: list of speeds quanitized into bins
    :return: List of speeds less than threshold and want to speed values corresponding to the speeds
    """
    # Lists to store speeds below threshold and want to speed values corresponding to the speeds
    list_of_speeds_above_threshold = []
    list_of_want_to_speeds_above_threshold = []

    for i in range(len(list_of_new_speeds)):

        # To find all speeds less than threshold and append it to a list
        if list_of_new_speeds[i] >= threshold:
            list_of_speeds_above_threshold.append(list_of_new_speeds[i])
            list_of_want_to_speeds_above_threshold.append(want_to_speed[i])

    return list_of_speeds_above_threshold, list_of_want_to_speeds_above_threshold


def probability_of_want_to_speed(list_of_want_to_speed):
    """
    Compute the probability of cars wanting to speed and those not wanting to speed
    :param list_of_want_to_speed: List of want to speed values
    :return: Probability of cars wanting to speed and not wanting to speed
    """
    number_of_want_to_speed = 0
    number_of_not_want_to_speed = 0

    for i in list_of_want_to_speed:

        # If the want_to_speed value is 1 increment number of cars wanting to speed value
        if i == 1:
            number_of_want_to_speed += 1

        # If the want_to_speed value is 0 increment number of cars not wanting to speed value
        else:
            number_of_not_want_to_speed += 1

    # Probability of cars wanting to speed
    probability_of_cars_wanting_to_speed = number_of_want_to_speed/(number_of_want_to_speed +
                                                                    number_of_not_want_to_speed)

    # Probability of cars not wanting to speed
    probability_of_cars_not_wanting_to_speed = number_of_not_want_to_speed/(number_of_want_to_speed +
                                                                    number_of_not_want_to_speed)
    return probability_of_cars_wanting_to_speed, probability_of_cars_not_wanting_to_speed


def mis_class_error_impurity(probability_of_cars_wanting_to_speed, probability_of_cars_not_wanting_to_speed):
    """
    To calculate the missclassification error
    :param probability_of_cars_wanting_to_speed: probability of wanting to speed
    :param probability_of_cars_not_wanting_to_speed: probability of the car not wanting to speed
    :return: Missclassification error
    """
    # misclassification rate = 1 - max(P(i/t))
    return 1 - max(probability_of_cars_wanting_to_speed, probability_of_cars_not_wanting_to_speed)


def gini_index_impurity(probability_of_cars_wanting_to_speed, probability_of_cars_not_wanting_to_speed):
    """
    To calculate the gini index value
    :param probability_of_cars_wanting_to_speed: probability of wanting to speed
    :param probability_of_cars_not_wanting_to_speed: probability of the car not wanting to speed
    :return: gini index value
    """
    # gini index = 1 - sum(P(i/t) ^ 2)
    return 1 - (math.pow(probability_of_cars_wanting_to_speed, 2) +
                math.pow(probability_of_cars_not_wanting_to_speed, 2))


def entropy_impurity(probability_of_cars_wanting_to_speed, probability_of_cars_not_wanting_to_speed):
    """
    To calculate the entropy value
    :param probability_of_cars_wanting_to_speed: probability of wanting to speed
    :param probability_of_cars_not_wanting_to_speed: probability of the car not wanting to speed
    :return: entropy value
    """
    # entropy =  - sum(P(i/t) * log(P(i/t)))
    if probability_of_cars_wanting_to_speed == 0 and probability_of_cars_not_wanting_to_speed != 0:
        return -(probability_of_cars_not_wanting_to_speed * math.log2(probability_of_cars_not_wanting_to_speed))
    elif probability_of_cars_not_wanting_to_speed == 0 and probability_of_cars_wanting_to_speed != 0:
        return -(probability_of_cars_wanting_to_speed * math.log2(probability_of_cars_wanting_to_speed))
    elif probability_of_cars_not_wanting_to_speed == 0 and probability_of_cars_wanting_to_speed == 0:
        return 0
    else:
        return -((probability_of_cars_wanting_to_speed * math.log2(probability_of_cars_wanting_to_speed)) +
                 (probability_of_cars_not_wanting_to_speed * math.log2(probability_of_cars_not_wanting_to_speed)))


def weighted_impurity(list_of_speeds_below_threshold, list_of_speeds_above_threshold, impurity_value_below_threshold,
                      impurity_value_above_threshold):
    """
    To calculate the weighted impurity values
    :param list_of_speeds_below_threshold: List of speeds below threshold
    :param list_of_speeds_above_threshold: List of speeds above threshold
    :param impurity_value_below_threshold: Misclass error, gini index or entropy value for values below threshold
    :param impurity_value_above_threshold: Misclass error, gini index or entropy value for values above threshold
    :return: weighted impurity value
    """
    term_1 = len(list_of_speeds_below_threshold) * impurity_value_below_threshold
    term_2 = len(list_of_speeds_above_threshold) * impurity_value_above_threshold
    return (term_1 + term_2)/(len(list_of_speeds_below_threshold) + len(list_of_speeds_above_threshold))


def impurity(list_of_new_speeds, want_to_speed):
    """
    To calculate measures of impurity
    :param list_of_new_speeds: list of speeds quanitized into bins
    :param want_to_speed: whether driver wants to speed or not
    :return:
    """
    # Lists to store values for the graphs for entropy, gini index and misclassification error
    mis_class_error_below_threshold = []
    gini_index_below_threshold = []
    entropy_below_threshold = []
    mis_class_error_above_threshold = []
    gini_index_above_threshold = []
    entropy_above_threshold = []

    # Weighted values
    mis_class_error_weighted = []
    gini_index_weighted = []
    entropy_weighted = []

    for threshold in range(LOW, HIGH):

        # To get subset of speeds below the threshold
        list_of_speeds_below_threshold, list_of_want_to_speeds_below_threshold = \
            less_than_threshold(threshold, list_of_new_speeds, want_to_speed)

        # Probability of cars wanting to speed and not wanting to speed
        probability_of_cars_wanting_to_speed_below_threshold, probability_of_cars_not_wanting_to_speed_below_threshold \
            = probability_of_want_to_speed(list_of_want_to_speeds_below_threshold)

        # To calculate the impurity values for below the threshold
        mis_class_error_below_threshold.append(mis_class_error_impurity(probability_of_cars_wanting_to_speed_below_threshold,
                                                        probability_of_cars_not_wanting_to_speed_below_threshold))
        gini_index_below_threshold.append(gini_index_impurity(probability_of_cars_wanting_to_speed_below_threshold,
                                                        probability_of_cars_not_wanting_to_speed_below_threshold))
        entropy_below_threshold.append(entropy_impurity(probability_of_cars_wanting_to_speed_below_threshold,
                                                        probability_of_cars_not_wanting_to_speed_below_threshold))

        # To get subset of speeds greater than the threshold
        list_of_speeds_above_threshold, list_of_want_to_speeds_above_threshold = \
            greater_than_threshold(threshold, list_of_new_speeds, want_to_speed)

        # Probability of cars wanting to speed and not wanting to speed
        probability_of_cars_wanting_to_speed_above_threshold, probability_of_cars_not_wanting_to_speed_above_threshold \
            = probability_of_want_to_speed(list_of_want_to_speeds_above_threshold)

        # To calculate the impurity values for above the threshold
        mis_class_error_above_threshold.append(
            mis_class_error_impurity(probability_of_cars_wanting_to_speed_above_threshold,
                                     probability_of_cars_not_wanting_to_speed_above_threshold))
        gini_index_above_threshold.append(gini_index_impurity(probability_of_cars_wanting_to_speed_above_threshold,
                                                              probability_of_cars_not_wanting_to_speed_above_threshold))
        entropy_above_threshold.append(entropy_impurity(probability_of_cars_wanting_to_speed_above_threshold,
                                                        probability_of_cars_not_wanting_to_speed_above_threshold))

        # To calculate impurity values for weighted misclassification error, weighted gini index and weighted entropy
        mis_class_error_weighted.append(weighted_impurity(list_of_speeds_below_threshold,
                                                          list_of_speeds_above_threshold,
                                                          mis_class_error_impurity(
                                                              probability_of_cars_wanting_to_speed_below_threshold,
                                                              probability_of_cars_not_wanting_to_speed_below_threshold),
                                                          mis_class_error_impurity(
                                                              probability_of_cars_wanting_to_speed_above_threshold,
                                                              probability_of_cars_not_wanting_to_speed_above_threshold)
                                                          ))

        gini_index_weighted.append(weighted_impurity(list_of_speeds_below_threshold,
                                                          list_of_speeds_above_threshold,
                                                          gini_index_impurity(
                                                              probability_of_cars_wanting_to_speed_below_threshold,
                                                              probability_of_cars_not_wanting_to_speed_below_threshold),
                                                          gini_index_impurity(
                                                              probability_of_cars_wanting_to_speed_above_threshold,
                                                              probability_of_cars_not_wanting_to_speed_above_threshold)))

        entropy_weighted.append(weighted_impurity(list_of_speeds_below_threshold,
                                                          list_of_speeds_above_threshold,
                                                          entropy_impurity(
                                                              probability_of_cars_wanting_to_speed_below_threshold,
                                                              probability_of_cars_not_wanting_to_speed_below_threshold),
                                                          entropy_impurity(
                                                              probability_of_cars_wanting_to_speed_above_threshold,
                                                              probability_of_cars_not_wanting_to_speed_above_threshold)))

    return mis_class_error_below_threshold, gini_index_below_threshold, entropy_below_threshold, \
           mis_class_error_above_threshold, gini_index_above_threshold, entropy_above_threshold, \
           mis_class_error_weighted, gini_index_weighted, entropy_weighted


def main(file_path):
    """
    Main calling function
    :param file_path: File path of the input file
    :return: None
    """
    speed, car_not_truck, distracted, commercial, want_to_speed = data_cleaning(file_path)
    list_of_new_speeds = quantize_bins(speed)

    # All values to plot
    mis_class_error_below_threshold, gini_index_below_threshold, entropy_below_threshold, \
    mis_class_error_above_threshold, gini_index_above_threshold, entropy_above_threshold, \
    mis_class_error_weighted, gini_index_weighted, entropy_weighted = impurity(list_of_new_speeds, want_to_speed)

    # Plot for thresholds below threshold
    plt.plot(range(LOW, HIGH), mis_class_error_below_threshold, label="Misclassification Error")
    plt.plot(range(LOW, HIGH), gini_index_below_threshold, label="Gini Index")
    plt.plot(range(LOW, HIGH), entropy_below_threshold, label="Entropy")
    plt.title("Plot of impurity values for subset of data")
    plt.xlabel("Speed in range of 41 through 85 mph")
    plt.ylabel("Impurity functions")
    plt.legend()
    plt.show()

    # plot for above threshold
    # plt.plot(range(LOW, HIGH), mis_class_error_above_threshold, label="Misclassification Error")
    # plt.plot(range(LOW, HIGH), gini_index_above_threshold, label="Gini Index")
    # plt.plot(range(LOW, HIGH), entropy_above_threshold, label="Entropy")
    # plt.title("Plot of impurity values for subset of data")
    # plt.xlabel("Speed in range of 41 through 85 mph")
    # plt.ylabel("Impurity functions")
    # plt.legend()
    # plt.show()

    # Plot for weighted values
    plt.plot(range(LOW, HIGH), mis_class_error_weighted, label="Misclassification Error Weighted")
    plt.plot(range(LOW, HIGH), gini_index_weighted, label="Gini Index Weighted")
    plt.plot(range(LOW, HIGH), entropy_weighted, label="Entropy Weighted")
    plt.title("BONUS: Plot of weighted impurity values of data")
    plt.xlabel("Speed in range of 41 through 85 mph")
    plt.ylabel("Impurity functions")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main('HW03_Vehicle_Data__v25.csv')

