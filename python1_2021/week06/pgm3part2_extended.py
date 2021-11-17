# week 36 python 1 class
'''
Name: Jina (Jamie) Jamison
Date: 2021-11-07
Description:  program 3 part 2

Program 3 part 2
1) create a dictionary from a vocabulary list
2) if the user enters a file name that does not exist, catch the error and re-prompt 
      for the correct file name
3) read in existing dictionary file
4) term is the key; definition is the value
5) ask user if they would like to add additional terms and definitions,
6) and how many if Y is the response
7) if a duplicate term is entered notify the user and ask if the users would like to 
        update the definition  BEFORE asking for the definition
8) end by printing the list of terms and definitions before asking the user for a 
        file name to save the new dictionary. **DO NOTE write over the original 
        unless enterd by the user.
9) save as text (txt) file, tap separated
Extended:
10) ask Y or N about writing out a new file
11) delete a term from the dictionary file

'''
'''
first prompt for an input vocabulary file
'''
wrong_file = True

while wrong_file:
    try:
        vocab_file = open(input("Please enter a vocabulary file: "))
        wrong_file = False  #  file is found, not wrong file
    except IOError:
        print('File not found! Please try again.')
        wrong_file = True    # file not found, wrong file


'''
read in the tile to my_dictionary
'''
my_dictionary = {}
for line in vocab_file:
    key, value = line.split('\t')    
    my_dictionary[key] = value
    
vocab_file.close()

'''
List out how many terms are currently in the dictionary and
prompt to see if the user wants to delete a term
'''
print("There are {} terms in this vocabulary list: ".format(len(my_dictionary)))
for key, value in my_dictionary.items():
    print('{:10} - {}'.format(key, value))

answer = "Y"
while answer == "Y":
    answer = input("Would you like to delete an item Y/N: ").upper()
    #print(answer)
    if answer != "Y":
        #print(answer)
        break
    
    term_to_delete = input("What term would you like to delete from the dictionary: ")
    if term_to_delete in my_dictionary.keys():
        my_dictionary.pop(term_to_delete)
        print(term_to_delete, " deleted from the dictionary.")
    else:
        print(term_to_delete, " is not in the dictionary.")
                        

'''
List out how many terms are currently in the dictionary
'''
print("There are {} terms in this vocabulary list: ".format(len(my_dictionary)))


'''
Main body of program
Ask user if they would like to add additional terms and definitions,
If Y(es) is the response, then how many
If a duplicate term is entered notify the user and ask if the users would like to 
        update the definition  BEFORE asking for the definition
If no duplicates or updates of existing terms, then add the new term
Finally print the list of terms and definitions         
'''
answer = "Y"
while answer == "Y":
    answer = input("Would you like to add more items Y/N: ").upper()
    #print(answer)
    if answer != "Y":
        #print(answer)
        break
   
    # typo, user enters alpha character - which I did at least once
    not_int = True
    while not_int:
        try:
            new_terms_num = int(input("How many new terms would you like to add? "))
            not_int = False
        except ValueError:
            print('Please enter a positive integer!')
            not_int = True
            
            
    # this may be horrible codeing but I couldn't come up with a better way to test for negative numbers       
    if new_terms_num < 0:
        print('Please enter a positive integer!')
        new_terms_num = int(input("How many new terms would you like to add? "))
            
        
    # prompt for a new term    
    
    for new_terms in range(0,new_terms_num):
        input_term = input("Term: ")
        #print(input_term)
        input_definition = input("Definition: ") + "\n"
        #print(input_definition)
        new_entry = {input_term: input_definition}
        #print(new_entry)
        
        # if the term is alreay in the dictionary ask the user if they want to update or enter a new term/value
        if input_term in my_dictionary.keys():
            print(input_term, " already in dictionary. ")
            add_answer = input("Do you want to update or make a new key? Answer update or new: ")  
            #print(add_answer)
            if add_answer == "update":
                print(add_answer, "updating existing ", input_term)
                my_dictionary.update(new_entry)
            elif add_answer == "new":
                input_term = input("Term: ") 
                #print(input_term)
                input_definition = input("Definition: ") + "\n"
                #print(input_definition)
                new_entry = {input_term: input_definition}
                #print(new_entry)
                default_dict.update(new_entry)
                #print(default_dict)
        else:
            # not in the dictionary
            my_dictionary.update(new_entry)
            
        new_terms_num += 1

    
print("all done")


    
'''
Prompt for an output filename
Don't write over the original file unless entered by the user
'''
for key, value in my_dictionary.items():
    #print(key, value)
    #print(key + ":\t" +value)
    print('{:10} - {}'.format(key, value))
    
''' 
Prompt the user to see if they want to print an output file or not
'''
answer = "Y"
#print("Answer starts as: ", answer)
while answer == "Y":
    answer = input("Do you want to save an output file? Y/N: ").upper()
    print("First answer: ", answer)
    if answer != "Y":
        #print("Answer not Y: ", answer)
        break
    
    else:   
        try:
            outfile = open(input("Enter a file name: "), "w")
            #print("File name: ", outfile)  
            for key, value in my_dictionary.items():
                line = key + "\t" + value
                #print(line)
                outfile.write(line)
                            
            outfile.close() 
            break # done
                    
                        
    
        except IOError:
            print("File not accessible")
            
            
            
print("Done")

                  
    
            