__author__= "Aditya Kalyan Jayanti & Rohit Ravishankar"
__email__= "aj8582@rit.edu & rr9105@rit.edu" 


def classifier(csv_file):

	# To write the result of classification
	file = open('HW_05_Jayanti_AdityaKalyan_Ravishankar_Rohit_MyClassifications.csv','w')
	rows = csv_file.readlines()

	# Dictionary to store each row of data
	columns_with_data = {}

	# To store column headers in a list
	attributes = []
	attributes_name = rows[0].split(',')
	for attribute in attributes_name:
		columns_with_data[attribute]=0
		attributes.append(attribute)

	# Iterating from 1 through all rows because the first row has only headers 
	for index in range(1,len(rows)):
		line = rows[index].split(',')
		line=line[0:len(rows[0])]
		for i in range(1,len(line)):
			columns_with_data[attributes[i]]= float(line[i])
		my_classifier_function(file, columns_with_data)


def my_classifier_function(file, columns_with_data):
		if columns_with_data["Sugar"]<=19:
			if columns_with_data["Egg"]<=12:
				if columns_with_data["Butter or Margarine"]<=18:
					if columns_with_data["Baking Powder"]<=2:
						file.write('1\n')
					else:
						if columns_with_data["cinnamon"]<=11:
							file.write('0\n')
						else:
							file.write('1\n')
				else:
					file.write('0\n')
			else:
				file.write('0\n')
		else:
			if columns_with_data["Canned Pumpkin_or_Fruit"]<=26:
				if columns_with_data["Vanilla"]<=6:
					file.write('0\n')
				else:
					file.write('1\n')
			else:
				file.write('1\n')


def main():

	# for any new validation set, the path must be entered here
	csv_file = open('Recipes_For_VALIDATION_2181_RELEASED_v202.csv', 'r')
	classifier(csv_file)


if __name__ == '__main__':
	main()
