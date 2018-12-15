__author__ = "Rohit Ravishankar"
__email__ = "rr9105@rit.edu"

import math
import pandas as pd
import seaborn
from scipy.cluster import hierarchy
from matplotlib import pyplot as plt


def read_input(file_name):
    """
    To read the input file and store it in a pandas dataframe
    :param file_name: Input file
    :return: Pandas data frame
    """

    # Reading the shopping data in to a pandas dataframe
    shopping_data = pd.read_csv(file_name, index_col='ID')

    # Cleaning header data
    headers = (shopping_data.columns.str.lower()).str.strip()
    shopping_data.columns = headers

    return shopping_data


def output_correlation_matrix(shopping_data):
    """
    To find the correlation matrix for the shopping data
    :param shopping_data: Data frame containing all the data
    :return: Correlation matrix for the given data
    """
    correlation_matrix = shopping_data.corr()
    return correlation_matrix


def get_eucledian_distance(array_points_i, array_points_j):
    """
    To get the eucledian distance between points in array 1 and corresponding points in array 2
    :param array_points_i: Array of points for row i
    :param array_points_j: Array of points for row j
    :return: Eucledian distance between the points
    """
    total_sum = 0
    for i in range(len(array_points_i)):

        #  eucledian distance for all the attributes
        total_sum = total_sum + math.pow((array_points_i[i] - array_points_j[i]), 2)
    return math.pow(total_sum, 0.5)


def calculate_average(row_1, row_2, count_1, count_2 ):
    """
    Finds the weighted average of the 2 arrays
    :param row_1: Cluster 1 values
    :param row_2: Cluster 2 values
    :param count_1: Count of elements in cluster 1
    :param count_2: Count of elements in cluster 2
    :return: array giving the centroid of combined cluster
    """

    # To calculate the weighted average for the given 2 rows
    return (row_1 * count_1 + row_2 * count_2)/(count_1+count_2)


def find_clusters(shopping_data):
    """
    To find all the clusters in the given shopping data
    :param shopping_data: Data frame containing all the data
    :return:
    """

    # To store each of the row values
    rows_data = dict()

    # To keep count of the points for each of the clusters
    count_clusters = dict()

    # To store all the points in the cluster
    cluster = set()

    # To store information about the last 10 merges
    last_10_cluster_values = []

    # To create each row of data as a cluster of itself
    for rows in range(1, shopping_data['milk'].count() + 1):
        rows_data[rows] = shopping_data.loc[rows].values
        count_clusters[rows] = 1

    # To store the count of the iterations
    idx = 1

    # We want to stop when there are only 3 clusters remaining
    while len(rows_data) > 3:

        # To store the minimum distance and the clusters which are closest
        minimum = math.inf
        cluster_1 = 0
        cluster_2 = 0
        for row_i in rows_data:
            for row_j in rows_data:

                # To find the minimum distance and the clusters which are closest
                if row_i != row_j:
                    eucledian_distance = get_eucledian_distance(rows_data[row_i], rows_data[row_j])

                    # Find the next smallest eucledian distance for the cluster
                    if minimum > eucledian_distance:
                        minimum = eucledian_distance
                        cluster_1 = row_i
                        cluster_2 = row_j

        # Get the rows of data for the best cluster choices
        row_1 = rows_data[cluster_1]
        row_2 = rows_data[cluster_2]

        # Get the count for the rows of data for the best cluster choices
        count_1 = count_clusters[cluster_1]
        count_2 = count_clusters[cluster_2]

        # Calculate the distance between the cluster centers
        row_average = calculate_average(row_1, row_2, count_1, count_2)

        # Once the cluster is created pop the original data points
        rows_data.pop(cluster_1)
        rows_data.pop(cluster_2)
        count_clusters.pop(cluster_1)
        count_clusters.pop(cluster_2)

        # The center of mass of a set of records, to represent
        # its center location in data space
        center = str(cluster_1) + "~" + str(cluster_2)
        cluster.add(center)
        rows_data[center] = row_average
        count_clusters[center] = count_1 + count_2
        minimum_value = min(count_1, count_2)

        # Record clusters at each step
        print("Smaller cluster being merged in for the iteration ", idx, "is of size: ", minimum_value)

        # This is to append the last 10 clusters
        if len(rows_data) <= 13:
            last_10_cluster_values.append(minimum_value)
        idx = idx + 1

    print("The last 10 merges prior to being left with only 3 clusters:- ")
    for each_value in last_10_cluster_values:
        print(str(each_value))

    print("\nThe size of the last 3 clusters and values are:-")
    for i in rows_data:
        print(str(count_clusters[i]), str(rows_data[i]), "\n")


def plot_dendrogram(shopping_data):
    """
    To plot the dendrogram
    :param shopping_data: Data frame of the shopping data
    :return: None
    """
    table_values = shopping_data.values

    plt.figure()
    plt.xlabel('ID')
    plt.ylabel('Distance')
    plt.title('Agglomerative Clustering')

    # To display only the last 10 merges for the dendrogram
    hierarchy.dendrogram(hierarchy.linkage(table_values, 'centroid'), truncate_mode='lastp', p=10)
    plt.show()


def main(file_name):
    """
    The main calling function for the program
    :param file_name: Input file
    :return: None
    """
    shopping_data = read_input(file_name)
    shopping_data_drop_eggs = shopping_data.drop(columns="eggs")
    print("The correlation matrix is:\n", output_correlation_matrix(shopping_data_drop_eggs))
    output_correlation_matrix(shopping_data_drop_eggs).to_csv(r'./HW06_Ravishankar_Rohit.csv', sep=',', index=False)

    # To plot the heatmap
    seaborn.heatmap(output_correlation_matrix(shopping_data_drop_eggs),
                    xticklabels=output_correlation_matrix(shopping_data_drop_eggs).columns.values,
                    yticklabels=output_correlation_matrix(shopping_data_drop_eggs).columns.values)
    plot_dendrogram(shopping_data_drop_eggs)
    find_clusters(shopping_data_drop_eggs)


if __name__ == '__main__':
    main('HW_AG_SHOPPING_CART_v805.csv')

