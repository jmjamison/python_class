# week 2 python 1 class
'''
Name: Jina (Jamie) Jamison
Date: Oct 8, 2021 (due: Oct 9, 2021)
Description:  Original Assignment
    1) Ask the user for two numbers, 2 heights in inches;
    2) the program should also print a mathematical statement for the subtraction of the two numbers -
        given by teh user, first number - second number showing how much taller the first person is to
        the second and show the heights in feet- inches.

##--------------------------------------------------------------

# Convert inches to feet and inches
'''
def intoft(inches):
   'Convert inches to feet inches'
   ft = inches // 12
   inch = inches % 12
   ftinch = str(ft) + "'" + str(inch) + '"'
   return ftinch


## Person[] holds the list of 2 persons heights
Person=[]

print("Enter two numbers (heights in inches).")

## Input the Heights
for x in range(2):
    #print(x) # debugging code
    Person.append(input("Person " + str(x+1) + " Height: "))
    # print(Person) # debugging code

# print(len(Person)) # debugging code

# print the math statement subtracting first - second
answer = (int(Person[0]) - int(Person[1]))


# print the math statement subtracting first - second
answer = (int(Person[0]) - int(Person[1]))
print(Person[0], "-", Person[1], " = ", answer)
print(" Person 1 is", answer, "inches taller than Person 2")

# convert the inches to feet and inches


# Print out heights in inches and feet
for y in range(len(Person)):
    print("Person", y+1, "is", intoft(eval(Person[y])))
