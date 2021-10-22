# week 3 python 1 class
'''
Name: Jamie Jamison
Date: 2021-10-22
Description:  program 2 part 2


'''
def add_people(x):
    how_many = x
    print("adding {0} names.".format(x))
    new_lines=''
    
    for num in range(0,int(how_many)):
        print(num+1)
        fname = input('Enter first name: ')
        lname = input('Enter last name: ')
        age = input('Enter age: ')
        occup = input('Enter occupation: ')
        height = input('Enter height (in inches): ')
        weight = input('Enter weight (in pounds): ')
        lifestyle = input('Choose lifestyle - 1-sedentary, 2-moderate, 3-active: ')
        line = '{}, {}, {}, {}, {}, {} ,{}\n'
        new_lines +=  line.format(fname, lname, age, occup, height, weight, lifestyle)
        
    return(new_lines)
        
        

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


print(roster_content)

num_names = len(roster_content)
print("There are {0} names in this file. Would you like to enter additional names? (Y/N)".format(num_names))

num_names = input("How many more names? ")

new_names = add_people(num_names)

roster_content.append(new_names)

print(roster_content)

# the output file
roster_out = open(input("Save new roster file as:  "), "w")
roster_strings = ''.join(roster_content)
roster_out.write(roster_strings)
roster_out.close()
print("File saved!")
