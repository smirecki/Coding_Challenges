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
# 012222 01/22/22 BJJ AVV
# 1114142503 11/14/14/25/03 GVVQI
# 0313012513
# 03141418192101
# 0113 - 0,1,1,3/BHHI 0,11,3/BWS 0,1,13/BHV  01/13 BY? ?????
# 2419182119021713
# 06131715070119

keyed_alphabet:"BHISO ECRTM GWYVA LUZDN FJKPQ X"
                ABCDE FGHIJ KLMNO PQRST UVWXY Z 
message = "012222 1114142503 0313012513 03141418192102 0113 2419182119021713 06131715070119",
keyed_alphabet = "BHISOECRTMGWYVALUZDNFJKPQX"

"ALL PEERS START SEEDING AT MIDNIGHT KTHXBAI"

import ast
foo = ast.literal_eval("{'x':1, 'y':2}")
print foo
#{'y': 2, 'x': 1}


"Decoded via - http://rumkin.com/tools/cipher/numbers.php
01,02,..."AVV KNNYC CMAYM CNNRSUB AM XSRUSBQM FMQOGAS" # Letter to numbers


#JS Example----------------------

// make the message
var msg = '012222 1114142503 0313012513 03141418192102 0113 2419182119021713 06131715070119';
 
// make an alphabet lookup
var chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
 
// make the key lookup
var key   = 'BHISOECRTMGWYVALUZDNFJKPQX';
 
var value_key = 0;
var char_decrypt = '';
var char_key = '';
 
var decrypted_string = '';
 
// parse out the message into an array of vars
for (var i=0;i<msg.length;i=i+2) {
    if(msg.charAt(i) != ' ') {
        char_key = chars.substr(parseInt(msg.substr(i,2)),1);
        value_key = key.indexOf(char_key);
        char_decrypt = chars.substr(value_key,1);
        decrypted_string = decrypted_string + char_decrypt;
    } else {
        decrypted_string = decrypted_string + ' ';
        i--;
    }
}
 
console.log(decrypted_string);

#-----------------------------

"""