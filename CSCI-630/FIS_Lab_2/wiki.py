__author__= "Rohit Ravishankar"
__email__= "rr9105@rit.edu"

import sys
from DataPreProcessing import *
from train import *


def main():
    """
    Main calling function of the program
    :return: None
    """
    if sys.argv[1] == 'train':
        build_training_data()
        main_trainer()

    if sys.argv[1] == 'predict' and len(sys.argv) > 2:
        from predict import classification
        from AdaboostPredict import decision_stumps
        input_file = open(sys.argv[2])
        data = input_file.readlines()
        print("Decision Tree prediction")
        for i in data:
            print(classification(i, i.strip().split()))

        print("\nAdaboost prediction")

        for i in data:
            print(decision_stumps(i, i.strip().split()))

    elif sys.argv[1] == 'predict':
        print('Wrong usage for prediction. Please supply a file after predict')


if __name__ == '__main__':
    main()