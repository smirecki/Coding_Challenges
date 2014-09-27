// Codeval - BIG DIGITS
/*
CHALLENGE DESCRIPTION:

Sometimes, there is a need to output big symbols on the devices, which support only ASCII characters and single fixed-width fonts. The only way to do this is to use the pseudographics for drawing big symbols.

Here is an example of the font with digits from 0 to 9:


1 -**----*--***--***---*---****--**--****--**---**--
2 *--*--**-----*----*-*--*-*----*-------*-*--*-*--*-
3 *--*---*---**---**--****-***--***----*---**---***-
4 *--*---*--*-------*----*----*-*--*--*---*--*----*-
5 -**---***-****-***-----*-***---**---*----**---**--
6 --------------------------------------------------
Each pixel is marked either with asterisk ‘*’ or with minus ‘-’. Size of a digit is 5×6 pixels.

Your task is to write a program, which outputs the numbers given to you with the font as in the example.

INPUT SAMPLE:

The first argument is a file that contains the lines with digits sequences you need to magnify. E.g.:


1 3.1415926
2 1.41421356
3 01-01-1970
4 2.7182818284
5 4 8 15 16 23 42

OUTPUT SAMPLE:

Print to stdout the magnified digits:


1  ***----*---*-----*--****--**--***---**--
2  ---*--**--*--*--**--*----*--*----*-*----
3  -**----*--****---*--***---***--**--***--
4  ---*---*-----*---*-----*----*-*----*--*-
5  ***---***----*--***-***---**--****--**--
6  ----------------------------------------
7  --*---*-----*---*---***----*--***--****--**--
8  -**--*--*--**--*--*----*--**-----*-*----*----
9  --*--****---*--****--**----*---**--***--***--
10 --*-----*---*-----*-*------*-----*----*-*--*-
11 -***----*--***----*-****--***-***--***---**--
12 ---------------------------------------------
13 -**----*---**----*----*---**--****--**--
14 *--*--**--*--*--**---**--*--*----*-*--*-
15 *--*---*--*--*---*----*---***---*--*--*-
16 *--*---*--*--*---*----*-----*--*---*--*-
17 -**---***--**---***--***--**---*----**--
18 ----------------------------------------
19 ***--****---*---**--***---**----*---**--***---**---*---
20 ---*----*--**--*--*----*-*--*--**--*--*----*-*--*-*--*-
21 -**----*----*---**---**---**----*---**---**---**--****-
22 *-----*-----*--*--*-*----*--*---*--*--*-*----*--*----*-
23 ****--*----***--**--****--**---***--**--****--**-----*-
24 -------------------------------------------------------
25 -*----**----*--****---*---**--***--***---*---***--
26 *--*-*--*--**--*-----**--*-------*----*-*--*----*-
27 ****--**----*--***----*--***---**---**--****--**--
28 ---*-*--*---*-----*---*--*--*-*-------*----*-*----
29 ---*--**---***-***---***--**--****-***-----*-****-
30 --------------------------------------------------

CONSTRAINTS:

Input lines are up to 16 symbols long.
Input can contain some other symbols, which should be ignored (i.e. points, hyphens, spaces); only numbers must be printed out.
//

	       3       1      4      5       9       2     6      8     9      7
          abcde  abcde  abcde  abcde  abcde  abcde  abcde  abcde  abcde  abcde
          12345  12345  12345  12345  12345  12345  12345  12345  12345  12345
1  -**--  ***--  --*--  -*---  ****-  -**--  ***--  -**--  -**--  -**--  ****-
2  *--*-  ---*-  -**--  *--*-  *----  *--*-  ---*-  *----  *--*-  *--*-  ---*-
3  *--*-  -**--  --*--  ****-  ***--  -***-  -**--  ***--  -**--  -***-  --*--
4  *--*-  ---*-  --*--  ---*-  ---*-  ---*-  *----  *--*-  *--*-  ---*-  -*---
5  -**--  ***--  -***-  ---*-  ***--  -**--  ****-  -**--  -**--  -**--  -*---
6  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----

   0  -**-- *--*- *--*- *--*- -**--  
   1  --*-- -**-- --*-- --*-- -***-
   2  ***-- ---*- -**-- *---- ****-
   3  ***-- ---*- -**-- ---*- ***--
   4  -*--- *--*- ****- ---*- ---*-
   5  ****- *---- ***-- ---*- ***--
   6  -**-- *---- ***-- *--*- -**--
   7  ****- ---*- --*-- -*--- -*---
   8  -**-- *--*- -**-- *--*- -**--
   9  -**-- *--*- -***- ---*- -**--

line1 
	1, 4
	same (2 & 3 ), (5 & 7), (6, 8, & 9)
line2
	1
	same (2,3,7) (4,8,9) (5,6)
line3
	4,9
	same (2,3,8) (1,7) (5,6)
line4
	1,2,6,7,8
	same (3,4,5,9)
line5 
	1,2,4,7
	same (3,5)(6,8,9)
line6 = "-----"


if (x == 0) {
	line1 += "-**--";
	line2 += "*--*-";
	line3 += "*--*-";
	line4 += "*--*-";
	line5 += "-**--";
} else if (x == 1) {
	line1 += "--*--";
	line2 += "-**--";
	line3 += "--*--";
	line4 += "--*--";
	line5 += "-***-";
} else if (x == 2) {
	line1 += "***--";
	line2 += "---*-";
	line3 += "-**--";
	line4 += "*----";
	line5 += "****-";
} else if (x == 3) {
	line1 += "***--";
	line2 += "---*-";
	line3 += "-**--";
	line4 += "---*-";
	line5 += "***--";
} else if (x == 4) {
	line1 += "-*---";
	line2 += "*--*-";
	line3 += "****-";
	line4 += "---*-";
	line5 += "---*-";
} else if (x == 5) {
	line1 += "****-";
	line2 += "*----";
	line3 += "***--";
	line4 += "---*-";
	line5 += "***--";
} else if (x == 6) {
	line1 += "-**--";
	line2 += "*----";
	line3 += "***--";
	line4 += "*--*-";
	line5 += "-**--";
} else if (x == 7) {
	line1 += "****-";
	line2 += "---*-";
	line3 += "--*--";
	line4 += "-*---";
	line5 += "-*---";
} else if (x == 8) {
	line1 += "-**--";
	line2 += "*--*-";
	line3 += "-**--";
	line4 += "*--*-";
	line5 += "-**--";
} else if (x == 9) {
	line1 += "-**--";
	line2 += "*--*-";
	line3 += "-***-";
	line4 += "---*-";
	line5 += "-**--";
} else {
	continue;
};



7  --*---*-----*---*---***----*--***--****--**--
8  -**--*--*--**--*--*----*--**-----*-*----*----
9  --*--****---*--****--**----*---**--***--***--
10 --*-----*---*-----*-*------*-----*----*-*--*-
11 -***----*--***----*-****--***-***--***---**--
12 ---------------------------------------------
13 -**----*---**----*----*---**--****--**--
14 *--*--**--*--*--**---**--*--*----*-*--*-
15 *--*---*--*--*---*----*---***---*--*--*-
16 *--*---*--*--*---*----*-----*--*---*--*-
17 -**---***--**---***--***--**---*----**--
18 ----------------------------------------
19 ***--****---*---**--***---**----*---**--***--  -**--  -*---
20 ---*----*--**--*--*----*-*--*--**--*--*----*-  *--*-  *--*-
21 -**----*----*---**---**---**----*---**---**--  -**--  ****-
22 *-----*-----*--*--*-*----*--*---*--*--*-*----  *--*-  ---*-
23 ****--*----***--**--****--**---***--**--****-  -**--  ---*-
24 --------------------------------------------------  -----
25 -*----**----*--****---*---**--***--***---*---***--
26 *--*-*--*--**--*-----**--*-------*----*-*--*----*-
27 ****--**----*--***----*--***---**---**--****--**--
28 ---*-*--*---*-----*---*--*--*-*-------*----*-*----
29 ---*--**---***-***---***--**--****-***-----*-****-
30 --------------------------------------------------


*/
