#Codeval - Big Numbers

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	# 'test' represents the test case
	line1 = ""
	line2 = ""
	line3 = ""
	line4 = ""
	line5 = ""
	line6 = ""
	for element in test:
	# building Big Number output
		if element == "0":
			line1 += "-**--"
			line2 += "*--*-"
			line3 += "*--*-"
			line4 += "*--*-"
			line5 += "-**--"
			line6 += "-----"
		elif element == "1":
			line1 += "--*--"
			line2 += "-**--"
			line3 += "--*--"
			line4 += "--*--"
			line5 += "-***-"
			line6 += "-----"
		elif element == "2":
			line1 += "***--"
			line2 += "---*-"
			line3 += "-**--"
			line4 += "*----"
			line5 += "****-"
			line6 += "-----"
		elif element == "3":   	
			line1 += "***--"
			line2 += "---*-"
			line3 += "-**--"
			line4 += "---*-"
			line5 += "***--"
			line6 += "-----"
		elif element == "4":    	
			line1 += "-*---"
			line2 += "*--*-"
			line3 += "****-"
			line4 += "---*-"
			line5 += "---*-"
			line6 += "-----"
		elif element == "5":    	
			line1 += "****-"
			line2 += "*----"
			line3 += "***--"
			line4 += "---*-"
			line5 += "***--"
			line6 += "-----"
		elif element == "6":    	
			line1 += "-**--"
			line2 += "*----"
			line3 += "***--"
			line4 += "*--*-"
			line5 += "-**--"
			line6 += "-----"
		elif element == "7":    	
			line1 += "****-"
			line2 += "---*-"
			line3 += "--*--"
			line4 += "-*---"
			line5 += "-*---"
			line6 += "-----"
		elif element == "8":    	
			line1 += "-**--"
			line2 += "*--*-"
			line3 += "-**--"
			line4 += "*--*-"
			line5 += "-**--"
			line6 += "-----"
		elif element == "9":
			line1 += "-**--"
			line2 += "*--*-"
			line3 += "-***-"
			line4 += "---*-"
			line5 += "-**--"
			line6 += "-----"
		else:
			line1 += ""
			line2 += ""
			line3 += ""
			line4 += ""
			line5 += ""
			line6 += ""

	print line1 + '\n', line2 + '\n', line3 + '\n', line4 + '\n', line5 + '\n', line6

test_cases.close()
