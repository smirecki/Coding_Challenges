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
# 01 22 22 01/22/22 BJJ AVV
# 11 14 14 25 03 11/14/14/25/03 GVVQI
# 03 13 01 25 13
# 03 14 14 18 19 21 01
# 01 13 - 0,1,1,3/BHHI 0,11,3/BWS 0,1,13/BHV  01/13 BY? ?????
# 24 19 18 21 19 02 17 13
# 06131715070119
 
ZeroBasedCount  01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26

Work flow === COUNT -> ALPHABET -> KEYED ALPHABET -> ALPHABET

Count            0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
keyed_alphabet:" B  H  I  S  O  E  C  R  T  M  G  W  Y  V  A  L  U  Z  D  N  F  J  K  P  Q  X"
Alphabet         A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
keyed_alph...    BHISOECRTMGWYVALUZDNFJKPQX
char_key         BWWLOOZDDNBZNDOOSTVCBNYTSVTCRNGNRPHBT
message =       01 22 22 SPACE 11 14 14 25 03 SPACE 03 13 01 25 13 SPACE 03 14 14 18 19 21 02 
                 
                SPACE 01 13 SPACE 24 19 18 21 19 02 17 13 SPACE 06 13 17 15 07 01 19" (37 VALUES)



message = "012222 1114142503 0313012513 03141418192102 0113 2419182119021713 06131715070119",
keyed_alphabet = "BHISOECRTMGWYVALUZDNFJKPQX"

"ALL PEERS START SEEDING AT MIDNIGHT KTHXBAI" (37 VALUES)

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