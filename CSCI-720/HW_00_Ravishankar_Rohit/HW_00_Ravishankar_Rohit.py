import matplotlib.pyplot as plt

# TOP SPEED, LOW SPEED and the DISTANCE to travel
HIGH_SPEED = 80
LOW_SPEED = 1
DISTANCE = 22

# GEARS
FRONT_GEAR = [73, 61, 47]
BACK_GEAR = [23, 29, 37, 43, 47, 63, 71]

def task_1():
    """
    Plot the time that it takes to get to work as a function of speed.
    :return: None
    """

    # To store the list of speeds to plot
    list_of_speeds = []
    list_of_times = []

    # To go from 1 through 80
    for i in range(LOW_SPEED, HIGH_SPEED + 1):
        list_of_speeds.append(i)
        time = (DISTANCE/i) * 60 * 60
        list_of_times.append(time)

    plt.plot(list_of_speeds, list_of_times)
    plt.xlabel("Speed (in mph)")
    plt.ylabel("Time (in s)")
    plt.show()


def task_2():
    """
    Plot the time that is saved as a function of speed in 5mph increments.
    :return: None
    """

    # To store the list of speeds to plot
    list_of_speeds = []
    list_of_times = []
    list_of_time_difference = [0]

    # To go from 1 through 80
    for i in range(LOW_SPEED, HIGH_SPEED + 1, 5):
        list_of_speeds.append(i)
        list_of_times.append(((DISTANCE / i) * 60))

    for i in range(1, len(list_of_times)):
        list_of_time_difference.append(list_of_times[i-1] - list_of_times[i])

    plt.plot(list_of_speeds, list_of_time_difference)
    plt.xlabel("Speed (in mph)")
    plt.ylabel("Time saved (in minutes)")
    plt.show()


def calculate_gear_ratio(front_gear, back_gear):
    """
    To calculate the gear ratio
    :param front_gear: The number of teeth on the front gear
    :param back_gear: The number of teeth on the rear gear
    :return: gear ratio
    """
    return front_gear/back_gear


def task_3():
    """
    Plot gear ratios for all possible gear combinations
    :return: None
    """

    # To store list of values to plot
    list_of_values_per_gear = []
    list_of_values = []

    for i in FRONT_GEAR:
        for j in BACK_GEAR:
            list_of_values_per_gear.append(calculate_gear_ratio(i, j))
        list_of_values.append(list_of_values_per_gear)
        list_of_values_per_gear = []

    for i in range(len(FRONT_GEAR)):
        for j in range(len(list_of_values[i])):
            plt.scatter(FRONT_GEAR[i], list_of_values[i][j])
            plt.annotate("(" + str(FRONT_GEAR[i]) + "," + str(BACK_GEAR[j]) + ")", (FRONT_GEAR[i], list_of_values[i][j]))
    plt.ylabel("Gear Ratio")
    plt.xlabel("Front Gears (number of teeth) ")
    plt.show()


if __name__== "__main__":
    task_1()
    task_2()
    task_3()