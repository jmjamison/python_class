# try same with BeautifulSoup
# part one get the story
from bs4 import BeautifulSoup
from urllib.request import urlopen
from re import findall
import re
from urllib.error import HTTPError

#def make_dictionary_list():
    

# term list
term_list = []
# dictionary 
dictionary_list = {}


# 1) get the short story path
url = ' http://classicshorts.com/stories/'
# story = "btw" + ".html"
#story = input("What's the short story path? ")
# typo, user enters alpha character - which I did at least once
#fullURL = url + story + ".html"
#print(fullURL)

# if type or not found:  HTTPError: HTTP Error 404: Not Found
wrong_site = True
while wrong_site:
    try:
        story = input("What's the short story path? ")
        fullURL = url + story + ".html"
        response = urlopen(fullURL)
        soup = BeautifulSoup(response, 'html.parser')
        definition_line = soup.find_all(href=re.compile("dictionary"))

        for line in soup.find_all(href=re.compile("dictionary")):
            #term = str(line.contents )
            term = re.sub(r"[^a-zA-Z0-9]","", str(line.contents ))
            #print(term, type(term)) debugging code
            term_list.append(term)    
        
        dictionary_list = {}.fromkeys(term_list, '-')
        print(dictionary_list)

        #print(term_list)    # debugging code
        #print(dictionary_list)
        #for key, value in dictionary_list.items():
            #print(key, value)
            #print(key + ":\t" +value)
            #print('{:15}{}'.format(key, value))
        
        update_def = input("Would you like to update a definition (Y/N)?")
        
        save_file = input("Do you want to save a definition file? Y/N")
        if save_file.upper() == "Y":            
            outfile = open(input("What would you like to call the output file: "), "w")
            print(outfile)
            for key, value in dictionary_list.items():
                line = '{:15}{}'.format(key, value)
                #print(line)
                outfile.write(line)
            outfile.close            
        else:
            break
                    
        #print(fullURL) # debugging code
        wrong_site = False  #  page is found, not wrong file
        
    except HTTPError as e:
        wrong_site = True    # site not found, wrong file 
        #print(e)
        print(fullURL, " not found")
        try_again = input("Do you want to try again or quit? Y/N")
        if try_again.upper() != "Y":
            print("ok, exiting program")
            break
        
