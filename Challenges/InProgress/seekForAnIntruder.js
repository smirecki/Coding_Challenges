// Codeeval - SEEK FOR AN INTRUDER

var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line !== "") {

        var regexp = "\B(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\B"


         if (line.match(regexp)) { 
           	console.log(match);
         }
    }
});

=====================

// http://jsfiddle.net/bvyt4qst/
// http://jsfiddle.net/7q00dmuu/

var line = new String('255.255.255.255 ladkfja;oiavkn ');

var re = /\B(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\B/;

var re2 = /d(b+)(d)/ig;

var m = re.exec(line);

if (m === null) {
    alert("No match");
} else {
    var s = "Match at position " + m.index + ":\n";
    for (i = 0; i < m.length; i++) {
        s = s + m[i] + "\n";
    }
    console.log(s);
    alert(s);
}