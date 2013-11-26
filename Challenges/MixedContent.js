//Mixed Content
// goal output "melon,apricot,peach,pineapple|8,33,21,0,16,50,37,0,7,17"
// line_input = "8,33,21,0,16,50,37,0,melon,7,apricot,peach,pineapple,17,21";

var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line !== "") {
        var lineDigits = new Array();
        var lineWords = new Array();

        line = line.split(",");
    
        for(var i = 0; i <= line.length -1; i++){
            var reDigit = new RegExp("\\d");
            if (reDigit.test(line[i])){
                lineDigits.push(line[i]);
            } else{
                lineWords.push(line[i]);
            }
        }

    lineDigits = lineDigits.toString();
    lineWords = lineWords.toString();
    var pipe = "|";
    var solution = "";

        if(lineDigits.length === 0){
            solution = lineWords;
        }else if (lineWords.length === 0){
            solution = lineDigits;
        }else{
            solution = lineWords.concat(pipe);
            solution = solution.concat(lineDigits);
        }

    console.log(solution);
    }
});
;

