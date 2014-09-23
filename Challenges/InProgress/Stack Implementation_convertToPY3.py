import sys
test_cases = open(sys.argv[1], 'r')		# open file and read test file 
for test in test_cases:					# read one line at a time
    test = test.split( )				# split the string into a list (space as the default delimiter and removing /n newlines)
    test.reverse()						# reverse the order of the list items
    test = test[::2]					# get every other item
    test = ' '.join(test)				# convert the list to a string seperated by ' ' spaces
    #print test_cases					# print the computed string
    print(test_cases)
test_cases.close()						# close file