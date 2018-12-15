__author__ = "Rohit Ravishankar"
__email__ = "rr9105@rit.edu"

import csv
import math
import numpy as np
import matplotlib.pyplot as plt

np.warnings.filterwarnings('ignore')


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
            speed.append(int(round(float(row[0]))))
            car_not_truck.append(int(row[1]))
            distracted.append(int(row[2]))
            commercial.append(int(row[3]))
            want_to_speed.append(int(row[4]))

    return speed, car_not_truck, distracted, commercial, want_to_speed


# Helper function for Otsu's method for 1D Clustering
def get_points(threshold, thresholds):
    """
    Get number of points over the threshold and under the threshold
    :param threshold: Threshold value
    :param thresholds: List of all points
    :return: List of points under threshold and list of points over threshold
    """
    # List to store points under the threshold and over the threshold
    under_threshold = []
    over_threshold = []

    # To iterate over the list of thresholds
    for i in range(len(thresholds)):
        if thresholds[i] <= threshold:
            under_threshold.append(thresholds[i])
        else:
            over_threshold.append(thresholds[i])
    return under_threshold, over_threshold


def otsus_method(thresholds):
    """
    Implement Otsu's method for 1D clustering on the data
    :param thresholds: Data points for Otsu's method
    :return: Largest_cluster, smallest_cluster, best_threshold, best_mixed_variance
    """
    best_mixed_variance = math.inf
    best_threshold = math.inf

    # To maintain a subset of the largest cluster & smallest cluster
    largest_cluster = []
    smallest_cluster = []

    for threshold in thresholds:

        # Points under threshold
        under_threshold, over_threshold = get_points(threshold, thresholds)

        # To find the fraction of points under and over the threshold
        points_under_threshold = len(under_threshold)
        points_over_threshold = len(over_threshold)

        # Total number of points in consideration
        total_points = points_under_threshold + points_over_threshold

        # To find the fraction of points & variance of points under the threshold
        wt_under = points_under_threshold/total_points
        var_under = np.var(under_threshold)

        # To find the fraction of points & variance of points over the threshold
        wt_over = points_over_threshold/total_points
        var_over = np.var(over_threshold)

        mixed_variance = float(wt_under) * float(var_under) + float(wt_over) * float(var_over)

        # Smaller of the 2 clusters from 1co update value of mixed variance
        if mixed_variance < best_mixed_variance:
            best_mixed_variance = mixed_variance
            best_threshold = threshold

            # To find the largest cluster
            if len(over_threshold) < len(under_threshold):
                largest_cluster = under_threshold
                smallest_cluster = over_threshold
            else:
                largest_cluster = over_threshold
                smallest_cluster = under_threshold
    return largest_cluster, smallest_cluster, best_threshold, best_mixed_variance


def threshold_setting(list_of_speeds, want_to_speed):
    """
    To perform threshold setting on the data
    :param list_of_speeds: List of speeds
    :param want_to_speed: To check if the driver actually wanted to speed
    :return: best threshold, best cost function value, false alarm rate, true positive rate, cost function list, \
    """

    # To store best values
    best_cost_func_yet = math.inf
    false_alarm_rate = []
    true_pos_rate = []
    cost_func_list = []
    cost_func_eq_wt_list = []

    for threshold in list_of_speeds:

        # Initializing True Positive, True Negative, False Positive, False Negative
        TN = TP = FP = FN = 0

        for speed_idx in range(len(list_of_speeds)):

            # To calculate TP, TN, FP, FN
            if list_of_speeds[speed_idx] < threshold:

                if want_to_speed[speed_idx] == 1:
                    FN += 1

                else:
                    TN += 1

            else:
                if want_to_speed[speed_idx] == 1:
                    TP += 1
                else:
                    FP += 1

        cost_func = FN + 3 * FP

        # threshold value computed for equal weights gives a value of 63

        cost_func_list.append(cost_func)
        cost_func_eq_wt_list.append(FN+FP)

        #  Variable to store the sum of FP+TN
        x = FP + TN

        #  Variable to store the sum of TP+FN
        y = TP + FN

        false_alarm_rate.append(FP/x)
        true_pos_rate.append(TP/y)

        if cost_func <= best_cost_func_yet:
            best_cost_func_yet = cost_func
            best_threshold_to_use = threshold

    return best_threshold_to_use, best_cost_func_yet, false_alarm_rate, true_pos_rate, cost_func_list, \
           cost_func_eq_wt_list


def aggressive_drivers(best_threshold, speed, wants_to_speed):
    """
    To return number of aggressive drivers
    :param best_threshold: Best threshold value
    :param speed: List of speed
    :param wants_to_speed: List of want_to_speed
    :return: number of aggressive drivers
    """
    aggresive = 0

    for i in range(len(speed)):
        # Aggressive drivers
        if speed[i] < best_threshold and wants_to_speed[i] == 1:
            aggresive += 1

    return aggresive


def non_reckless_drivers(best_threshold, speed, wants_to_speed):
    """
    To return number of non-reckless drivers caught
    :param best_threshold: Best threshold value
    :param speed: List of speed
    :param wants_to_speed: List of want_to_speed
    :return: number of aggressive drivers
    """
    non_reckless = 0

    for i in range(len(speed)):
        # Non-reckless drivers
        if speed[i] >= best_threshold and wants_to_speed[i] == 0:
            non_reckless += 1

    return non_reckless


def plot_threshold_vs_cost(speed, cost_func_list, cost_func_eq_wt_list):
    """
    Plot threshold vs cost function
    :param speed: List of speeds
    :param cost_func_list: List of the cost function values
    :param cost_func_eq_wt_list: List of the cost function values with equal weights
    :return: None
    """
    plt.plot(speed, cost_func_list, label='Cost function: FN+3*FP')
    plt.plot(speed,cost_func_eq_wt_list, label='Cost function: FN+FP')
    plt.legend()
    plt.xlabel('Threshold speeds (in mph)')
    plt.ylabel('Cost function')
    plt.title('Plot of the cost function as a function of thresholds used')
    plt.show()


def ROC_Curve(false_alarm_rate, true_positive_rate, false_alarm_rate_point, true_positive_rate_point):
    """
    To plot the ROC curve
    :param false_alarm_rate: The false alarm rate
    :param true_positive_rate: The true positive rate
    :param false_alarm_rate_point: false alarm rate point when cost function is minimum
    :param true_positive_rate_point: true positive rate point when cost function is minimum
    :return: None
    """
    plt.plot(false_alarm_rate, true_positive_rate)
    plt.plot(false_alarm_rate_point, true_positive_rate_point, marker='o')
    plt.xlabel("False positive rate")
    plt.title('ROC Curve - Threshold is 65 mph')
    plt.ylabel("True positive rate")
    plt.show()


def main(file_path):
    """
    The main calling function to other functions
    :param file_path: File path of the input file
    :return:
    """
    speed, car_not_truck, distracted, commercial, want_to_speed = data_cleaning(file_path)

    sorted_speed, want_to_speed = [list(x) for x in zip(*sorted(zip(speed, want_to_speed), key=lambda pair:pair[0]))]

    best_threshold, best_cost_func_yet, false_alarm_rate, true_pos_rate, cost_func_list, cost_func_eq_wt_list = \
        threshold_setting(sorted_speed, want_to_speed)

    # To find the number of non-reckless and aggressive drivers
    aggressive = aggressive_drivers(best_threshold, sorted_speed, want_to_speed)
    non_reckless = non_reckless_drivers(best_threshold, sorted_speed, want_to_speed)

    print("The best threshold when using Clustering is: " + str(best_threshold))
    print("The number of aggressive drivers let through: " + str(aggressive))
    print("The number of non-reckless drivers pulled over: " + str(non_reckless))
    print("The threshold when using Otsu's method is: " + str(otsus_method(speed)[2]))

    # To plot the threshold vs cost graph
    plot_threshold_vs_cost(sorted_speed, cost_func_list, cost_func_eq_wt_list)

    false_alarm_rate_point = 0
    true_pos_rate_point = 0
    for i in range(len(sorted_speed)):
        if sorted_speed[i] == best_threshold:
            false_alarm_rate_point = false_alarm_rate[i]
            true_pos_rate_point = true_pos_rate[i]
            break

    # To plot ROC curve
    ROC_Curve(false_alarm_rate, true_pos_rate, false_alarm_rate_point, true_pos_rate_point)


if __name__ == "__main__":
    main('vehicle_data_v2181.csv')

