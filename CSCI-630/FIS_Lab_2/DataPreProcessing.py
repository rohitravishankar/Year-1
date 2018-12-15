__author__ = "Rohit Ravishankar"
__email__ = "rr9105@rit.edu"

import re
import csv

LANGUAGE = ["EN", "NL"]

FILE_NAMES = ["english.txt", "dutch.txt"]

NUMBER_OF_WORDS_PER_SENTENCE = 20

COMMON_DUTCH_WORDS = ['de', 'het', 'en', 'een', 'voor', 'van', 'welke', 'te', 'hij', 'zij', 'op', 'ik', 'bij']

COMMON_ENGLISH_WORDS = ['a', 'an', 'the', 'which', 'what', 'when']


def merge_training_data():
    """
    To merge the training data to create an aggregated file
    :return: None
    """
    line_data = []
    with open("Training_Data.txt", "w") as file:
        for training_data_language in ["Training_EN.txt", "Training_NL.txt"]:
            with open(training_data_language, "r") as language_file:
                read_text = language_file.readlines()
                for line in read_text:
                    file.write(line)

    # Ensuring no trailing spaces etc
    with open("Training_Data.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip().split(", ")
            line_data.append(line)

    with open('Training_Data_CSV.csv', 'w') as Training_Data_CSV:
        writer = csv.writer(Training_Data_CSV)
        writer.writerows([['COLUMN1', 'COLUMN2', 'COLUMN3', 'COLUMN4', 'COLUMN5', 'COLUMN6', 'COLUMN7', 'COLUMN8',
                           'COLUMN9', 'COLUMN10', 'Label']])
        writer.writerows(line_data)

    print("Training Data merged and CSV created")


def write_training_data(training_data, language):
    """
    TO write the training data to a file
    :param training_data: Training data with Y AND N values
    :param language: To annotate the data
    :return: None
    """

    feature = ""
    count = 0
    with open("Training_"+language+".txt", "w") as file:
        for line in training_data:

            # Trying to limit the samples per language
            if count <= 4000:
                for value in line:
                    for language_type in value:
                        if str(language_type) == "EN" or str(language_type) == "NL":
                            language_type += "\n"
                        feature += str(language_type) + ", "
                feature = feature.strip(", ")
                file.write(feature)
                feature = ""
                count += 1


def create_training_data_file(list_of_word_lines, language):
    """
    To create the training data file
    :param list_of_word_lines: list of list with each of size of 15 word length
    :param language: Language of the input
    :return: feature vector
    """
    # To store each feature vector
    feature_vector = []

    # To store the entire dataset
    data = []

    for sentence in list_of_word_lines:

        # Contains Q
        CONTAINS_Q = 'N'

        # Contains Q
        CONTAINS_X = 'N'

        # Contains more than 1 vowel
        VOWELS = 'N'

        # Contains common dutch substrings
        DUTCH_SUBSTRING = 'N'

        # Contains is-was
        ISWAS = 'N'

        # Contains come
        COME = 'N'

        # Contains common english words
        COMMON_ENGLISH_WORDS = 'N'

        # Contains common dutch words
        DUTCH_WORDS = 'N'

        # Contains dutch ij
        IJ = 'N'

        # Contains and
        AND = 'N'

        # Contains they, he, she
        COLLECTIVES = 'N'

        for word in sentence:

            if re.match('[0-9]*', word):
                word = re.sub('[0-9]*', '', word)

            if re.match('[!?~`@#$%&)(_=+/.,"»;«-]', word):
                word = re.sub('[!?~`@#$%&)(_=+/.,"»;«-]', '', word)

            word = word.lower()
            if "de" == word or "het" == word or "dat" == word or "en" == word or "een" == word or "voor" == word or "van" == word or "welke" == word \
                    or "te" == word or "hij" == word or "zij" == word or "op" == word or "ik" == word or "bij" == word:
                DUTCH_WORDS = 'Y'

            if "ij" in word:
                IJ = 'Y'

            if "the" == word or "but" == word or "for" == word or "which" == word or "that" == word or "and" == word or "not" == word \
                    or "to" == word or "in" == word:
                COMMON_ENGLISH_WORDS = 'Y'

            if "q" in word:
                CONTAINS_Q = 'Y'

            if "x" in word:
                CONTAINS_X = 'Y'

            if "aa" in word or "ee" in word or "ii" in word or "uu" in word:
                VOWELS = 'Y'

            if "ijk" in word or "sch" in word or "ijn" in word:
                DUTCH_SUBSTRING = 'Y'

            if "is" == word or "of" == word or "was" == word or "all" in word:
                ISWAS = 'Y'

            if "come" == word or "a" == word:
                COME = 'Y'

            if "and" == word:
                AND = 'Y'

            if "he" == word or "she" == word or "it" == word or "they" == word:
                COLLECTIVES = 'Y'

        feature_vector.append([DUTCH_WORDS, IJ, COMMON_ENGLISH_WORDS, CONTAINS_Q, CONTAINS_X,
                             VOWELS, DUTCH_SUBSTRING, ISWAS,
                             COME, AND, COLLECTIVES, language])

        data.append(feature_vector)
        feature_vector = []
    return data


def limiting_sentence_length(input_text):
    """
    To split the string into n- word sentences
    :param input_text: Input list of words
    :return: Training data as a list of n- word inputs
    """

    # To all the sentences into a list of words
    training_words = []

    # To store the training data as a list of 15 words
    training_data_as_list = []

    # Helper data structure
    sample = []

    for line in input_text:
        line = line.split(" ")
        for word in line:
            if word != "":
                training_words.append(word)

    # To store the training data into a list of list with only 15 words in each list
    for word in training_words:
        if len(sample) < NUMBER_OF_WORDS_PER_SENTENCE-1:
            sample.append(word)
        else:
            sample.append(word)
            training_data_as_list.append(sample)
            sample = []
    return training_data_as_list


def read_file(filename):
    """
    To read the input file
    :param filename: Name of file
    :return: List containing the text data as a file
    """

    print("Reading TextFile " + filename)
    text = []
    with open(filename, encoding="utf8") as file:
        lines = file.readlines()
    for line in lines:
        line = line.strip()
        text.append(line)
    return text


def build_training_data():
    """
    Main calling function for the program
    :return: None
    """
    for i in range(len(FILE_NAMES)):
        input_text = read_file(FILE_NAMES[i])
        list_of_word_lines = limiting_sentence_length(input_text)
        data = create_training_data_file(list_of_word_lines,  LANGUAGE[i])
        write_training_data(data, LANGUAGE[i])
    merge_training_data()


if __name__ == '__main__':
    build_training_data()