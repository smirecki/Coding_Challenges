// Slang Flavor

var counterPunctuation = 0;
var slangItCounter = -1;
var fs  = require("fs");

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {

	if (line !== "") {
		var newLine = "";

		for (var i = 0; i <= line.length -1; i++) {

			if (line[i] === "?" || line[i] === "!" || line[i] === ".") {
				if(counterPunctuation % 2 === 1) {
					newLine += slangIt(counterPunctuation);
					++counterPunctuation;				
				} else {
					newLine +=line[i];
					++counterPunctuation;
				}
			} else {
				newLine += line[i];
			}
		}
		console.log(newLine);
	}

	function slangIt(counterPunctuation) {
		var slangArray = [", yeah!", ", this is crazy, I tell ya.", ", can U believe this?", ", eh?", ", aw yea.", ", yo.", "? No way!", ". Awesome!"];
		++slangItCounter;

		if(slangItCounter >= 8) {
			slangItCounter = 0;
		}

		return(slangArray[slangItCounter]);
	}

});