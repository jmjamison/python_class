my_dictionary = {}

wrong_file = True

while wrong_file:
    try:
        vocab_file = open(input("Please enter a vocabulary file: "))
        print('Open success!')
        wrong_file = False  #  file is found, not wrong file
    except IOError:
        print('File not found! Please try again.')
        wrong_file = True    # file not found, wrong file
        
        
for line in vocab_file:
    key, value = line.split('\t')    
    my_dictionary[key] = value
    
#print(my_dictionary)
my_dictionary = {}
for line in vocab_file:
    key, value = line.split('\t')    
    my_dictionary[key] = value

    for key, value in my_dictionary.items():
        #print(key, value)
        #print(key + ":\t" +value)
        print('{:10} - {}'.format(key, value))