__author__ = "Rohit Ravishankar"
__email__ = "rr9105@rit.edu"


def question_4a():
    """
    Calculate for the 12 time stamps
    :return: None
    """
    # Prior probabilities
    Working = 1/2
    Surfing = 1/2
    Meeting = 0

    # Transition probabilities
    Working_Working = 1/2
    Surfing_Surfing = 1/4
    Meeting_Meeting = 0

    Working_Surfing = 1/4
    Surfing_Working = 1/2

    Meeting_Surfing = 2/3
    Surfing_Meeting = 1/4

    Meeting_Working = 1/3
    Working_Meeting = 1/4

    time_stamps = list()

    time_stamps.append([Working, Surfing, Meeting])

    for i in range(1, 12):
        working_calculation = time_stamps[i-1][0] * Working_Working + \
                              time_stamps[i-1][1] * Surfing_Working + \
                              time_stamps[i-1][2] * Meeting_Working

        surfing_calculation = time_stamps[i-1][0] * Working_Surfing + \
                              time_stamps[i-1][1] * Surfing_Surfing + \
                              time_stamps[i-1][2] * Meeting_Surfing

        meeting_calculation = time_stamps[i-1][0] * Working_Meeting + \
                              time_stamps[i-1][1] * Surfing_Meeting + \
                              time_stamps[i-1][2] * Meeting_Meeting

        time_stamps.append([working_calculation, surfing_calculation, meeting_calculation])

    for i in time_stamps:
        print(i)

    return time_stamps


if __name__ == '__main__':
    question_4a()

