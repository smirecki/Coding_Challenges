<?php
$file_data = file_get_contents($argv[1]);
        // File Data "Sanitation"
        $file_data = str_replace("\r\n","\n",$file_data);
        $file_data = str_replace("\r","\n",$file_data);
        // Make each line in the file an array.
        $file_data = explode("\n",$file_data);
        foreach($file_data as $line)
        { // For Each Line
                $line = trim($line);
                if($line == "") continue; // Continue the loop if the line is blank.
        
                $line = explode(";",$line);
                $intString = array();
        
		foreach($line as $value){
    			array_push($intString, charToInt($value));
		};

                $intString = implode($intString);        
                print $intString . "\n";
        };
        
        function charToInt ($value){
            if($value == "zero"){
                $value = 0;
            }elseif($value == "one"){
                $value = 1;
            }elseif($value == "two"){
                $value = 2;
            }elseif($value == "three"){
                $value = 3;
            }elseif($value == "four"){
                $value = 4;
            }elseif($value == "five"){
                $value = 5;
            }elseif($value == "six"){
                $value = 6;
            }elseif($value == "seven"){
                $value = 7;
            }elseif($value == "eight"){
                $value = 8;
            }elseif($value == "nine"){
                $value = 9;
            }else{
                $value = "";
            };
            
            return $value;
        };
   
?>

