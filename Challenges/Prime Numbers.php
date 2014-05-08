<?php

    $file_data = file_get_contents($argv[1]);
    $file_data = explode("\n",$file_data);
    
    foreach($file_data as $line){ // For Each Line
        $line = trim($line);
        if($line == "") continue;
                
        iprimes_upto($line);
    };
    function iprimes_upto($limit){
        for ($i = 2; $i < $limit; $i++){
            $primes[$i] = true;
        }
        for ($n = 2; $n < $limit; $n++){
            if ($primes[$n]){
                for ($i = $n*$n; $i < $limit; $i += $n){
                    $primes[$i] = false;
                }
	        }
        }
  	    foreach($primes as $key => $value){
 		    if($value==1){
 			    $build_string = $key . ",";
                $string .=$build_string;
            };
 	    };
        $string = chop($string,",");
        print $string . "\n";
    };
?>
