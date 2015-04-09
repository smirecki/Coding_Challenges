// Functions
// A collection of functions with testing values removed

//Notes: changed null value output to "null"


//////// Custom Sort 
// input array ["XY","XY","XY","XY","XY"]
// output array - same as about, but in order 2-A

function cardsSorter(arr) { 
    var result = [];
    var cardOrder = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"];
    
    for (var j = 0; j < cardOrder.length; ++j) {
        for (var i = 0; i < arr.length; ++i) {
            if (arr[i][0] == cardOrder[j]) {
                result.push(arr[i]);
            }
        }
    }
    return result;
}


/////////// Duplicates Checker
// input array ["XY","XY","XY","XY","XY"]
// output array ["type or null", Array[result]]

function duplicateChecker(arr) {
    var results = [];
    var duplicateArr = [];
    for (var i = 0; i < arr.length - 1; i++) {
        if ((arr[i][0]) == (arr[i + 1][0])) {
            results.push(arr[i][0]);
        }
    }

    if (results.length === 0) { // No duplicates
        duplicateArr.push("null");
        duplicateArr.push(results);
    } else if (results.length == 1) { // One Pair
        duplicateArr.push("Pair");
        duplicateArr.push(results);
    } else if (results.length == 2 && results[0] == results[1]) { // Three of a kind
        duplicateArr.push("Three of a Kind");
        duplicateArr.push(results);
    } else if (results.length == 3 && results[0] == results[1] && results[0] == results[2]) { // Four of a kind
        duplicateArr.push("Four of a Kind");
        duplicateArr.push(results);
    } else if (results.length == 2 && results[0] != results[1]) { // Two Pairs
        duplicateArr.push("Two Pairs");
        duplicateArr.push(results);
    } else if (results.length == 3 && results[0] != results[2]) { // One Pairs & Three - Full House
        duplicateArr.push("Full House");
        duplicateArr.push(results);  
    }
    return duplicateArr.length > 0 ? duplicateArr : "null";
}


//////////// Flush Checker 
// input array ["XY","XY","XY","XY","XY"]
// output array "Flush" or "null"

function flushChecker(arr) {
    var suits = ["C", "D", "H", "S"];
    var flushCards = -4;

    for (var j = 0; j < suits.length; ++j) {
         if (flushCards == 1) {
             break;
         }
        flushCards = -4;
        for (var i = 0; i < arr.length; ++i) {
            if (arr[i][1] == suits[j]) {
                ++flushCards;
            }
        }
    }
    return flushCards === 1 ? "Flush" : "null";
}


/////////// Straight Checker
// input array ["XY","XY","XY","XY","XY"]
// output array ["Straight, Straight Royal or null" , "highest card if straight"]

function straightChecker(arr) {
    var straight = -3;
	var s = ["23456", "34567", "45678", "56789", "6789T", "789TJ", "89TJQ", "9TJQK", "TJQKA"];
	var straightArr = [];

    for (var i = 0; i < s.length; i++) {
        if ((arr[0][0]) == (s[i][0])) {
            for (var j = 1; j < 5; j++) {
                if (s[i][j] == arr[j][0]) {
                    straight++;
                }
            }
        }
    }

    if (straight != 1) {
        straightArr.push("null");
    } else if (arr[4][0] == "A") {
        straightArr.push("Straight Royal");
        straightArr.push(arr[4][0]);
    } else {
        straightArr.push("Straight");
        straightArr.push(arr[4][0]);
    }
    return straightArr;
}



