__author__ = "Rohit Ravishankar"
__email__ = "rr9105@rit.edu"

import csv
import math
import os

# stores the path to the program, i.e., the current file
PROGRAM_PATH = os.path.dirname(os.path.abspath(__file__))

# Stores the path to the static folder
INPUT_FILES_FOLDER = os.path.join(PROGRAM_PATH, "InputFiles")

# Stores the path to the output folder where you find all the output maps
OUTPUT_KML_FILES_FOLDER = os.path.join(PROGRAM_PATH, "OutputKMLFiles")

# List of file names
GPS_FILES = ['ZI8G_ERF_2018_08_16_1428.txt', 'ZI8H_HJC_2018_08_17_1745.txt', 'ZI8J_GKX_2018_08_19_1646.txt',
             'ZI8K_EV7_2018_08_20_1500.txt', 'ZI8N_DG8_2018_08_23_1316.txt', 'ZIAA_CTU_2018_10_10_1255.txt',
             'ZIAB_CIU_2018_10_11_1218.txt', 'ZIAC_CO0_2018_10_12_1250.txt']

# Number of lines to skip on the input file
SKIP_LINES = 5

# Types of data
TYPES_OF_DATA = ['$GPRMC', '$GPGGA']

# STOP SIGN THRESHOLDS
STOP_SIGN_SPEED_THRESHOLD = 7           # Stop sign speed threshold
STOP_SIGN_TIME_THRESHOLD = 1            # Stop sign time threshold
STOP_SIGN_LAST_SIGN_THRESHOLD = 0.01    # Stop sign last stop sign threshold


# LEFT TURN THRESHOLD
MIN_ANGLE = 50                          # Left turn minimum angle
MAX_ANGLE = 170                         # Left turn maximum angle
LEFT_TURN_SPEED_THRESHOLD = 1           # Left turn speed
LEFT_TURN_LAST_SIGN_THRESHOLD = 0.0001  # Left turn last stop sign threshold


def emit_header(file_name):
    """
    To emit the header for the output file
    :param file_name: Name of the input file
    :return: Output file pointer to the KML file
    """

    # The output file is the same name as the input file appended with OUTPUT at the end
    output_file_name = file_name[:-4] + "_OUTPUT.kml"

    # Opens the output file in write mode
    output_file = open(output_file_name, "w")
    output_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    output_file.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
    output_file.write('<Document>\n')
    output_file.write('\t<Style id="yellowPoly">\n')
    output_file.write('\t\t<LineStyle>\n')
    output_file.write('\t\t\t<color>Af00ffff</color>\n')
    output_file.write('\t\t\t<width>6</width>\n')
    output_file.write('\t\t</LineStyle>\n')
    output_file.write('\t\t<PolyStyle>\n')
    output_file.write('\t\t\t<color>7f00ff00</color>\n')
    output_file.write('\t\t</PolyStyle>\n')
    output_file.write('\t</Style>\n')
    output_file.write('\t<Placemark>\n')
    output_file.write('\t\t<styleUrl>#yellowPoly</styleUrl>\n')
    output_file.write('\t\t<LineString>\n')
    output_file.write('\t\t<Description>Speed in MPH, not altitude.</Description>\n')
    output_file.write('\t\t\t<extrude>1</extrude>\n')
    output_file.write('\t\t\t<tesselate>1</tesselate>\n')
    output_file.write('\t\t\t<altitudeMode>absolute</altitudeMode>\n')
    output_file.write('\t\t\t<coordinates>\n')

    return output_file


def convert_to_degrees_mins(value, lat_or_long, cardinal_direction):
    """
    To convert the lat/long value to degrees instead of degrees and minutes seperately
    :param value: Value to be converted to degree value
    :param lat_or_long: Type of input, i.e., latitude or longitude
    :param cardinal_direction: Direction, i.e., N, S, E, W
    :return: Latitude or longitude value in degrees
    """
    # Lat/long values determine the cardinal direction and hence the +ve/-ve value for coordinate
    if lat_or_long == 'latitude':
        degrees = float(value[:2])
        minutes = float(value[2:]) * 0.0166667

        if cardinal_direction == 'N':
            return degrees + minutes
        else:
            return - (degrees + minutes)

    else:
        degrees = float(value[:3])
        minutes = float(value[3:]) * 0.0166667

        if cardinal_direction == 'E':
            return degrees + minutes
        else:
            return - (degrees + minutes)


def remove_duplicates(add_data):
    """
    To remove duplicates from a list of coordinates
    :param add_data: The list of all coordinates with duplicates
    :return: List without duplicates
    """
    final_list = []
    for each_tuple in add_data:

        # If the current tuple exists in the final list, i.e., duplicate tuple, don't add to the list
        if each_tuple not in final_list:
            final_list.append(each_tuple)
    return final_list


def convert_to_kml(file_name, output_file):
    """
    Read the text file and convert the coordinates to represent coordinates in the KML file
    :param file_name: Input file path
    :param output_file: Path of the output file
    :return: None
    """

    with open(file_name, "r") as input_file:

        # Skip the first 5 lines
        for _ in range(SKIP_LINES):
            next(input_file)

        # CSV is read using csv.reader
        csv_reader = csv.reader(input_file, delimiter=",")

        # Set to store all the coordinates
        all_coordinates = list()

        # Iterating over each of the coordinates in the CSV
        for line in csv_reader:

            # If the line is of RMC type separate the data out
            if line[0] == TYPES_OF_DATA[0]:

                # I was getting a line with an empty string so a check for that!
                if line[3] != '' or line[4] != '' or line[5] != '' or line[6] != '':
                    latitude = convert_to_degrees_mins(line[3], "latitude", line[4])
                    longitude = convert_to_degrees_mins(line[5], "longitude", line[6])

            # You don't want duplicate data values and hence we don't pick GGA records
            else:
                continue
            all_coordinates.append((longitude, latitude, 1000))

        # To use only the unique values, i.e., deduplication
        all_coordinates = remove_duplicates(all_coordinates)

        for coordinate in all_coordinates:
            output_file.write("\n\t\t\t\t" + str(coordinate[0]) + "," + str(coordinate[1]) + "," + str(coordinate[-1]))

        # Closing tags for the KML
        output_file.write("\n\t\t\t</coordinates>")
        output_file.write("\n\t\t</LineString>")
        output_file.write("\n\t</Placemark>")


def plot_stop_signs(stop_signs, output_file):
    """
    To plot stop signs with red marks
    :param stop_signs:  List of stop signs
    :param output_file: Output file pointer
    :return: None
    """
    for stop_sign in stop_signs:
        output_file.write("\n<Placemark>")
        output_file.write("\n\t<description>RED Pin for stop</description>")
        output_file.write('\n\t<Style id="normalPlacemark">')
        output_file.write('\n\t\t<IconStyle>')
        output_file.write('\n\t\t\t<color>ff0000ff</color>')
        output_file.write('\n\t\t\t<Icon>')
        output_file.write('\n\t\t\t\t<href>http://maps.google.com/mapfiles/kml/paddle/1.png</href>')
        output_file.write('\n\t\t\t</Icon>')
        output_file.write('\n\t\t</IconStyle>')
        output_file.write('\n\t</Style>')
        output_file.write('\n\t<Point>')
        output_file.write("\n\t\t<coordinates>" + str(stop_sign[0]) + "," + str(stop_sign[1]) + "," + str(300) +
                          "</coordinates>")
        output_file.write("\n\t</Point>")
        output_file.write("\n</Placemark>")


def plot_left_turns(left_turns, output_file):
    """
    To plot the left turns
    :param left_turns: List of left turns
    :param output_file: output file
    :return: None
    """
    for left_turn in left_turns:
        output_file.write('\n<Placemark>')
        output_file.write('\n\t<description>Default Pin is Yellow</description>')
        output_file.write('\n\t<Point>')
        output_file.write('\n\t\t<coordinates>')
        output_file.write("\n\t\t\t" + str(left_turn[0]) + "," + str(left_turn[1]) + "," + "1000")
        output_file.write('\n\t\t</coordinates>\n')
        output_file.write('\n\t</Point>')
        output_file.write('\n</Placemark>')


def emit_trailer(output_file):
    """
    To emit the trailer for a given file
    :param output_file: The output file pointer
    :return: None
    """
    output_file.write("\n</Document>")
    output_file.write("\n</kml>")


def convert_to_mph(speed_in_knots):
    """
    To covert the given speed in knots to speed in mph
    :param speed_in_knots: Speed in knots
    :return: Speed in mph
    """
    return 1.15078 * float(speed_in_knots)


def convert_time_to_secs(input_time):
    """
    To convert input time to mins from hhmmss.ss format
    :param input_time: The input time to convert
    :return: Time in minutes
    """
    hours = input_time[:2]
    minutes = input_time[2:4]
    second = input_time[4:]

    hours = int(hours) * 60 * 60
    minutes = int(minutes) * 60
    second = float(second)

    return hours+minutes+second


def get_max_velocity(all_data):
    """
    Get the max velocity for each trip
    :param all_data: list of lists containing all the data
    :return: Max velocity for a given trip
    """
    max_velocity = 0
    for data in all_data:
        if max_velocity < data[3]:
            max_velocity = data[3]
    return max_velocity


def get_cost_function(all_data):
    """
    Get the cost function for each trip
    :param all_data: list of lists containing all data
    :return: Returns cost for a given trip
    """
    # Get the start time and the end time and calculating the cost based on that
    first_time = all_data[0][0]
    last_time = all_data[len(all_data)-1][0]

    max_velocity = get_max_velocity(all_data)/120

    travel_time = (last_time - first_time)/(60*30)
    return travel_time+max_velocity


def read_text_file(file_name):
    """
    Read the text file and create a list of lists for all the data
    :param file_name: Path of the input file
    :return: list of lists containing all data
    """

    with open(file_name, "r") as input_file:

        # Skip the first 5 lines
        for _ in range(SKIP_LINES):
            next(input_file)

        # CSV reading
        csv_reader = csv.reader(input_file, delimiter=",")

        # Set to store all the coordinates
        all_data = list()

        for line in csv_reader:

            # If the line is of RMC type separate the data out
            if line[0] == TYPES_OF_DATA[0] and line[2] != 'V':
                latitude = convert_to_degrees_mins(line[3], "latitude", line[4])
                longitude = convert_to_degrees_mins(line[5], "longitude", line[6])
                time = convert_time_to_secs(line[1])
                date = line[9]
                speed = convert_to_mph(line[7])
                tracking_angle = float(line[8])

            # You don't want duplicate data values
            else:
                continue
            all_data.append([time, longitude, latitude, speed, tracking_angle, date])

        # To remove all duplicate entries
        all_data = remove_duplicates(all_data)
    return all_data


def get_all_stop_signs(all_data):
    """
    To get a list of all the stop signs within a given route
    :param all_data: List of data for a given route
    :return: List of stop sign coordinates
    """
    stop_signs = []

    for i in all_data:

        # To check the next 10 points after the current set of points
        for j in all_data[all_data.index(i)+1: all_data.index(i)+10]:

            # When the speed is below the speed for the stop sign threshold and when the difference in time for the
            # points is greater than the threshold
            if j[0] - i[0] >= STOP_SIGN_TIME_THRESHOLD and \
                    i[3] <= STOP_SIGN_SPEED_THRESHOLD:

                if not stop_signs:
                    stop_signs.append((i[1], i[2]))
                else:
                    last_position = stop_signs[-1]

                    # Finding the distance between the current stop sign and the previous stop sign
                    distance_difference = math.sqrt((i[1] - last_position[0]) ** 2 +
                                                    (i[2] - last_position[1]) ** 2)

                    # if the distance is less than the threshold delete the previous
                    if distance_difference <= STOP_SIGN_LAST_SIGN_THRESHOLD:
                        del stop_signs[-1]
                    stop_signs.append((i[1], i[2]))
    return stop_signs


def get_all_left_turns(all_data):
    """
    To get all the left turns
    :param all_data: List of data for a given route
    :return: List of coordinates for a left hand turn
    """

    # To store all the list of left turns
    left_turns = []

    for i in all_data:

        # We check for the next 10 set of data points
        for j in all_data[all_data.index(i)+1: all_data.index(i)+10]:

            # To validate if the tracking angle lies between the given range and if the speed is greater than 1
            # The assumption I am making here is that the tracking angle is wider for a left turn as compared to a right
            # one. The speed is checked because at 0 speed the tracking angle keeps fluctuating
            if MIN_ANGLE <= abs(j[-2] - i[-2]) <= MAX_ANGLE and i[3] >= LEFT_TURN_SPEED_THRESHOLD:

                # If its the first left turn encountered add it to the list
                if not left_turns:
                    left_turns.append((i[1], i[2]))
                else:
                    last_position = left_turns[-1]

                    # Finding the distance between the current point and the previous turn point
                    distance_difference = math.sqrt((i[1] - last_position[0]) ** 2 +
                                                    (i[2] - last_position[1]) ** 2)

                    # If the encountered point is very close to the previous encountered left turn point update the
                    # left turn in question
                    if distance_difference <= LEFT_TURN_LAST_SIGN_THRESHOLD:
                        del left_turns[-1]
                    left_turns.append((i[1], i[2]))
    return left_turns


def main():
    """
    Main calling function for the program
    :return: None
    """
    # Create output folder if it doesn't exist
    if not os.path.exists(OUTPUT_KML_FILES_FOLDER):
        os.makedirs(OUTPUT_KML_FILES_FOLDER)

    # To create KML files in the Output Files folder and print stop signs
    print("\nSTOP SIGNS & LEFT TURNS FOR THE FILES: ")
    for file_name in GPS_FILES:

        # Emit the header
        output_file = emit_header(file_name)

        # Convert the input into a KML
        convert_to_kml(os.path.join(INPUT_FILES_FOLDER, file_name), output_file)

        # Get all the data for the stop sign and left turn evaluation ready
        all_data = read_text_file(os.path.join(INPUT_FILES_FOLDER, file_name))

        # Get all the stop signs
        stop_signs = get_all_stop_signs(all_data)

        # Plot all the stop signs
        plot_stop_signs(stop_signs, output_file)
        print("\n"+file_name + ": " + str(stop_signs))

        # Get all the left turns for a route
        left_turns = get_all_left_turns(all_data)

        # Plot all the left turns for the route
        plot_left_turns(left_turns, output_file)
        print(file_name + ": " + str(left_turns))

        # Emit the trailer for the output KML file
        emit_trailer(output_file)

    # Calculate the cost function for all the files
    print("\n\n\nCOST FUNCTION FOR THE FILES: ")
    for file_name in GPS_FILES:
        all_data = read_text_file(os.path.join(INPUT_FILES_FOLDER, file_name))
        print(file_name + ": " + str(get_cost_function(all_data)))

    # To move all the files to the output file to the output folder
    for file_name in GPS_FILES:
        os.rename(os.path.join(PROGRAM_PATH, file_name[:-4] + "_OUTPUT.kml"),
                  os.path.join(OUTPUT_KML_FILES_FOLDER, file_name[:-4] + "_OUTPUT.kml"))


if __name__ == '__main__':
    main()