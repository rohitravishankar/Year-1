__author__ = "Rohit Ravishankar"
__email__ = "rr9105@rit.edu"

import csv
import math


def build_decision_tree(features, data, list_of_features, tab_space, predict_file):
    """
    To recursively build a decision tree
    :param features: The list of features
    :param data: The dataset without the columnn headers
    :param list_of_features: The list of features, i.e., column headers
    :param tab_space: The level of indentation at the current level
    :param predict_file: The file to write the prediction to\ 
    :return: Majority class
    """

    # TO store class labels
    count_label_1 = 0
    count_label_2 = 0
    for line in data:
        if line[-1] == "EN":
            count_label_1 += 1
        else:
            count_label_2 += 1
    if count_label_1 > count_label_2:
        majority_class = "ENGLISH"
    else:
        majority_class = "DUTCH"

    # To define the level of indentation
    total_tab_spaces = '\t' * tab_space

    # Stopping condition
    if tab_space == 8 or len(data) <= 40:
        predict_file.write(total_tab_spaces)
        if majority_class == "ENGLISH":
            result = "ENGLISH"
        else:
            result = "DUTCH"
        predict_file.write('return \'' + result + '\'\n')
        return majority_class
    else:
        threshold = 1.0
        for value in range(len(features) - 1):
            # impurity_rate = get_impurity_value(value, data, count_label_1, count_label_2)
            impurity_rate = get_impurity_value(value, data)
            if impurity_rate <= threshold:
                best_attribute = value
                threshold = impurity_rate
        left = []
        right = []
        for each in data:
            if each[best_attribute] != 'N':
                left.append(each)
            else:
                right.append(each)
        predict_file.write(total_tab_spaces + "if " + list_of_features[features[best_attribute]] + ":\n")
        build_decision_tree(features, left, list_of_features, tab_space + 1, predict_file)
        predict_file.write(total_tab_spaces)
        predict_file.write("else:\n")
        build_decision_tree(features, right, list_of_features, tab_space + 1, predict_file)


def read_csv_data_file(training_data_file):
    """
    TO read the csv data
    :param training_data_file: Training data csv file 
    :return: Return attributes and data
    """
    flag = False
    data = []
    attributes = ""
    with open(training_data_file) as file:
        for line in csv.reader(file, delimiter=","):
            if not flag:
                attributes = line
                flag = True
            else:
                data.append(line)
        return attributes, data


def generate_decision_rules(training_data_file):
    """
    To generate the list of decision rules
    :param training_data_file: The input training data CSV  
    :return: None
    """
    
    print("Reading Training Data and generating decision tree program")

    with open("predict.py", "w", encoding="UTF-8") as predict_file:
        features, data = read_csv_data_file(training_data_file)
        list_of_features = {
            features[0]: '"de" in word or "het" in word or "dat" in word or "en" in word or "een" in word or "voor" in word or "van" in word or "welke" in word or "te" in word or "hij" in word or "zij" in word or "op" in word or "ik" in word or "bij" in word',
            features[1]: '"ij" in word',
            features[2]: '"the" in word or "but" in word or "for" in word or "which" in word or "that" in word or "and" in word or "not" in word or "to" in word or "in" in word',
            features[3]: '"q" in word',
            features[4]: '"x" in word',
            features[5]: '"aa" in input_sentence or "ee" in input_sentence or "ii" in input_sentence or "uu" in input_sentence',
            features[6]: '"ijk" in input_sentence or "sch" in input_sentence or "ijn" in input_sentence',
            features[7]: '"is" in word or "of" in word or "was" in word or "all" in word',
            features[8]: '"come" in word or "a" in word',
            features[9]: '"and" == word',
            features[10]: '"he" == word or "she" == word or "it" == word or "they" == word'
        }
        predict_file.write("""
def classification(input_sentence, word):
""")
        build_decision_tree(features, data, list_of_features, 1, predict_file)
        predict_file.write("""
if __name__ == "__main__":
    input_sentence = input("Enter the sentence you want to predict")
    results = classification(input_sentence.split())
    print(results)
""")


def get_impurity_value(value, data):
    """
    Get impurity value
    :param value: The attribute in question
    :param data: The data set
    :return: Impurity value
    """

    # TP, TN, FP, FN values
    part_1_en = 0
    part_1_nl = 0
    part_2_en = 0
    part_2_nl = 0
    for line in data:
        if line[value] == 'Y':
            if line[len(line) - 1] == "EN":
                part_1_en += 1
            else:
                part_1_nl += 1
        elif line[value] == 'N':
            if line[len(line) - 1] == "EN":
                part_2_en += 1
            else:
                part_2_nl += 1

    # Total points on either side of the threshold
    total_part_1 = part_1_en + part_1_nl
    total_part_2 = part_2_en + part_2_nl

    if total_part_1 == 0:
        gini_index_1 = 1.0
    else:
        gini_index_1 = 1 - ((part_1_en / total_part_1) ** 2 + (part_1_nl / total_part_1) ** 2)
    if total_part_2 == 0:
        gini_index_2 = 1.0
    else:
        gini_index_2 = 1 - ((part_2_en / total_part_2) ** 2 + (part_2_nl / total_part_2) ** 2)
    gini = (total_part_1 / (total_part_1 + total_part_2) * gini_index_1) + (
                total_part_2 / (total_part_1 + total_part_2) * gini_index_2)
    return gini


def get_accuracy(english_file, dutch_file):
    """
    To check the accuracy of the test document
    :param english_file: English file
    :param dutch_file: Dutch File
    :return: Accuracy of the model for the languages
    """
    files = []
    accuracy_result = []

    # To calculate the accuracy of our model
    from predict import classification

    # To create a list of files for english and dutch
    files.append(english_file)
    files.append(dutch_file)

    for file in range(len(files)):
        count_1_label = 0
        count_2_label = 0
        with open(files[file], encoding="UTF-8") as f:
            sentences = f.readlines()
            for line in sentences:

                # To clean the data before sending the input
                eachline = line.strip()
                line = line.strip().split()

                # To send the line and the list of words for the decision trees
                result = classification(eachline, line)

                # To count the number of decisions for english and dutch
                if result == "ENGLISH":
                    count_1_label += 1
                else:
                    count_2_label += 1

            # Count classifications for each file
            count = list()
            count.append(count_1_label)
            count.append(count_2_label)
            total = count_1_label + count_2_label
            accuracy_result.append(round(count[file] / total * 100, 3))
    for accuracy, lang in zip(accuracy_result, ["English", "Dutch"]):
        print("Accuracy for " + lang + " : " + str(accuracy))


def one_r_rule(lc, record_data):
    """
    1-R rule to create decision stumps
    :param lc: The value to pick for 1-R rule
    :param record_data: Each data record
    :return: 1-R decision values
    """
    if lc == 0:
        if record_data[0] == "TRUE":
            return "NL"
        else:
            return "EN"
    elif lc == 1:
        if record_data[1] == "TRUE":
            return "NL"
        else:
            return "EN"
    elif lc == 2:
        if record_data[2] == "TRUE":
            return "EN"
        else:
            return "NL"
    elif lc == 3:
        if record_data[3] == "TRUE":
            return "EN"
        else:
            return "NL"
    elif lc == 4:
        if record_data[4] == "TRUE":
            return "EN"
        else:
            return "NL"
    elif lc == 5:
        if record_data[5] == "TRUE":
            return "NL"
        else:
            return "EN"
    elif lc == 6:
        if record_data[6] == "TRUE":
            return "NL"
        else:
            return "EN"
    elif lc == 7:
        if record_data[7] == "TRUE":
            return "EN"
        else:
            return "NL"
    elif lc == 8:
        if record_data[8] == "TRUE":
            return "EN"
        else:
            return "NL"
    elif lc == 9:
        if record_data[9] == "TRUE":
            return "EN"
        else:
            return "NL"
    elif lc == 10:
        if record_data[10] == "TRUE":
            return "EN"
        else:
            return "NL"


def adaBoost(data):
    """
    To perform adaboost
    :param data: The dataset
    :return: Weighted majority
    """
    record_data = []
    weighted_majority = []

    # To get the instances of the data with the results into a list
    for instance in data:
        if instance[len(instance) - 1] == "EN" or instance[len(instance) - 1] == "NL":
            record_data.append(instance)

    # vector of N example weights
    weight = [1/len(record_data)] * len(record_data)

    # Number of features
    for lc in range(10):
        error = 0
        # If the value is misclassified
        for j in range(len(record_data)):
            if one_r_rule(lc, record_data[j]) != record_data[j][len(record_data[j]) - 1]:
                error = error + weight[j]

        # If the value is correct
        for j in range(len(record_data)):
            if one_r_rule(lc, record_data[j]) == record_data[j][len(record_data[j]) - 1]:
                weight[j] = weight[j] * (error/(1 - error))

        # To normalize the weights
        for j in range(len(record_data)):
            weight[j] /= sum(weight)
        hypothesis_weight = math.log(abs(1 - error) / error, 2)
        weighted_majority.append(hypothesis_weight)
    return weighted_majority


def write_adaboost(weighted_majority, adaboost_file):
    """
    To write the adaboost prediction to file
    :param weighted_majority: The weighted majority from the adaboost algorithm
    :param adaboost_file: the file pointer to write to
    :return: None
    """
    adaboost_file.write("""
def decision_stumps(input_sentence, word):
    weighted_majority = """ + str(weighted_majority) +
    """
    result = adaboost_decision(weighted_majority, input_sentence, word)
    if result < 0:
        return "DUTCH"
    else:
        return "ENGLISH"
    
    
def adaboost_decision(weighted_majority, input_sentence, word):
    sum_value = 0
    result_weighted_majority = []
    if "de" in word or "het" in word or "dat" in word or "en" in word or "een" in word or "voor" in word or "van" in word or "welke" in word or "te" in word or "hij" in word or "zij" in word or "op" in word or "ik" in word or "bij" in word:
        result_weighted_majority.append(1)
    else:
        result_weighted_majority.append(-1)
    if "ij" in word:
        result_weighted_majority.append(1)
    else:
        result_weighted_majority.append(-1)
    if "the" in word or "but" in word or "for" in word or "which" in word or "that" in word or "and" in word or "not" in word or "to" in word or "in" in word:
        result_weighted_majority.append(-1)
    else:
        result_weighted_majority.append(1)
    if "q" in word:
        result_weighted_majority.append(-1)
    else:
        result_weighted_majority.append(1)        
    if "x" in word:
        result_weighted_majority.append(-1)
    else:
        result_weighted_majority.append(1) 
    if "aa" in input_sentence or "ee" in input_sentence or "ii" in input_sentence or "uu" in input_sentence:
        result_weighted_majority.append(1)
    else:
        result_weighted_majority.append(-1)
    if "ijk" in input_sentence or "sch" in input_sentence or "ijn" in input_sentence:
        result_weighted_majority.append(1)
    else:
        result_weighted_majority.append(-1)
    if "is" in word or "of" in word or "was" in word or "all" in word:
        result_weighted_majority.append(-1)
    else:
        result_weighted_majority.append(1)
    if "come" in word or "a" in word:
        result_weighted_majority.append(-1)
    else:
        result_weighted_majority.append(1) 
    if "and" == word:
        result_weighted_majority.append(-1)
    else:
        result_weighted_majority.append(1) 
    if "he" == word or "she" == word or "it" == word or "they" == word:
        result_weighted_majority.append(-1)
    else:
        result_weighted_majority.append(1)
    
    for i in result_weighted_majority:
        sum_value += weighted_majority[i] * result_weighted_majority[i]
    return sum_value
    
if __name__ == '__main__':
    input_sentence = input("Enter the sentence you want to predict: ")
    word = input_sentence.split()
    results = decision_stumps(input_sentence, word)
    print(results)                    
""")


def get_adaboost_accuracy(english_file, dutch_file):
    """
    To get the accuracy for adaboost
    :param english_file: English file
    :param dutch_file: Dutch file
    :return: Accuracy
    """
    files = list()
    files.append(english_file)
    files.append(dutch_file)
    accuracy_result = []
    from AdaboostPredict import decision_stumps

    for file in range(len(files)):
        count_1_label = 0
        count_2_label = 0
        with open(files[file], encoding="UTF-8") as f:
            sentences = f.readlines()
            for line in sentences:

                # To clean the data before sending the input
                eachline = line.strip()
                line = line.strip().split()

                # To send the line and the list of words for the decision trees
                result = decision_stumps(eachline, line)

                # To count the number of decisions for english and dutch
                if result == "ENGLISH":
                    count_1_label += 1
                else:
                    count_2_label += 1

            # Count classifications for each file
            count = list()
            count.append(count_1_label)
            count.append(count_2_label)
            total = count_1_label + count_2_label
            accuracy_result.append(round(count[file] / total * 100, 3))
    for accuracy, lang in zip(accuracy_result, ["English", "Dutch"]):
        print("Accuracy for " + lang + " : " + str(accuracy))


def start_adaboost(filename):
    """
    The calling function for adaboost algorithm
    :param filename: Input data file
    :return: None
    """
    print("\nAdaboost Running")
    features, data = read_csv_data_file(filename)
    weighted_majority = adaBoost(data)
    adaboost_file = open("AdaboostPredict.py", "w", encoding="UTF-8")
    write_adaboost(weighted_majority, adaboost_file)
    adaboost_file.close()
    # get_adaboost_accuracy("english.txt", "dutch.txt")


def main_trainer():
    """
    Main calling function
    :return: None
    """
    generate_decision_rules("Training_Data_CSV.csv")
    # get_accuracy("english.txt", "dutch.txt")
    start_adaboost("Training_Data_CSV.csv")


if __name__ == "__main__":
    generate_decision_rules("Training_Data_CSV.csv")
    # get_accuracy("english.txt", "dutch.txt")
    start_adaboost("Training_Data_CSV.csv")
