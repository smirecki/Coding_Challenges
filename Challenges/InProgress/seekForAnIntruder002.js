var line = new String(' hjgkg 255.255.255.255 k ladkfja;oiavkn ');

var re = /\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/;

var m = re.exec(line);

if (m === null) {
    alert("No match");
} else {
    var s = "Match at position " + m.index + ":\n";
    for (i = 0; i < m.length; i++) {
        s = s + m[i] + "\n";
    }
    console.log(s);
    //alert(s);
}

// ====================================================================
var line = "334343'dfasdf";

/*
var re = /apples/gi;
var str = "Apples are round, and apples are juicy.";
var newstr = str.replace(re, "oranges");
print(newstr);
*/

var re = /'/gi;
var str = "334343'dfasd";
var newstr = str.replace(re, "@");
//console.log(newstr);

// ============================================

    var str = new String ("3w:b21f[rsnj^Rgg[t!(<5vIup^&]o@489.229.130.225gw4\SwBEbN222.137.104.206[Jo<)lj36bB.034062405073xx37d;~wKi/DIAeVfeBO55");
    
    
    
    var patt = new RegExp(/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/);
    var res = patt.exec(str);
    document.getElementById("demo").innerHTML = res;
console.log(res[0]);