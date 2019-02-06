__author__ = "Rohit Ravishankar"
__email__ = "rr9105@rit.edu"


def question_4b():
    """
    Calculate for 12 time stamps
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

    # Feeling probabilities
    Working_Unhappy = 1/4
    Working_Meh = 1/2
    Working_Happy = 1/4
    Working_Mood = [Working_Unhappy, Working_Meh, Working_Happy]

    Surfing_Unhappy = 1/2
    Surfing_Meh = 0
    Surfing_Happy = 1/2
    Surfing_Mood = [Surfing_Unhappy, Surfing_Meh, Surfing_Happy]

    Meeting_Unhappy = 1/3
    Meeting_Meh = 2/3
    Meeting_Happy = 0
    Meeting_Mood = [Meeting_Unhappy, Meeting_Meh, Meeting_Happy]

    time_stamps = list()
    time_stamps.append([Working * Working_Mood[0], Surfing * Surfing_Mood[0], Meeting * Meeting_Mood[0]])
    print([Working * Working_Mood[0], Surfing * Surfing_Mood[0], Meeting * Meeting_Mood[0]])
    for i in range(1, 12):

        index = i % 3

        working_calculation = time_stamps[i-1][0] * Working_Working + \
                              time_stamps[i-1][1] * Surfing_Working + \
                              time_stamps[i-1][2] * Meeting_Working
        working_calculation = working_calculation * Working_Mood[index]

        surfing_calculation = time_stamps[i-1][0] * Working_Surfing + \
                              time_stamps[i-1][1] * Surfing_Surfing + \
                              time_stamps[i-1][2] * Meeting_Surfing
        surfing_calculation = surfing_calculation * Surfing_Mood[index]

        meeting_calculation = (time_stamps[i-1][0] * Working_Meeting) + \
                              (time_stamps[i-1][1] * Surfing_Meeting) + \
                              (time_stamps[i-1][2] * Meeting_Meeting)
        meeting_calculation = meeting_calculation * Meeting_Mood[index]

        normalizing_value = working_calculation + surfing_calculation + meeting_calculation
        print([working_calculation/normalizing_value, surfing_calculation/normalizing_value, meeting_calculation/normalizing_value])
        time_stamps.append([working_calculation, surfing_calculation, meeting_calculation])

    return time_stamps


if __name__ == '__main__':
    question_4b()

