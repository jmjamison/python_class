#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
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
9) text (txt) file, tap separated
'''


# In[3]:



# read-only is the default but set to be careful
#vocab_file = open(input("Please enter a vocabulary file: "), "r+")

wrong_file = True

while wrong_file:
    try:
        vocab_file = open(input("Please enter a vocabulary file: "))
        print('Open success!')
        wrong_file = False  #  file is found, not wrong file
    except IOError:
        print('File not found! Please try again.')
        wrong_file = True    # file not found, wrong file


# In[5]:


my_dictionary = {}
for line in vocab_file:
    key, value = line.split('\t')    
    my_dictionary[key] = value


# In[6]:


print(my_dictionary)


# In[7]:


for key, value in my_dictionary.items():
    #print(key, value)
    #print(key + ":\t" +value)
    print('{:10} - {}'.format(key, value))


# In[8]:


print("There are {} terms in this vocabulary list: ".format(len(my_dictionary)))


# In[9]:


# my_dictionary.items()


# In[10]:


'''
Other dictionary methods
clear()	    Removes all the elements from the dictionary
copy()	    Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and values
get()	    Returns the value of the specified key
items()	    Returns a list containing a tuple for each key value pair
keys()	    Returns a list containing the dictionary's keys
pop()	    Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''


# In[11]:


new_key = 'IDLE'
new_value = "Integrated development environment"
my_dictionary[new_key]=new_value


# In[ ]:


my_dictionary.items()


# In[12]:


answer = "Y"
while answer.capitalize() == "Y":
    answer = input("Do you want to add more items Y/N: ")
    answer.capitalize
    print(answer)
print("all done")


# In[ ]:





# In[ ]:




