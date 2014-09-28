var fs = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line !== "") {

        var line1 = "";
        var line2 = "";
        var line3 = "";
        var line4 = "";
        var line5 = "";
        var line6 = "";
        
        for (var i = 0; i <= line.length ; ++i) {
            if (line[i] === "0") {
                line1 += "-**--";
                line2 += "*--*-";
                line3 += "*--*-";
                line4 += "*--*-";
                line5 += "-**--";
                line6 += "-----";
            } else if (line[i] == "1") {
                line1 += "--*--";
                line2 += "-**--";
                line3 += "--*--";
                line4 += "--*--";
                line5 += "-***-";
                line6 += "-----";
            } else if (line[i] == "2") {
                line1 += "***--";
                line2 += "---*-";
                line3 += "-**--";
                line4 += "*----";
                line5 += "****-";
                line6 += "-----";
            } else if (line[i] == "3") {
                line1 += "***--";
                line2 += "---*-";
                line3 += "-**--";
                line4 += "---*-";
                line5 += "***--";
                line6 += "-----";
            } else if (line[i] == "4") {
                line1 += "-*---";
                line2 += "*--*-";
                line3 += "****-";
                line4 += "---*-";
                line5 += "---*-";
                line6 += "-----";
            } else if (line[i] == "5") {
                line1 += "****-";
                line2 += "*----";
                line3 += "***--";
                line4 += "---*-";
                line5 += "***--";
                line6 += "-----";
            } else if (line[i] == "6") {
                line1 += "-**--";
                line2 += "*----";
                line3 += "***--";
                line4 += "*--*-";
                line5 += "-**--";
                line6 += "-----";
            } else if (line[i] == "7") {
                line1 += "****-";
                line2 += "---*-";
                line3 += "--*--";
                line4 += "-*---";
                line5 += "-*---";
                line6 += "-----";
            } else if (line[i] == "8") {
                line1 += "-**--";
                line2 += "*--*-";
                line3 += "-**--";
                line4 += "*--*-";
                line5 += "-**--";
                line6 += "-----";
            } else if (line[i] == "9") {
                line1 += "-**--";
                line2 += "*--*-";
                line3 += "-***-";
                line4 += "---*-";
                line5 += "-**--";
                line6 += "-----";
            } else {
                
            }
        }
        console.log(line1);
        console.log(line2);
        console.log(line3);
        console.log(line4);
        console.log(line5);
        console.log(line6);
    }
});