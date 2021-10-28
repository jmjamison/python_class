# week 3 python 1 class
'''
Name: Jamie Jamison
Date: 2021-10-22
Description:  program 2 part 2

roster_extended.csv

'''
'''
function creates a new person line, returns that line to be appended to roster_content
'''
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
        

'''
convert inches to feet, called when printing out the report, height
'''
def inches2feet(height):
    height_feet = height//12
    height_inches = height % 12
    new_ht = str(height_feet) + "'" + str(height_inches) + '"'
    return new_ht

'''
initial greeting to user, greeting can change, example:  Happy Holidays instead of Hello
'''
greeting = 'Hello.'
print(greeting)

'''
read-only is the default but set here to be careful
assume that the input files are in the same directory as the program
'''
try:
    roster_file = open(input("Please enter a roster file: "), "r")
except IOError:
    print('File not found! try again.')
    roster_file = open(input("Please enter a roster file: "), "r")


# readline the header first to get rid of it 
header = roster_file.readline()
# then read the rest of the file content
roster_content = roster_file.readlines()
roster_file.close()


# how many names/lines are in the file
num_names = len(roster_content)
add_more_names_response = input("There are {0} names in this file. Would you like to enter additional names? (Y/N)".format(num_names))
if add_more_names_response == 'Y' or add_more_names_response =='y':
    new_names = int(input("How many more names? "))
    for new_names in range(0,new_names):
        print('{0:-^11}'.format(' ' + str(new_names+1) + ' ' ))
        roster_content.append(add_person())
    print('-'*11)
elif add_more_names_response == 'N' or add_more_names_response =='n':
    # go straight to print
    print('-'*11)
else:
    print("Please choose Y or N.")
    add_more_names_response = input("There are {0} names in this file. Would you like to enter additional names? (Y/N)".format(num_names))



# split up roster_content
roster_content_split = []

for name in roster_content:
    current_row = name.replace('\n', '')    
    roster_content_split.append(current_row.split(',')) 
    
'''
variable lengths, these are the default column widths 
'''
longestfirst = 9
longestlast = 8
age_length = 3
longestoccupation = 10
height_length = 5
weight_length = 3
activity_length = 10

'''
Check the first name, last name and occupation in case those are wider than the default width
'''
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
    
    ## if lifesyle isn't 1, 2 or 3 replace with n/a for x and 99 for blanks.
    if person[6] == 'x':
        person[6] = 'n/a' 
    elif person[6] == '':
        person[6] = '99'  # ie. missing data

# debugging code
# print(longestfirst, longestlast, longestoccupation)

# the output file
roster_out = open(input("Save new roster file as:  "), "w")

# header
header = '{:>{var1}} {:>{var2}} {:>3} {:>{var3}} {:>15} {:>15} {:>15} \n'.format('First', 'Last', 'Age', 'Occupation', 'Ht', 'Wt', 'Lifestyle', var1 = longestfirst, var2 = longestlast, var3 = longestoccupation)
roster_out.write(header)

for person in roster_content_split:
    # Anna', 'Barbara', '35', 'nurse', '63', '129', '', 'x', '']
    personformat = '{:>{var1}} {:>{var2}} {:>3} {:>{var3}} {:>15} {:>15} {:>15} \n'.format(person[0], person[1], person[2], person[3], inches2feet(int(person[4])), person[5], person[6], var1 = longestfirst, var2 = longestlast, var3 = longestoccupation)
    roster_out.write(personformat)
    
roster_out.close()
print("File saved!")