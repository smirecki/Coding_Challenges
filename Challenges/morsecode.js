//morse code
var fs  = require("fs");

function show_props(obj, moresC, objName) {
    result = "";

    for (var prop in obj) {
        if(moresC == obj[prop] ){
            result = prop;
        }
    }
    return result;
    }



fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line !== "") {
        ///////////////////////////////
        var code = {
            A: '.-',    B: '-...',  C: '-.-.',  D: '-..',   E: '.',     F: '..-.',
            G: '--.',   H: '....',  I: '..',    J: '.---',  K: '-.-',   L: '.-..',
            M: '--',    N: '-.',    O: '---',   P: '.--.',  Q: '--.-',  R: '.-.',
            S: '...',   T: '-',     U: '..-',   V: '...-',  W: '.--',   X: '-..-',
            Y: '-.--',  Z: '--..',  0: '-----', 1: '.----', 2: '..---', 3: '...--',
            4: '....-', 5: '.....', 6: '-....', 7: '--...', 8: '---..', 9: '----.'
        };
        
        line = line.split(" ");
        
        var output = "";
        
        for(var i = 0 ; i <= line.length; i++){
            if(line[i] !== ""){
                show_props(code, line[i], "o");
                output = output + result;
            }else{
                output = output + " ";
            }
        }

    console.log(output);
        //////////////////////////////
    }
});

