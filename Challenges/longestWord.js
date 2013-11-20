//longest word

var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line !== "") {
        var greatestElement = "";

        line = line.split(" ");

        for(var i=0; i<= line.length -1; i++){
         
            if(line[i].length > greatestElement.length){
                greatestElement = line[i];
            }
       
        }
        console.log(greatestElement);
    }
});

