'''
Week 2 Python Notes

Agenda:
* eval()
* input()
* Execution Control (if, elif, else)
* for-loops and range()
* strings
* formatted output
* files
'''



"""
########## eval() ##########
## eval() takes a string and evaluates the string as if it were a Python expression
w = 4       ## int type
t = '4'     ## string type

print(type(w))
print(type(t))

x = eval(t)     ## 4 in Python is a number

print(x)            ## x was evaluated as a number because 4 in Python is a number
print(type(x))      ## x is seen as an int

"""
"""

########## input() ##########
 #ERROR Example
print('Hello, what is your name? ')
name = input()                      ## In this example, it's separate
print('Welcome,', name)

age = input('How old are you? ')    ## print and input prompt combined; print text first and then wait for user input
print(type(age))                    ## age is being interpreted as a string
agedays = age * 365.25
print(agedays)


"""


# CORRECT Example
print('Hello, what is your name? ')
name = input()                      ## In this example, it's separate
print('Welcome,', name)

age = eval(input('How old are you? '))      #eval() evaluates the input as if it were Python code;
                                            # whatever number it's given will be interpreted as a number
print(type(age))                    ## age is being interpreted as a string
agedays = age * 365.25
print(agedays)
"""
"""

"""
eval('10')          ## evaluates the number 10
eval('53//7')       ## evaluate the value of 53 // 7
eval('[1,2,3,4]')   ## evaluate [1,2,3,4] for what it means in Python, a list
eval('Hello')       ## evaluates Hello as if it were a line of code in Python, but variable Hello doesn't exist
"""

"""
##### Task: Ask user for length in yards and convert to meters #####
# 1.094 meters in a yard

def ydstom(yards):
    'Convert yards to meters'
    meters = yards/1.094
    return meters

yrds = eval(input('How many yards? '))          ## Don't forget eval() since we are expecting a number
m = round(ydstom(yrds), 2)
print(yrds, "yards is", m, "meters")            ## By default, Python adds in spaces for you between print items
"""

"""
##### Task: Ask the user for a height in inches and convert to ft-in #####
# 12 inches to 1 foot

def intoft(inches):
   'Convert inches to feet inches'
   ft = inches // 12
   inch = inches % 12
   ftinch = str(ft) + "'" + str(inch) + '"'
   return ftinch

userinput = eval(input('How many inches tall? '))
height = intoft(userinput)
print(userinput, "inches is", height)           ## <<userinput>> inches is <<height>>
"""


########## Execution Control, if-statements ##########

"""
## One-way decision: Height requirement
## Scenario: amusement park with 125 cm minimum height requirement to ride
## Stop the rider if they are not tall enough


hinches = eval(input("Enter your height in inches: "))
hcm = hinches * 2.54
if hcm < 125:
    'the rider is shorter than 125'
    print('STOP! YOU SHALL NOT PASS!')
    print('You are not tall enough')
## once you stop indenting, you are no longer in the if-statement
print('Have a nice day! =)')
"""

"""
## Two-way decision: Height requirement
## Scenario: amusement park with 125 cm minimum height requirement to ride
## Stop the rider if they are not tall enough
## Allow the rider on otherwise

hinches = eval(input("Enter your height in inches: "))
hcm = hinches * 2.54
if hcm < 125:
    'the rider is shorter than 125'
    print('STOP! YOU SHALL NOT PASS!')
    print('You are not tall enough')
else:
    print('You are tall enough. Enjoy the ride!')
## once you stop indenting, you are no longer in the if-statement
print('Have a nice day! =)')
"""


"""
## More decisions: Height requirement
## Scenario: amusement park with 125 cm minimum height requirement to ride
##           reserved row for those between 110-125 cm
## Stop the rider if they are not tall enough
## Offer a reserved seat if they are between 110 and 125
## Allow the rider on otherwise

hinches = eval(input("Enter your height in inches: "))
hcm = hinches * 2.54

if hcm < 110:
    'the rider is shorter than 110'
    print('STOP! YOU SHALL NOT PASS!')
    print('You are not tall enough')
elif hcm < 125:
    print('Would you like to sit in the reserved row?')
else:
    print('You are tall enough. Enjoy the ride!')

print('Have a nice day! =)')
"""

"""
## Another example with reversed if-statements
hinches = eval(input("Enter your height in inches: "))
hcm = hinches * 2.54
if hcm >= 125:
    print('You are tall enough. Enjoy the ride!')
elif hcm >= 110:
    print('Would you like to sit in the reserved row?')
else:
    print('STOP! YOU SHALL NOT PASS!')
    print('You are not tall enough')
print('Have a nice day! =)')
"""


"""
## BAD EXAMPLE (two ifs, even though everything belongs together)
hinches = eval(input("Enter your height in inches: "))
hcm = hinches * 2.54
if hcm >= 125:
    print('You are tall enough. Enjoy the ride!')
if hcm >= 110:                                      ## a person who is tall enough will also be offered the reserved row
    print('Would you like to sit in the reserved row?')
else:
    print('STOP! YOU SHALL NOT PASS!')
    print('You are not tall enough')
print('Have a nice day! =)')
"""

"""
## BAD EXAMPLE (condition checking order)
hinches = eval(input("Enter your height in inches: "))
hcm = hinches * 2.54
if hcm >= 110:                                      ## a person who is tall enough will always be offered the reserved row
    print('Would you like to sit in the reserved row?')
elif hcm >= 125:
    print('You are tall enough. Enjoy the ride!')
else:
    print('STOP! YOU SHALL NOT PASS!')
    print('You are not tall enough')
print('Have a nice day! =)')
"""

"""
## You can have as many elif as you want
hinches = eval(input("Enter your height in inches: "))
hcm = hinches * 2.54
if hcm >= 125:
    print('You are tall enough. Enjoy the ride!')
elif hcm >= 110:
    print('Row 1')
elif hcm >= 100:
    print('Row 2')
elif hcm >= 90:
    print('Row 3')
else:
    print('STOP! YOU SHALL NOT PASS!')
    print('You are not tall enough')
print('Have a nice day! =)')
"""

"""
## More decisions: Height requirement
## Scenario: amusement park with 125 cm minimum height requirement to ride
##           reserved row for those between 110-125 cm
## Stop the rider if they are not tall enough
## Offer a reserved seat if they are between 110 and 125
##      + Interaction
## Allow the rider on otherwise

hinches = eval(input("Enter your height in inches: "))
hcm = hinches * 2.54

if hcm < 110:
    'the rider is shorter than 110'
    print('STOP! YOU SHALL NOT PASS!')
    print('You are not tall enough')
elif hcm < 125:
    response = input('Would you like to sit in the reserved row [Y/N]?')
    if response == 'Y':
        print('Right this way.')
    else:
        print('Sorry, please enjoy a different ride.')
else:
    print('You are tall enough. Enjoy the ride!')

print('Have a nice day! =)')

"""

"""
## Amusement Park Height with Functions

def intocm(inches):
    return inches * 2.54

def checkHeight(inches):
    hcm = intocm(inches)
    if hcm < 110:
        'the rider is shorter than 110'
        print('STOP! YOU SHALL NOT PASS!')
        print('You are not tall enough')
    elif hcm < 125:
        response = input('Would you like to sit in the reserved row [Y/N]?')
        if response == 'Y':
            print('Right this way.')
        else:
            print('Sorry, please enjoy a different ride.')
    else:
        print('You are tall enough. Enjoy the ride!')

    print('Have a nice day! =)')


hinches = eval(input("Enter your height in inches: "))
checkHeight(hinches)
"""


########## for loops ##########
"""
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)
"""

"""
for i in range(1, 101):     ## start at 1, end before 101, increment 1
    print('Hello')
    print("The value of i is now:", i)

print("The value of i outside is now:", i)  ## variable i still exists and will be the last loop value
"""

"""
for i in range(20):         ## start at 0, end before 20, increment 1
    print(i)
"""

"""
for j in range(1, 101, 2):      ## start at 1, end before 101, increment by 2
    print(j)
"""

"""
for num in range(500, -500, -100):
    print(num)
"""

"""
for num in range(20, 10, 3):    ## Nothing happens because we are already beyond the 10 cut-off (and adding by 3 to 20 will not bring us towards 10)
    print(num)
"""

"""
for i in reversed(range(0,10)):
    print(i)
"""


"""
########## for-loops with lists and strings ##########
mylist = ['milk', 'eggs', 'bread', 'bananas', 'ham']
for item in mylist:             ## item is first 'milk', then it will be 'eggs', then 'bread', ...
    print('I went to the store and bought', item)


text ='my really extremely truly long string text in Python'
for letter in text:
    print("Letter:", letter)

for letter in 'open':
    print(letter)
"""

"""
########## Combination range, but also looping through a list ##########
## 1. milk
## 2. eggs
## 3. bread
## ...
mylist = ['milk', 'eggs', 'bread', 'bananas', 'ham']
print('I need the following items from the store:')
for i in range(len(mylist)):            ##range(5) so 0, 1, 2, 3, 4
    print(str(i+1) + '.', mylist[i])    
    print(i + 1, '. ', mylist[i], sep='')   ## this will also give the same thing.
                                            ## sep = '' tells Python that you don't want the default space given at commas
"""

"""
##### Write a function that spells a given word backwards #####
def reverseSpell(word):
    'return a string with the reverse spelling of a word'       # e, en, eno, enoh, enohp
    reverseword = ''
    for i in reversed(range(len(word))):        # 4, 3, 2, 1, 0
        reverseword = reverseword + word[i]
        #print(reverseword)
    return reverseword

print(reverseSpell('phone'))
"""

"""
## Scenario: write a function that takes in 2 or 3 names (last, first, middle)
## Your function should return a string with the first name and last name printed in order
## If there is a middle name, print just the initial followed with a period
## First M. Last
def firstmlast(last, first, middle = None):
    'returns names in First M. Last order'
    if middle == None:
        return first + ' ' + last
    else:
        return first + " " + middle[0] + ". " + last

print(firstmlast("Geller", "Ross", "Eustace"))
print(firstmlast("Buffay", "Phoebe"))
print(firstmlast(last = "Bing", middle = "Muriel", first = "Chandler"))
print(firstmlast('Green', 'Rachel', 'Geller', 'Monica'))
"""


"""
help(print)
print('hello')
print('bye')

print('hello', end = '')    ## stops the new line after print
print('bye')
"""


"""
##### print() #####
n = 1919
mascot = "Bruins"
school = "UCLA"

print(n, mascot, school)
print(n, mascot, school, sep = "")
print(n, mascot, school, sep = ';')
print(n, mascot, school, sep = '\t')        ## separated by tab
print(n, mascot, school, sep = '\n')

print(n, mascot, school)
print(n, mascot, school, end = "")
print(n, mascot, school, end = ';')
print(n, mascot, school, end = '!!!')        ## separated by tab
print(n, mascot, school, end = '4832478')
"""


##### more strings #####

"""
## multi-line strings
fish1 = 'One fish\nTwo fish\nRed fish\nBlue fish'
fish2 = '''Black fish
Blue fish
Old fish
New fish'''
print(fish1)    ##print() is automatically adding a new line after "Blue fish"
print(fish2)    ##print() is also adding a new line after "New fish"
"""

"""
########## String methods/functions ##########
## For the following few functions, we need to use the object.method() format
## For table, refer to textbook page 97 (Table 4.1 String methods)
funstring1 = "i'm having fun programming in Python! Are you having fun programming in Python?"
funstring2 = 'i\'m having fun programming in Python! Are you having fun programming in Python?'
print(funstring1 == funstring2)

## print each of these to see what happens
funstring1.capitalize()
funstring1.count('programming')
funstring1.lower()
funstring1.replace("Python", "C")

secretcode = str.maketrans('abcdef', 'uvwxyz')
secretstring = funstring1.translate(secretcode)
# a -> u
# b -> v
# c -> w
# d -> x
# e -> y
# f -> z

print(funstring1)       ## because I did not save the mutated string anywhere, funstring is still it's original form
print(secretstring)
"""


##### formatted output #####
"""
roster = ['Anna Barbara', 'Catherine Do', 'Eric Frederick',
        'Gabriel Hernandez', 'Ivy Joo', 'Kelly Marks']
for name in roster:
    print(name)
"""

"""
roster = ['Anna Barbara', 'Catherine Do', 'Eric Frederick',
        'Gabriel Hernandez', 'Ivy Joo', 'Kelly Marks']
for name in roster:
    splitname = name.split()    ## by default the name will be split at the spaces and put into a list
    formattedname = '{2:10} {0:12}-----{1:10}'.format(splitname[0], splitname[1], 'hello')
    print(formattedname)
"""

