//OverLappingRectangles in JavaScript
var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line !== "") {
      line = line.split(",");

            x1 = Number(line[0]),
		    y1 = Number(line[1]),
		    x2 = Number(line[2]),
		    y2 = Number(line[3]),
		    x3 = Number(line[4]),
		    y3 = Number(line[5]),
		    x4 = Number(line[6]),
		    y4 = Number(line[7]);
             
	    if ((y3>y1 && y3>y2 && y4>y1 && y4>y2) || (y3<y1 && y3<y2 && y4<y1 && y4<y2) || (x3>x1 && x3>x2 && x4>x1 && x4>x2) || (x3<x1 && x3<x2 && x4<x1 && x4<x2)){
		    console.log("False"); //Above - Below - Right - Left 
	    } else {
		    console.log("True"); //Overlapping
        }      
    }
});

