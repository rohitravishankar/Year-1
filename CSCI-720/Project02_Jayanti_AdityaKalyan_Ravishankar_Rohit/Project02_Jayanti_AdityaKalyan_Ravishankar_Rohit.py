__author__ = "Aditya Kalyan Jayanti & Rohit Ravishankar"
__email__ = "aj8582@rit.edu & rr9105@rit.edu"

import pandas as pd


def get_month_data(input_file_frame, start_date, end_date):
    """
    To get a subset of data for analysis of the differences of accidents
    :param input_file_frame: Input file data frame
    :param start_date: Start date of the date range
    :param end_date: End date of the date range
    :return: Pandas data frame for subset of data
    """
    return input_file_frame.loc[(input_file_frame['DATE'] > start_date) & (input_file_frame['DATE'] <= end_date)]


def get_june_difference(input_file_frame):
    """
    To get the difference of accidents between june 2017 & june 2018
    :param input_file_frame: Pandas data frame
    :return:
    """
    june_2018 = get_month_data(input_file_frame, '2018-06-01', '2018-06-30')
    june_2017 = get_month_data(input_file_frame, '2017-06-01', '2017-06-30')

    # Persons killed/injured
    print("Average persons killed per day in June 2017", june_2017['NUMBER OF PERSONS KILLED'].sum()/30)
    print("Average persons killed per day in June 2018", june_2018['NUMBER OF PERSONS KILLED'].sum()/30)
    print("Persons injured in June 2017", june_2017['NUMBER OF PERSONS INJURED'].sum())
    print("Persons injured in June 2018", june_2018['NUMBER OF PERSONS INJURED'].sum())

    # # Pedestrians killed/injured
    # print("Average pedestrians killed per day in June 2017", june_2017['NUMBER OF PEDESTRIANS KILLED'].sum() / 30)
    # print("Average pedestrians killed per day in June 2018", june_2018['NUMBER OF PEDESTRIANS KILLED'].sum() / 30)
    # print("Average pedestrians injured per day in June 2017", june_2017['NUMBER OF PEDESTRIANS KILLED'].sum() / 30)
    # print("Average pedestrians injured per day in June 2018", june_2018['NUMBER OF PEDESTRIANS KILLED'].sum() / 30)
    #
    # # Cyclist killed/injured
    # print("Average cyclists killed per day in June 2017", june_2017['NUMBER OF CYCLIST KILLED'].sum() / 30)
    # print("Average cyclists killed per day in June 2018", june_2018['NUMBER OF CYCLIST KILLED'].sum() / 30)
    # print("Average cyclists injured per day in June 2017", june_2017['NUMBER OF CYCLIST KILLED'].sum() / 30)
    # print("Average cyclists injured per day in June 2018", june_2018['NUMBER OF CYCLIST KILLED'].sum() / 30)
    #
    # # Motorists killed/injured
    # print("Average motorists killed per day in June 2017", june_2017['NUMBER OF MOTORIST KILLED'].sum() / 30)
    # print("Average motorists killed per day in June 2018", june_2018['NUMBER OF MOTORIST KILLED'].sum() / 30)
    # print("Average motorists injured per day in June 2017", june_2017['NUMBER OF MOTORIST KILLED'].sum() / 30)
    # print("Average motorists injured per day in June 2018", june_2018['NUMBER OF MOTORIST KILLED'].sum() / 30)


def get_july_difference(input_file_frame):
    """
    To get the difference of accidents between june 2017 & june 2018
    :param input_file_frame: Pandas data frame
    :return:
    """
    july_2018 = get_month_data(input_file_frame, '2018-07-01', '2018-07-30')
    july_2017 = get_month_data(input_file_frame, '2017-07-01', '2017-07-30')

    # Persons killed/injured
    print("Average persons killed per day in July 2017", july_2017['NUMBER OF PERSONS KILLED'].sum()/30)
    print("Average persons killed per day in July 2018", july_2018['NUMBER OF PERSONS KILLED'].sum()/30)
    print("Persons injured in July 2017", july_2017['NUMBER OF PERSONS INJURED'].sum())
    print("Persons injured in July 2018", july_2018['NUMBER OF PERSONS INJURED'].sum())

    # # Pedestrians killed/injured
    # print("Average pedestrians killed per day in July 2017", july_2017['NUMBER OF PEDESTRIANS KILLED'].sum() / 30)
    # print("Average pedestrians killed per day in July 2018", july_2018['NUMBER OF PEDESTRIANS KILLED'].sum() / 30)
    # print("Average pedestrians injured per day in July 2017", july_2017['NUMBER OF PEDESTRIANS KILLED'].sum() / 30)
    # print("Average pedestrians injured per day in July 2018", july_2018['NUMBER OF PEDESTRIANS KILLED'].sum() / 30)
    #
    # # Cyclist killed/injured
    # print("Average cyclists killed per day in July 2017", july_2017['NUMBER OF CYCLIST KILLED'].sum() / 30)
    # print("Average cyclists killed per day in July 2018", july_2018['NUMBER OF CYCLIST KILLED'].sum() / 30)
    # print("Average cyclists injured per day in July 2017", july_2017['NUMBER OF CYCLIST KILLED'].sum() / 30)
    # print("Average cyclists injured per day in July 2018", july_2018['NUMBER OF CYCLIST KILLED'].sum() / 30)
    #
    # # Motorists killed/injured
    # print("Average motorists killed per day in July 2017", july_2017['NUMBER OF MOTORIST KILLED'].sum() / 30)
    # print("Average motorists killed per day in July 2018", july_2018['NUMBER OF MOTORIST KILLED'].sum() / 30)
    # print("Average motorists injured per day in July 2017", july_2017['NUMBER OF MOTORIST KILLED'].sum() / 30)
    # print("Average motorists injured per day in July 2018", july_2018['NUMBER OF MOTORIST KILLED'].sum() / 30)


def get_difference_of_data(filename):
    """
    To get the result of accidents across different years
    :param filename: Input file name
    :return:
    """
    data = pd.read_csv(filename, low_memory=False)
    data['DATE'] = pd.to_datetime(data['DATE'])
    get_june_difference(data)
    get_july_difference(data)



if __name__ == '__main__':
    get_difference_of_data("NYPD_Motor_Vehicle_Collisions.csv")