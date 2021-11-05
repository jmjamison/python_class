wrong_file = True

while wrong_file:
    try:
        vocab_file = open(input("Please enter a vocabulary file: "))
        print('Open success!')
        wrong_file = False  #  file is found, not wrong file
    except IOError:
        print('File not found! Please try again.')
        wrong_file = True    # file not found, wrong file