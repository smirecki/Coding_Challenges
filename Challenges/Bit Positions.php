<?php
//Bit Positions
// Given a number n and two integers p1,p2 determine if the bits in position p1 and p2 are the same or not. Positions p1 and p2 and 1 based.
//
$file_data = file_get_contents($argv[1]);
        // File Data "Sanitation"
        $file_data = str_replace("\r\n","\n",$file_data);
        $file_data = str_replace("\r","\n",$file_data);
        // Make each line in the file an array.
        $file_data = explode("\n",$file_data);
    
	foreach($file_data as $line){
        $line = trim($line);
        if($line == "") continue;

		$line = explode(",", $line);
		$line[0] = base_convert($line[0], 10, 2);
		$baseTwoValue = str_split($line[0]);
		$baseTwoValue = array_reverse($baseTwoValue);
	
			if($baseTwoValue[$line[1]-1] == $baseTwoValue[$line[2]-1]){
				print "true" . "\n";
				}else{
				print "false" . "\n";
			};
	};
?>

