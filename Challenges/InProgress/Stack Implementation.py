""" Stack Implementation

------------ Description -------------
Write a program implementing a stack inteface for integers.The interface should have 'push' and 'pop' functions. You will be asked to 'push' a series of integers and then 'pop' and print out every alternate integer.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename containing a series of space delimited integers, one per line. E.g.

1 2 3 4
10 -2 3 4
OUTPUT SAMPLE:

Print to stdout, every alternate integer(space delimited), one per line. E.g.

4 2
4 -2

-------------- INPUT START ---------------------------------
#Sample code to read in test cases:

import sys
test_cases = open(sys.argv[1], 'r')
print "pretest"
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...
    print test
print "post test"

test_cases.close()

--------------INPUT END ------------------------------------
----------------OUTPUT START --------------------------
pretest
-24 -40 96 87 76 -80 63 86 -30 22 12 -57 61 71 3 -17 50 50 -98

-17 4 71 14 -100 -53 89 -27 -25 -39 47

-5 0 -74 13 60 0 35 100 -20 87 58 -53 32 54 -54 -77 -14 -43 94 78 73 8 -27 86 -57 93

30 -68 54 10 -34 40 -18 -5 39 42 -45 -3 -17 -1 58 -82 53 -25 -29 -85 -97 -62 -87 11 5 -35 -19 67 -76 -62 33 10 69 -71 -52

-3 -89 20 45 -43 -63 79 88 16

69 -63 61 8 -75 -24 -50 96 48 -35 59 61 34 -10 15 -32 -65 -48 94 34 64 -95 22 33 -91 29 21 100 -64 54 32 15 -11 54 29 23 -14 -17 -19 -32 100 -42 -83 -70 -32 -15 96 40 -51 -54 27 -41 -2 -77 -54 13 100 93 25 -2 32 -79 -36 100 -75 -51 -85 40 87 -28 -64 -5 -24 -84 -98 28 74 -22 -94 -29 -25 63 -19 -73 -64 -35 -76 -87 55 61 -89 12 40

8 17 84 -57 43 -78 60 -65

-66 44 22 64 17 78 -74 11 -81 -85 37 69 -27 31 16 -31 16 85 -13 -84 23 94 -86 89 -43 47 -10 43 -93 -60 -36 -25 -79 -73 69 -2 -85 -71 71 81 -23 -35 39

4 4 61 68 -46 43 -37 99 85 93 -73 -51 97 69 -94 99 -83 -46 -50 49 -43 57 -32 27 6 55 -54 -96 97 64 13 -98 -21 27 -3 67 -97 49 -12 44 -76 -72 -69 40 28 10 77 -40 50 3 67 15 68 30 -23 83 27 10 66 -1 -67 77 42 24 -39 38 57 -3 54 83 41 -60 -69 -71 23 37 82 -76 65 -79 -25 -62 -17 -51 90 39 81 42 14 -26

-25 56 -82 74 93 -41 17 78 40 -78 -17 -7 33 -59 -18 -59 72 96 -16 59 27 -65 -46 -78 49 59 38 -19 59 37 -77 -70 -88 0 99 -55 -90 -56 27 45 -57 -85 -14 -2 63 16 72 6 -24 63 21 -26 -92 -13 -75 26 72 100 3

-13 81 73 -10 -45 92 -34 -63 -87 44 -76 4 9 -59 -41 -91 -15 15 -51 28 16 -3 5 20 39 93 -51 -21 12 91 -41 31 -79 29 -30 42 71 -66 90 77 -54 67 13 -27 85 -22 20 13 -45 46 79 -17 -7 -71 -91 -63 19 97 5 -50 -100 19 -34 -73 -23 32 17 -83 -95 -32 40 97 94 -65 -49 70 99 -25 -21 34 17 -14 8 -32 -31 88 -69 7

29 -42 -84 58 -18 66 37 -38 -70 -1 -33 -82 -89 -37 -42 -34 94 -34 91 14 -36 -4 45 46 -79 -9 96 64 -33 -65 22 -91 15 -14 -66 3 -1 -85 -73 18 14 68 50 31 96 28 -54 -83 91 -45 61 -93 -80 43 -28 -81 -52 53 -6 51 17 -67 35 -50 -55 -78 -9 -62 -48 29 -19 7 21 -32 -43 -50 4 -42 -19 99 13 -96 62 73 67 17 30 -63 78 68 -74 43 -64

76 26 -15 -42 -44 94 88 45 55 16 -22 -99 -20 16 -86 47 -46 -89 58 45 -80 -89 -97 47 -69 -64 -34 -12 43 -24 11 -63 -78 -57 -60 1 -45 -90 -93 97 -78 -23 -81 -63 31 -94 -12 -28 -33 90 14 -15 -96 -63 8 -76 38 30 29 -94 15 56 79 -26 25 44 -7 22 -62 -36 93 45 56 -8 -17 22 -4 8 -62 -33 -88 -65 76 -79 -93 -24 -16 -12 98 86 100 39 73

-13 35 96 10 44 -37 40 -69 -46 50 77 -8 57 5 -48 -41 -84 81 5 -22 54 -35 -91 -75 -53 17 -74 -35 26 20 -92 -41 -28 -15 53 -76 -71 -36 -15 -44 27 -88 -42 73 93 43 13 -49 -49 99 45 -40 -28 7 -58

62 22 57 54 -68 -53 70 -79 -6 38 -41 -89 -93 61 -1 54 -9 -100 -75 -50 57 -72 -15 -57 -52 69 37 0 19 -5 50 -13 36 82 78 -56 35 -46 -28 98 -94 10 -62 90 91 -3 100 97 -87 -51 37 53 -46

-11 -52 62 69 60 4 -78 -56 -5

49 24 -94 7 0 74 -31 36 -75 -47 -24 -39 31 -13 67 70 -37 66 -26 -81 59 -50 -81 -27 33 34 1 -74 -63 -17 -9 13 71 27 -3 -9 -70 56 49 80 -32 51 -38 -100 78 -73 -90 -11

91 -70 -60 -72 -97 67 -3 -86 19 -94 30 94 -44 -68 28 60 -37 3 -28 90 88 -37 5 -60 -19 31 33 -31 -34 48 -30 80 -8 -49

14 48 -88 -47 -92 99 67 -17 -96 75 51 71 -69

3 -75 53 -13 48 -88 87 -41 -46

10 70 -35 -23 16 -55 44 6 59 -92 16 -26 86 51 -86 64 28 95 6 -63 -42 42

10 -1

37 -90 -19 78 60 24 -87 37 -11 71 -98 -78 -37 14 -75 51 5 -69 94 29 86 -75 63 -93 -10 32 -100 30 -6 39 94 48 65 -14 10 38 96 -8 -38 -69 -81 -93 49 -100 -63 -1 99 41 79 85 -85 89 33 94 -35 65 -17 -47 32 -44 -83 -100 91 90 -79 -11 -20 -42 -27 -17 -81 -43 -42 -35 12 -32 -3 -67 73 -27 83 -28 82 35 -87 -60 -6 -66 4 -60

1 2 3 4

10 20 30 40

-53 -96 -75 -30 -37 -7 100 -82 92 91 49 -59 6 74 -75 -10 11 95 21 43 -73 36 -29 -31 87 59 55 29 -52 -15 98 1 -2 -14 -55 -51 66 38 76 82 42 76 -96 96 -98 38 23 62 10 -7 -39 -75 -90 -73 29 73 51 -38 -59 31 30 -36 -68 23 -60 -46 -59 31 -90 42 15 87 26 -66 74 98 9 48 38 -92 13 29 -64

7 -76 93 -51 45 -26 -68 36 -59 31 -32 -38 59 -49 -4 -78 -32 64 -29 62 26 33 10 -34 -86 -43 21 53 76 -48 57 -65 4 -37 -74

69 -38 -15 -43 100 24 -93 -96 20 86 89 -36 -72 -74 2 -49 -64 -1 -56 -86 -100 18 48 -97 -1 23 -25 9 1 94 90 47 -36 -11 0 -75 28 -92 7 50 -43 76 84 -45 86 -65 75 -60 -21 -87 -16 -22 -61 63 -92 61 24 -38 48 -64 62 -91 -77 1 95 -87 5 -67 -72 5 70 94 -69 -62 -87 91 68 -51 22 1 86 -97 4 -50 -4 29 -24 -84 56 10 -7 31 4 32 92 92 -62 94 -20

-52 -48 69 38 -36 -59 -90 -95 11 81 -100 31 -4 33 15 -31 26 72 42 1 9 -65 -91 83 -36 -12 -72 95 71 -27 -14 7 -21 69 -66 -38 -80 -32 39

-63 -91 -49 -31 23 -10 -27 -61 -83 75 -37 32 -70 -32 7 53 -68 -69 47 5 -37 -41 88 54 -31 -1 -61 95 26 79 22 6 -14 -68 -38 43 83 25 -68 -76 -57 -12 -90 76 -49 19 51 -29 92 -36 12 -49 90 -99 81 -38 58 -37 9 -37 -19 -2 56 76 -47 -62 13 -76 -18 -34 -76 99 88 18 56 35 45 -28 54 -7 -32 4 -11 -8 -13 -50

34 -90 -80 5 100 83 -70 1 64 38 -13 91 56 70 66 -51 -70 -52 -13 14 -100 81 -94 -41 93 -68 -18

-36 36 -66 -51 66 -88 -99 -64 17 47 -78 90 52 -70 -8 63 -38 34 23 90 6 -63 73 34 -98 -70 -15 22 -90 29 43 -90 71 -95 -33 56 64 -5 24 70 47 47 57 14 13 -100 -76 -65 17 -61 -63 79 -60 2 71 -79 76 42 15 99 -90 -65 56 -39 -95 67 -95 -72 94 -46 -17 27 -21 23 54 -33 -54 70 -32 10 63 -98 29 -18 68 44 56 -5 28 -7 5 49

-43 5 -1 -81 -31 60 -7 -38 27 84 57 45 -96 -61 78 51 48 -43 -2 -28 -80 88 -26 -96 -42 -28 93 100 40 -5 -37 -25 -70 68 90 -97 56

19 -74 42 0 -51 -50 51 -95 60 2 -100 40 -3 -90 -68 78 44 35 -11

63 7 73 45 -43 -3 16 97 50 -70 53 -34 60 -78 -71 81 91 -17 -79 20 -43 -67 17 4 -10 20 -50 35 -54 -62 95 -78 34 53 -71 57 -53 -49 78 2 -35

10 100 1 2 5 -9 0

-95 -74 49 -55 44 -73 -10 -89 93 29 19 -100 -41 18 -16 75 -61 -82 -20 57 -23 87 100 -58 -52 -74 85 -18 -40 -28 -58 -64 -13 30 -91 -28 50 57 -85 -69 51 58 15 19

-69 -95 62 89 -42 49 -11 47 3 88 -11 62 31 29 42 -19 -37 99 100 -17 98 -100 34 -6 26 -52 -35 -52 36 -71 7 65 59 67 -72 25 31 33 -83 -20 24 -11 94 66 92 -15 -15 -73 20 48 -71 -22 -19 14 88 34 -75 25 11 -88 68 63 -50 -47

-36 -44 -85 54 -12 -15 -82 81 45 -97 -14 -31 -39 -51 -23 45 73 -6 -43 60 91 -2 -79 15 -83 34 -78 -39 -31 -49 -70 40 27 -79 39 45 8

-47 -52 63 6 -81 70 13 -11 44 35 86 46 -20 -45 -93 30 36 82 8 46 49 78 -75 9 20 52 -55 -14 6 71 93 66 -17 99 -58 -47 -82 31 66 -88 -4 -30 -8 -26 -14 -40 57 23 84 -72 -64 13 98 -34 34 49 -46 -67 -50 -48 -44 43 -66 -39 99

post test
-----------------OUTPUT END -----------------------------


------------------Soultion
""" 
import sys
test_cases = open(sys.argv[1], 'r')		# open file and read test file 
for test in test_cases:					# read one line at a time
    test = test.split( )				# split the string into a list (space as the default delimiter and removing /n newlines)
    test.reverse()						# reverse the order of the list items
    test = test[::2]					# get every other item
    test = ' '.join(test)				# convert the list to a string seperated by ' ' spaces
    print test_cases					# print the computed string
test_cases.close()						# close file