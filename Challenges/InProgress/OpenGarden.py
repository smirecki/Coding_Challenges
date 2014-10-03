"""  Open Garden - throw down

The 2010 Census puts populations of 26 largest US metro areas at 18897109, 12828837, 9461105, 6371773, 5965343, 5946800, 5582170, 5564635, 5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279833, 3095313, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508, and 2134411.

Can you find a subset of these areas where a total of exactly 100,000,000 people live, assuming the census estimates are exactly right? Provide the answer and code or reasoning used.
================================================================================

25! = 15,511,210,043,330,985,984,000,000
26! = "The factorial of 26 is 4.03291461 x 10^26. The factorial of 4.03291461 x 10^26 would be an immeasurably huge number."
====
18,897,109
12,828,837
 9,461,105
 6,371,773
 5,965,343
 5,946,800
 5,582,170
 5,564,635
 5,268,860
 4,552,402
 4,335,391
 4,296,250
 4,224,851
 4,192,887
 3,439,809
 3,279,833
 3,095,313
 2,812,896
 2,783,243
 2,710,489
 2,543,482
 2,356,285
 2,226,009
 2,149,127
 2,142,508
 2,134,411.
===
wiki
Subset sum problem -- http://en.wikipedia.org/wiki/Subset_sum_problem



==============some js notes
//input
var numbers = [18897109, 12828837, 9461105, 6371773, 5965343, 5946800, 5582170, 5564635, 5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279833, 3095313, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508, 2134411];
var total = 0;

for(var i = 0; i < numbers.length; ++i){
    total += numbers[i];
    console.log("line " + i + " total: " + total + "   this number = " + numbers[i] + "   This number + 1 =  " + (numbers[i]+1));
};
console.log(total);
//output
line 0 total: 18897109   this number = 18897109   This number + 1 =  18897110 (index):27
line 1 total: 31725946   this number = 12828837   This number + 1 =  12828838 (index):27
line 2 total: 41187051   this number = 9461105   This number + 1 =  9461106 (index):27
line 3 total: 47558824   this number = 6371773   This number + 1 =  6371774 (index):27
line 4 total: 53524167   this number = 5965343   This number + 1 =  5965344 (index):27
line 5 total: 59470967   this number = 5946800   This number + 1 =  5946801 (index):27
line 6 total: 65053137   this number = 5582170   This number + 1 =  5582171 (index):27
line 7 total: 70617772   this number = 5564635   This number + 1 =  5564636 (index):27
line 8 total: 75886632   this number = 5268860   This number + 1 =  5268861 (index):27
line 9 total: 80439034   this number = 4552402   This number + 1 =  4552403 (index):27
line 10 total: 84774425   this number = 4335391   This number + 1 =  4335392 (index):27
line 11 total: 89070675   this number = 4296250   This number + 1 =  4296251 (index):27
line 12 total: 93295526   this number = 4224851   This number + 1 =  4224852 (index):27
line 13 total: 97488413   this number = 4192887   This number + 1 =  4192888 (index):27
line 14 total: 100928222   this number = 3439809   This number + 1 =  3439810 (index):27
line 15 total: 104208055   this number = 3279833   This number + 1 =  3279834 (index):27
line 16 total: 107303368   this number = 3095313   This number + 1 =  3095314 (index):27
line 17 total: 110116264   this number = 2812896   This number + 1 =  2812897 (index):27
line 18 total: 112899507   this number = 2783243   This number + 1 =  2783244 (index):27
line 19 total: 115609996   this number = 2710489   This number + 1 =  2710490 (index):27
line 20 total: 118153478   this number = 2543482   This number + 1 =  2543483 (index):27
line 21 total: 120509763   this number = 2356285   This number + 1 =  2356286 (index):27
line 22 total: 122735772   this number = 2226009   This number + 1 =  2226010 (index):27
line 23 total: 124884899   this number = 2149127   This number + 1 =  2149128 (index):27
line 24 total: 127027407   this number = 2142508   This number + 1 =  2142509 (index):27
line 25 total: 129161818   this number = 2134411   This number + 1 =  2134412 (index):27
129161818 // grand total

=============




"""