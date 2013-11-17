//Sudoku
//CodEval version

var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line !== "") {
       var gridSize = 0,
           allValues = 0,
           i = 0,
           totalSum = 0;
        
        line = line.split(";");
        gridSize = line[0];
        allValues = line[1];
        allValues = allValues.split(",");
    
        for (i = 0; i <= allValues.length -1; i++) {
            totalSum = totalSum + Number(allValues[i]);
        }
        
        if (gridSize == 4 && totalSum == 40 || gridSize == 9 && totalSum == 405) {
            console.log("True") ;
        } else {
            console.log("False");
        }          
    }
});
