__author__ = "Rohit Ravishankar"
__email__ = "rr9105@rit.edu"

import pandas as pd
import numpy as np
import math
from matplotlib import pyplot as plt
from numpy import linalg
from sklearn.cluster import KMeans


def read_input(file_name):
    """
    To read the file
    :param file_name: Name of the input file
    :return: pandas dataframe with the data
    """
    # Reading the shopping data in to a pandas dataframe
    shopping_data = pd.read_csv(file_name, index_col='ID')

    # Cleaning header data
    headers = (shopping_data.columns.str.lower()).str.strip()
    shopping_data.columns = headers

    return shopping_data


def calculate_covariance_matrix(shopping_data):
    """
    To calculate the covariance matrix
    :param shopping_data: Shopping data
    :return: Covariance matrix
    """
    return shopping_data.cov()


def calculate_eigen_vector_values(covariance_matrix):
    """
    To return the eigen vectors and eigen values for the given covariance matrix
    :param covariance_matrix: Covariance matrix for the shopping data
    :return: eigen values and eigen vectors
    """

    return linalg.eig(covariance_matrix.get_values())


def calculate_absolute_eigen_values(eigen_values):
    """
    To get the absolute eigen values
    :param eigen_values: eigen values
    :return: absolute value for all the eigen values
    """
    abs_eigen_values = []
    for value in eigen_values:
        abs_eigen_values.append(math.fabs(value))
    return abs_eigen_values


def get_first_two_eigen_vectors(eigen_values, eigen_vectors, abs_eigen_values):
    """
    To get the first 2 eigen vectors
    :param eigen_values: Eigen values
    :param eigen_vectors: eigen vectors
    :param abs_eigen_values: absolute eigen values
    :return: None
    """
    # the eigen vectors are the columns in the list
    eigen_vectors = eigen_vectors.transpose()
    
    dict_abs_eigen_value = {}

    dict_eigen_vector = {}
    
    # associating eigen values to the vector and eigen values to its absolute values
    for i in range(0, len(abs_eigen_values)):
        dict_abs_eigen_value[abs_eigen_values[i]] = eigen_values[i]

        dict_eigen_vector[eigen_values[i]] = eigen_vectors[i]

    abs_eigen_values.sort(reverse=True)

    # finding the two highest eigen vectors
    highest_vector_1 = dict_eigen_vector[dict_abs_eigen_value[abs_eigen_values[0]]]
    highest_vector_2 = dict_eigen_vector[dict_abs_eigen_value[abs_eigen_values[1]]]

    return highest_vector_1, highest_vector_2


def plot_normalized_eigen_values(abs_eigen_values):
    """
    To plot normalized values of absolute eigen values
    :param abs_eigen_values: Absolute eigen values
    :return: None
    """
    sum_absolute_cumulative_value = sum(abs_eigen_values)

    # To store the cumulative normalized values
    cumulative_normalized_values = [0]

    number_eigen_vectors = [0]
    i = 1

    # To calculate cumulative sums
    key = 0

    # Normalizing each value
    for value in abs_eigen_values:
        key += value
        
        # Normalizing the value
        cumulative_normalized_values.append(key / sum_absolute_cumulative_value)
        number_eigen_vectors.append(i)
        i += 1

    # plotting the graph
    plt.xlabel("Number of Eigen Vectors ")
    plt.ylabel("Cumulative Sum of Normalized Eigen values")
    plt.title("Cumulative sum of Normalized Eigen values vs Number of Vectors")
    plt.plot(number_eigen_vectors, cumulative_normalized_values, '.-')
    plt.show()
    

def plot_agglomeration_data(highest_vector_1, highest_vector_2, shopping_data):
    """
    Projecting the data points on the two eigen vectors and plotting a scatter plot
    :param highest_vector_1: Vector with highest absolute eigen value
    :param highest_vector_2: Vector with 2nd highest absolute eigen value
    :param shopping_data: the data frame containing the data points.
    :return: returns the x and y coordinate of the 2D projected data.
    """
    # finding the dot product of eigen vector and data point.
    x = shopping_data.dot(highest_vector_1)
    y = shopping_data.dot(highest_vector_2)

    plt.title("2-D plot of the Projected Values")
    plt.xlabel("1st Highest Vector Projection")
    plt.ylabel("2nd Highest Vector Projection")
    plt.scatter(x, y)
    plt.show()

    return x, y


def plot_K_means(x, y):
    """
    Function performs K means clustering on the data
    :param x: nd-array X coordinates of the data
    :param y: nd-array Y coordinates of the data
    :return: returns the cluster centres formed
    """
    num_cluster = 3

    # forming a new data frame
    X = pd.DataFrame({
        'x':x,
        'y': y
    })

    # performing K-means clustering
    kmeans = KMeans(n_clusters=num_cluster, init='k-means++', n_init=10, max_iter=500, tol=0.0001,
                    precompute_distances='auto', verbose=0,).fit(X)

    # plotting the data and cluster centres
    plt.scatter(x, y, c='', edgecolors='black')
    plt.xlabel("1st Highest Vector Projection")
    plt.ylabel("2nd Highest Vector Projection")
    for i in range(num_cluster):
        plt.scatter(kmeans.cluster_centers_[i][0], kmeans.cluster_centers_[i][1], c='red')

    plt.title("K means Clustering")
    plt.show()

    return kmeans.cluster_centers_


def main(file_name):
    """
    Main calling function for the program
    :param file_name: File name of input file
    :return: None
    """

    # To read the data into a pandas dataframe
    shopping_data = read_input(file_name)

    # Calculating covariance matrix
    covariance_matrix = calculate_covariance_matrix(shopping_data)

    # Eigen vectors and eigen values for the covariance matrix
    eigen_values, eigen_vectors = calculate_eigen_vector_values(covariance_matrix)

    # Calculating absolute eigen values
    abs_eigen_values = calculate_absolute_eigen_values(eigen_values)

    # Get first 2 eigen vectors
    highest_vector_1, highest_vector_2 = get_first_two_eigen_vectors(eigen_values, eigen_vectors, abs_eigen_values)
    highest_vector_1_list = ['%.3f' % elem for elem in highest_vector_1.tolist()]
    highest_vector_2_list = ['%.3f' % elem for elem in highest_vector_2.tolist()]
    print("highest vector 1: "+str(highest_vector_1_list))
    print("highest vector 2: "+str(highest_vector_2_list))
    print("\n")

    # Plotting normalized eigen values
    plot_normalized_eigen_values(abs_eigen_values)

    # Plot agglomeration data
    x, y = plot_agglomeration_data(highest_vector_1, highest_vector_2, shopping_data)

    centres = plot_K_means(x, y)

    # To store the vectors
    vectors = []

    for i in range(len(centres)):
        print("cluster center "+str(i+1)+": ("+str(round(centres[i][0], 3))+" ,"+str(round(centres[i][1], 3))+")")
        x_hv1 = centres[i][0]*highest_vector_1
        y_hv2 = centres[i][1]*highest_vector_2
        vectors.append(x_hv1+y_hv2)

    milk = shopping_data["milk"].mean()
    petfood = shopping_data["petfood"].mean()
    veggies = shopping_data["veggies"].mean()
    cereal = shopping_data["cereal"].mean()
    bread = shopping_data["bread"].mean()
    rice = shopping_data["rice"].mean()
    meat = shopping_data["meat"].mean()
    eggs = shopping_data["eggs"].mean()
    yogurt = shopping_data["yogurt"].mean()
    chips = shopping_data["chips"].mean()
    cola = shopping_data["cola"].mean()
    fruit = shopping_data["fruit"].mean()

    item_list = [milk, petfood, veggies, cereal, bread, rice, meat, eggs, yogurt, chips, cola, fruit]

    print("\n")

    for i in range(len(vectors)):
        val = item_list[i] + vectors[i]
        val_list = ['%.3f' % elem for elem in val.tolist()]
        # print("Vector "+str(i+1)+": "+str(list(np.round(item_list[i]+vectors[i], 3))))
        print("Vector " + str(i + 1) + ": " + str(val_list))


if __name__ == '__main__':
    file_name = "HW_AG_SHOPPING_CART_v805.csv"
    main(file_name)
