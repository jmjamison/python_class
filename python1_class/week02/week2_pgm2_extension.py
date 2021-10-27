# week 2 python 1 class
'''
Name: Jina (Jamie) Jamison
Date: Oct 8, 2021
Description:
    1) prompt user for a general category of things
    2) prompt the user for five things to put in the list
        ** change to ask the user for the size of the list
    3) ask the user to enter a number between one and five
        ** check for blanks
    4) based on the numeric input(n), print the n-th item in the sorted list
    5) print the sorted list
    6) prompt the user for a character
    7) print a list of booleans reflecting whether the user-entered character is in each element of the list

'''

print("Let's create a list of things. Think of a general category.")

category = input("What category of things should we store? (One word or name with no spaces): ")
#print(category)
list_size = eval(input("How many things would you like it this list? "))

category_list=[]

for x in range(list_size):
    category_list.append(input(category + " " + str(x+1) + ": "))

pick_number = eval(input("\nPick a number between 1 and " + str(list_size) + ": "))

# test that the number is really between 1 and 5

print("You picked", str(category_list[pick_number-1])+"!")

# sort the list
sorted_category_list = sorted(category_list)

print("\nThe sorted list is:", sorted_category_list)

# pick a character
test_character = input("\nPick a single character: ")

## This is problably not the best way to do this but the only way I could get
##     output that looked correct

boolean_category_list=[]
for x in range(list_size):
    boolean_category_list.append(test_character in sorted_category_list[x])

print(boolean_category_list)

# test that the number is really between 1 and 5

