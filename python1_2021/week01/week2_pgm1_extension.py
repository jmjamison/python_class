# week 2 python 1 class
'''
Name: Jina (Jamie) Jamison
Date: Oct 8, 2021 (due: Oct 9, 2021)
Description:  Assignment with Additions
    1) Ask the user for two numbers, 2 heights in inches;
    2) the program should also print a mathematical statement for the subtraction of the two numbers -
        given by teh user, first number - second number showing how much taller the first person is to
        the second and show the heights in feet- inches.
    3) Added code to print whether Person1 is taller, same height or shorter than Person2

##--------------------------------------------------------------

# Convert inches to feet and inches  ( from class example)
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
    # print(Person)  # debugging code

# print(len(Person))  # debugging code

# print the math statement subtracting first - second
answer = (int(Person[0]) - int(Person[1]))

# print the math statement subtracting first - second
print(Person[0], "-", Person[1], " = ", answer)

# test if Person1 is taller, same as or shorter than Person2
if answer > 0:
    print("Person 1 is", answer, "inches taller than Person 2")
elif answer == 0:
    print("Persons 1 and 2 are the same height.")
elif answer < 0:
    print("Person 1 is", abs(answer),  "inches shorter than Person 1")


# Print out heights in inches and feet
for y in range(len(Person)):
    print("Person", y+1, "is", intoft(eval(Person[y])))
