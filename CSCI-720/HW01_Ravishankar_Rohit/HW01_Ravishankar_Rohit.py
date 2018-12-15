__author__ = "Rohit Ravishankar"
__email__ = "rr9105@rit.edu"

import csv
import random
import math
import numpy as np
import matplotlib.pyplot as plt

np.warnings.filterwarnings('ignore')

# To seperate out the values with the stop time duration less than 0.5s
STOP_TIME_DURATION_LIMIT = 0.5


# Parzen Estimation Parameter
# Window size
h = 1000

# Cube dimension
d = 1

# Volume of cube
V = (h ** d)


def task_1a(file_path):
    """
    To create a list with values which are greater than 0.5 seconds
    :param file_path: File path of the input file
    :return: List containing data values greater than 0.5s stop time
    """

    # List to store cleaned data
    cleaned_data = []

    with open(file_path) as input_file:
        input_file_reader = csv.reader(input_file)

        # To skip the header while reading
        next(input_file_reader)

        for row in input_file_reader:

            # If the element at position 2 is less than 0.5s we want to add that record to another CSV file
            if float(row[1]) >= STOP_TIME_DURATION_LIMIT:

                # Append the cleaned data in a float format to the list
                cleaned_data.append(float(row[1]))
    return cleaned_data


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


# Helper function for Parzen Window estimation
def count_rows(file_path):
    """
    To count the number of rows in a given file at the file path
    :param file_path: Path to the file
    :return: Number of rows in the file
    """
    with open(file_path) as input_file:
        input_file_reader = csv.reader(input_file)

        # To skip the header lines
        next(input_file_reader)

        # To count the number of rows
        row_count = sum(1 for _ in input_file_reader)

    return row_count


def task_2a(file_path):
    """
    Plot the input data, or a sub-set of it, against random noise
    :param file_path: file path to input file
    :return: None
    """
    # To hold values that we would need to plot
    x = []
    y = []

    with open(file_path) as input_file:
        input_file_reader = csv.reader(input_file)

        # To skip the header lines
        next(input_file_reader)

        # To count the number of rows
        row_count = count_rows(file_path)

        for i in range(row_count):
            y.append(random.uniform(0, 1))

        # For each row within the input file
        for row in input_file_reader:
            x.append(float(row[1]))

        plt.scatter(x, y, s=2, edgecolors='b', label='Input Data')
        plt.xlabel('Time stopped (in s)')
        plt.ylabel('Random Noise')
        plt.title('Plot of the input data')
        plt.legend()
        plt.show()


def phi_function(x_value, value):
    """
    To implement the Φ for Parzen window estimation
    :param x_value: The point around which the window is centered
    :param value: Value to check if it lies in the window or not
    :return: 1 or 0 based on whether the function lies in the window or not
    """
    # If the point lies outside the window
    if value < (x_value - (h//2)) or value > (x_value + (h//2)):
        return 0
    return 1


def density_estimate_function(k, V, n):
    """
    To calculate the density estimate function for Parzen Window estimation
    :param k: The number of points inside the hypercube
    :param V: The total volume of the hypercube
    :param n: The total number of points in the given file
    :return: Density function estimate
    """
    return k/(n * V)


def task_2c(file_path):
    """
    To perform Parzen Window Estimation on the given data set
    :param file_path: file path to input file
    :return: None
    """

    # Stores th list of stop duration
    list_of_x = []
    with open(file_path) as input_file:
        input_file_reader = csv.reader(input_file)

        # To skip the header while reading
        next(input_file_reader)
        for row in input_file_reader:
            list_of_x.append(float(row[1]))

    # To store the density estimate function values
    f = []

    # Sorting the list for plotting purposes
    list_of_x = sorted(list_of_x)

    for x in list_of_x:

        # This is to store th summation of all phi values calculated. We refresh this to 0 for each iteration
        k = 0

        for xi in list_of_x:

            # To calculate the Φ function value at a cube centered around x
            phi = phi_function(x, xi)

            # To calculate k, i.e., the number of points falling inside the hypercube of side h
            k += phi

        density_estimate = density_estimate_function(k, V, len(list_of_x))
        f.append(density_estimate)
    print(f)
    plt.plot(list_of_x, f)
    plt.xlabel('Time stopped (in s)')
    plt.ylabel('Density Estimate Function')
    plt.title('Parzen Window Estimation')
    plt.show()


def task_1(file_path):
    """
    The main calling function for all subtasks of task 1
    :param file_path: Path of the input data file
    :return:
    """
    # To create a subset of cleaned_data, i.e., no stop durations less than 0.5s
    cleaned_data = task_1a(file_path)

    # List to store lists in order to choose for the next iteration
    list_of_clusters = []

    # Task 1b
    largest_cluster, smallest_cluster, largest_smallest_threshold, largest_smallest_mixed_variance\
        = otsus_method(cleaned_data)

    # Task 1c
    cluster_1, cluster_2, cluster_12_threshold, cluster_12_mixed_variance = \
        otsus_method(largest_cluster)

    list_of_clusters.append(smallest_cluster)
    list_of_clusters.append(cluster_1)
    list_of_clusters.append(cluster_2)
    list_of_clusters.sort(key=lambda s: len(s))

    cluster_3, cluster_4, cluster_34_threshold, cluster_34_mixed_variance = otsus_method(list_of_clusters[-1])

    print("\n")

    # In case you want to check the number of points in each of the clusters
    print("cluster 2: " + str(len(cluster_2)))
    print("cluster 3: " + str(len(cluster_3)))
    print("cluster 4: " + str(len(cluster_4)))
    print("smallest cluster: " + str(len(smallest_cluster)))
    print("\n")

    # In case you want to check the average values in each of the clusters
    print("Smallest cluster average: " + str(sum(smallest_cluster)/len(smallest_cluster)))
    print("Cluster 2 average: " + str(sum(cluster_2)/len(cluster_2)))
    print("Cluster 3 average: " + str(sum(cluster_3) / len(cluster_3)))
    print("Cluster 4 average: " + str(sum(cluster_4) / len(cluster_4)))
    print("\n")

    # In case you want to check the standard deviation in each of the clusters
    print("Smallest cluster standard deviation: " + str(np.std(smallest_cluster)))
    print("Cluster 2 standard deviation: " + str(np.std(cluster_2)))
    print("Cluster 3 standard deviation: " + str(np.std(cluster_3)))
    print("Cluster 4 standard deviation: " + str(np.std(cluster_4)))
    print("\n")

    # In case you want to check the min in each of the clusters
    print("Smallest cluster minimum value: " + str(min(smallest_cluster)))
    print("Cluster 2 minimum value: " + str(min(cluster_2)))
    print("Cluster 3 minimum value: " + str(min(cluster_3)))
    print("Cluster 4 minimum value: " + str(min(cluster_4)))
    print("\n")

    # In case you want to check the max in each of the clusters
    print("Smallest cluster maximum value: " + str(max(smallest_cluster)))
    print("Cluster 2 maximum value: " + str(max(cluster_2)))
    print("Cluster 3 maximum value: " + str(max(cluster_3)))
    print("Cluster 4 maximum value: " + str(max(cluster_4)))


def task_2(file_path):
    """
    The main calling function for all subtasks for task 2
    :return: None
    """
    # task_2a(file_path)
    task_2c(file_path)


if __name__ == "__main__":

    # The file should reside in the same location as the code
    file_path = 'HW_01_Unknown_Data.csv'
    # task_1(file_path)
    task_2(file_path)
