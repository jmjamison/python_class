
def intoft(inches):
    'returns a string value of the height in feet\'inches"'
    ft = inches//12       ## 12 inches to 1 foot
    inch = inches%12
    return str(ft) + "'" + str(inch) + '"'

def kgtolb(kg):
    'take weight in kg and return weight in pounds'
    return round(kg * 2.20462, 1)

## first name
## last name
## age
## height in inches  -- convert this to ft inches
## weight in kg  -- convert this to pounds
roster = [['Anna','Barbara', 35, 60, 58.5],
           ['Catherine','Do', 45, 65, 61.5],
           ['Eric','Frederick', 28, 65, 63.5],
           ['Gabriel','Hernandez', 55, 70, 68],
           ['Ivy','Joo', 31, 55, 57],
           ['KellyAnneMary','Marks', 21, 75, 60]]


longestfirst = 5        ## need 5 spaces minimum for first name
longestlast = 5         ## need 5 spaces minimum for last name

print(longestfirst, longestlast)

for person in roster:

    ## First Name: if name is longer than longestfirst, then I need to update longestfirst
    if len(person[0]) > longestfirst:
        longestfirst = len(person[0])

    ## Last Name: if name is longer than longestlast, then I need to update longestlast
    if len(person[1]) > longestlast:
        longestlast = len(person[1])


print(longestfirst, longestlast)