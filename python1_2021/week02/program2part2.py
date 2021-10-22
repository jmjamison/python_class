# week 3 python 1 class
'''
Name: Jamie Jamison
Date: 2021-10-22
Description:  program 2 part 2


'''
def add_people(x):
    how_many = x
    print("adding {0} names.".format(x))
    
    for num in range(0,int(how_many)):
        print(num+1)
        

#import os

#cwd = os.getcwd()
#print("Current working directory: {0}".format(cwd))
# use roster_extended.csv

greeting = 'Hello.'

print(greeting)

# read-only is the default but set to be careful
roster_file = open(input("Please enter a roster file: "), "r")
# read the header first to get rid of it then read the content
header = roster_file.readline()
#print(header)
roster_content = roster_file.readlines()
roster_file.close()


#print(roster_content)

num_names = len(roster_content)
print("There are {0} names in this file. Would you like to enter additional names? (Y/N)".format(num_names))

num_names = input("How many more names? ")

add_people(num_names)