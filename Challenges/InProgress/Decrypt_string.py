#Decrypt string

test = "BHISOECRTMGWYVALUZDNFJKPQX"
test_dict = {}

for index in range(len(test)):
    test_dict[index] = test[index]  
  
print test_dict
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
keyed_alphabet: "BHISOECRTMGWYVALUZDNFJKPQX"

message = "012222 1114142503 0313012513 03141418192102 0113 2419182119021713 06131715070119",
keyed_alphabet = "BHISOECRTMGWYVALUZDNFJKPQX"

import ast
foo = ast.literal_eval("{'x':1, 'y':2}")
print foo
#{'y': 2, 'x': 1}
"""