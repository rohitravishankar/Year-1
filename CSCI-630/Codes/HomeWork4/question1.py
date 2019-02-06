__author__ = "Rohit Ravishankar"
__email__ = "rr9105@rit.edu"

import pandas as pd


def check_linearly_separable(data):
    """
    To check if the dataset is linearly separable
    :param data: The input data set
    :return: None
    """
    data.plot.scatter(x=data[data.columns[0]], y=data[data.columns[2]])


def read_data(file_name):
    """
    To read the data from the csv file into a pandas dataframe
    :param file_name: input file name
    :return: pandas dataframe of the input file
    """
    return pd.read_csv(file_name)


if __name__ == '__main__':
    data = read_data('data.csv')
    check_linearly_separable(data)
