#Decrypt string

test = "BHISOECRTMGWYVALUZDNFJKPQX"
test_dict = {}

for index in range(len(test)):
    test_dict[index] = test[index]  
  
print test_dict
#Executing the program....
$python2.7 main.py
{0: 'B', 1: 'H', 2: 'I', 3: 'S', 4: 'O', 5: 'E', 6: 'C', 7: 'R', 8: 'T', 9: 'M', 10: 'G', 11: 'W', 12: 'Y', 13: 'V', 14: 'A', 15: 'L', 16: 'U', 17: 'Z', 18: 'D', 19: 'N', 20: 'F', 21: 'J', 22: 'K', 23: 'P', 24: 'Q', 25: 'X'}
message = "012222"

for index in range(len(test_dict)):
  if test_dict[index] == 0
    print test_dict[index]

"""
#!/usr/bin/python

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print 'Current fruit :', fruits[index]

print "Good bye!"

message: "012222 1114142503 0313012513 03141418192102 0113 2419182119021713 06131715070119",
# 012222
# 1114142503
# 0313012513
# 03141418192101
# 0113 - 0,1,1,3/BHHI 0,11,3/BWS 0,1,13/BHV ?????
# 2419182119021713
# 06131715070119

keyed_alphabet: "BHISOECRTMGWYVALUZDNFJKPQX"

message = "012222 1114142503 0313012513 03141418192102 0113 2419182119021713 06131715070119",
keyed_alphabet = "BHISOECRTMGWYVALUZDNFJKPQX"

import ast
foo = ast.literal_eval("{'x':1, 'y':2}")
print foo
#{'y': 2, 'x': 1}
"""