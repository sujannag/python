"""
This example is to load datasets from a csv file format.
In this example code we will try to read data from a csv file and also
write data back to another csv file.

"""

# imports the CSV
import csv

# defines the number of instances to work with
l_instance = 1

# open the CSV File in read only format

# Actual Dataset
#with open('housing_dataset.csv', 'rb') as csvread:


# Temp Data set
with open('housing_dataset.csv', 'rb') as csvread:
    reader = csv.reader(csvread)
    #for x in xrange(l_instance):                 # for loop executing 3 times
    #    print reader.next()             # prints the first three rows of the dataset


# open a new csv file to write data to
    with open('housing_updated.csv', "wb") as csvwrite:
        writer = csv.writer(csvwrite)

        #for row in reader:         # To write all the rows
        for x in xrange(3):         # To write 3 rows
            writer.writerow(reader.next())

csvread.close()
csvwrite.close()