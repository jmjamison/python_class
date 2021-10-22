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
        
        print('{0:-^11}'.format(' ' + str(num+1) + ' ' ))
        
        fname = input('First Name: ')
        lname = input('Last Name: ')
        age = input('Age: ')
        occup = input('Occupation: ')
        height = input('Height (in inches): ')
        weight = input('Weight (in pounds): ')
        lifestyle = input('Lifestyle (1-sedentary, 2-moderate, 3-active): ')
        line = '{}, {}, {}, {}, {}, {} ,{}\n'
        new_lines +=  line.format(fname, lname, age, occup, height, weight, lifestyle)
        
    return(new_lines)
        
def inches2feet(height):
    height_feet = height//12
    height_inches = height % 12
    return (height_feet, height_inches)




# variable lengths
longestfirst = 9
longestlast = 8
age_length = 3
longestoccupation = 10
height_length = 5
weight_length = 3
activity_length = 10


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

print(longestfirst, longestlast)

for person in roster_content:

    ## First Name: if name is longer than longestfirst, then I need to update longestfirst
    if len(person[0]) > longestfirst:
        longestfirst = len(person[0])
        print(person[0])

    ## Last Name: if name is longer than longestlast, then I need to update longestlast
    if len(person[1]) > longestlast:
        longestlast = len(person[1])
        print(person[1])


print(longestfirst, longestlast)



# the output file
roster_out = open(input("Save new roster file as:  "), "w")
roster_strings = ''.join(roster_content)
roster_out.write(roster_strings)
roster_out.close()
print("File saved!")
