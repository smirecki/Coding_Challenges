<?php  

//FizzBuzz - [ http://en.wikipedia.org/wiki/Fizz_buzz ], [ http://rosettacode.org/wiki/FizzBuzz ]

//The input will be a file with multiple lines and three values per line A, B, N,
//which represent the first value to divide by "A", the second to divide by "B" and
//the limit "N".


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
                
                $array = explode(" ",$line);
                
                tester($array[0], $array[1], $array[2]);
        }
        
        function tester($A, $B, $N){
		
	  for($i = 1; $i <= $N; $i++) //FizzBuzz Logic
              if ($A == 0 or $B == 0){
                echo "zero ";
    	        //echo $A . " " . $B;
	    } else if ($i % $A == 0 and $i % $B == 0){
	        echo "FB ";
	    } else if ($i % $A == 0){
	        echo "F ";
	    } else if ($i % $B == 0){
	        echo "B ";
	    } else {
	        echo $i . " ";
	      }
	  echo \n;
	}
?>


