# week 3 python 1 class
'''
Name: Jamie Jamison
Date: 2021-10-22
Description:  program 2 part 2

roster_extended.csv

'''
# adds a new person line to raster_content 
def add_person():    
    fname = input('First Name: ')
    lname = input('Last Name: ')
    age = input('Age: ')
    occup = input('Occupation: ')
    height = input('Height (in inches): ')
    if height.isnumeric() == False:
        height = input('Height (in inches) must be an integer: ')
    weight = input('Weight (in pounds): ')
    if weight.isnumeric() == False:
        weight = input('Weight (in pounds) must be an integer: ')
    lifestyle = input('Lifestyle (1-sedentary, 2-moderate, 3-active): ')
    if lifestyle == '1':
        lifestyle = "sedentary"
    elif lifestyle == '2':
        lifestyle = "moderate"
    elif lifestyle == '3':
        lifestyle = "active"
    else:
        lifestyle = input("Incorrect input. Please enter 1, 2 or 3 for Lifstyle choice. ")
        
    new_line = ('{}, {}, {}, {}, {}, {}, {}\n'.format(fname, lname, age, occup, height, weight, lifestyle,'\n'))
        
    return(new_line)
        
# convert inches to feet
def inches2feet(height):
    height_feet = height//12
    height_inches = height % 12
    new_ht = str(height_feet) + "'" + str(height_inches) + '"'
    return new_ht


# initial greeting to user, greeting can change
greeting = 'Hello.'
print(greeting)

# read-only is the default but set to be careful
roster_file = open(input("Please enter a roster file: "), "r")


# read the header first to get rid of it then read the content
header = roster_file.readline()
#print(header)
roster_content = roster_file.readlines()
roster_file.close()

num_names = len(roster_content)
print("There are {0} names in this file. Would you like to enter additional names? (Y/N)".format(num_names))

new_names = int(input("How many more names? "))

#print("adding {0} names.".format(num_names))

for new_names in range(0,new_names):
    print('{0:-^11}'.format(' ' + str(new_names+1) + ' ' ))   
    roster_content.append(add_person())


# split up roster_content
roster_content_split = []

for name in roster_content:
    current_row = name.replace('\n', '')    
    roster_content_split.append(current_row.split(',')) 
    
#print(roster_content_split)
# get lengths
# variable lengths
longestfirst = 9
longestlast = 8
age_length = 3
longestoccupation = 10
height_length = 5
weight_length = 3
activity_length = 10

#print(longestfirst, longestlast, longestoccupation)

for person in roster_content_split:

    ## First Name: if name is longer than longestfirst, then I need to update longestfirst
    if len(person[0]) > longestfirst:
        longestfirst = len(person[0])

    ## Last Name: if name is longer than longestlast, then I need to update longestlast
    if len(person[1]) > longestlast:
        longestlast = len(person[1])
        
    ## occupation: if name is longer than longestlast, then I need to update longestlast
    if len(person[3]) > longestoccupation:
        longestoccupation = len(person[3])    
    
    ## occupation: if name is longer than longestlast, then I need to update longestlast
    if person[6] == 'x':
        person[6] = 'n/a' 
    elif person[6] == '':
        person[6] = '99'  # ie. missing data

print(longestfirst, longestlast, longestoccupation)

type(longestfirst)


# the output file
roster_out = open(input("Save new roster file as:  "), "w")

# header
header = '{:>{var1}} {:>{var2}} {:>3} {:>{var3}} {:>15} {:>15} {:>15} \n'.format('First', 'Last', 'Age', 'Occupation', 'Ht', 'Wt', 'Lifestyle', var1 = longestfirst, var2 = longestlast, var3 = longestoccupation)
roster_out.write(header)

for person in roster_content_split:
    # Anna', 'Barbara', '35', 'nurse', '63', '129', '', 'x', '']
    personformat = '{:>{var1}} {:>{var2}} {:>3} {:>{var3}} {:>15} {:>15} {:>15} \n'.format(person[0], person[1], person[2], person[3], inches2feet(int(person[4])), person[5], person[6], var1 = longestfirst, var2 = longestlast, var3 = longestoccupation)
    #print(personformat)
    #roster_strings = ''.join(roster_content_split)
    roster_out.write(personformat)
    
roster_out.close()
print("File saved!")