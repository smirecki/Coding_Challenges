//Big numbers 002

var fs = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line !== "") {

        var line0  = "";
        //var line1 = "";
        //var line2 = "";
        //var line3 = "";
        //var line4 = "";
        //var line5 = "";
        //var line6 = "";
        // inputLine = new String(line);

        for (var x in line) {

            if (x === 0) {
                line0 += "zero ";
                line1 += "-**--";
                line2 += "*--*-";
                line3 += "*--*-";
                line4 += "*--*-";
                line5 += "-**--";
                line6 += "-----";
            } else if (x === 1) {
                line0 += "one ";
                line1 += "--*--";
                line2 += "-**--";
                line3 += "--*--";
                line4 += "--*--";
                line5 += "-***-";
                line6 += "-----";
            } else if (x === 2) {
                line0 += "two ";
                line1 += "***--";
                line2 += "---*-";
                line3 += "-**--";
                line4 += "*----";
                line5 += "****-";
                line6 += "-----";
            } else if (x === 3) {
                line0 += "three ";
                line1 += "***--";
                line2 += "---*-";
                line3 += "-**--";
                line4 += "---*-";
                line5 += "***--";
                line6 += "-----";
            } else if (x === 4) {
                line0 += "four ";
                line1 += "-*---";
                line2 += "*--*-";
                line3 += "****-";
                line4 += "---*-";
                line5 += "---*-";
                line6 += "-----";
            } else if (x === 5) {
                line0 += "five ";
                line1 += "****-";
                line2 += "*----";
                line3 += "***--";
                line4 += "---*-";
                line5 += "***--";
                line6 += "-----";
            } else if (x === 6) {
                line0 += "six ";
                line1 += "-**--";
                line2 += "*----";
                line3 += "***--";
                line4 += "*--*-";
                line5 += "-**--";
                line6 += "-----";
            } else if (x === 7) {
                line0 += "seven ";
                line1 += "****-";
                line2 += "---*-";
                line3 += "--*--";
                line4 += "-*---";
                line5 += "-*---";
                line6 += "-----";
            } else if (x === 8) {
                line0 += "eight ";
                line1 += "-**--";
                line2 += "*--*-";
                line3 += "-**--";
                line4 += "*--*-";
                line5 += "-**--";
                line6 += "-----";
            } else if (x === 9) {
                line0 += "nine ";
                line1 += "-**--";
                line2 += "*--*-";
                line3 += "-***-";
                line4 += "---*-";
                line5 += "-**--";
                line6 += "-----";
            } else {}
            console.log(line1);
            //console.log(line1);
            //console.log(line2);
            //console.log(line3);
            //console.log(line4);
            //console.log(line5);
        }
    }
});