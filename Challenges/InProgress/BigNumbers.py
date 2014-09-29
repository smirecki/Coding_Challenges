#Codeval - Big Numbers
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	# 'test' represents the test case, do something with it
	line1 = ""
	line2 = ""
	line3 = ""
	line4 = ""
	line5 = ""
	line6 = ""


	#Can "for in" iterate over a String like this or should a definite loop be used?
	for element in test:
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

	print line1, line2, line3, line4, line5, line6


test_cases.close()
