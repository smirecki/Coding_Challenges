<?php

    $file_data = file_get_contents($argv[1]);
    $file_data = explode("\n",$file_data);
    
    foreach($file_data as $line){ // For Each Line
        $line = trim($line);
        if($line == "") continue;
            
    $line = explode(",",$line);

            $x1 = $line[0];
            $y1 = $line[1];
            $x2 = $line[2];
            $y2 = $line[3];
            $x3 = $line[4];
            $y3 = $line[5];
            $x4 = $line[6];
            $y4 = $line[7];

            if($y3>$y1 && $y3>$y2 && $y4>$y1 && $y4>$y2){
                print "False" . "\n";				//Above
            }elseif($y3<$y1 && $y3<$y2 && $y4<$y1 && $y4<$y2){
                   print "False" . "\n";			//Below
            }elseif($x3>$x1 && $x3>$x2 && $x4>$x1 && $x4>$x2){
                    print "False" . "\n";			//Right
            }elseif($x3<$x1 && $x3<$x2 && $x4<$x1 && $x4<$x2){
	                print "False" . "\n";			//Left
            }else{
	                print"True" . "\n";			//Overlapping
            };
    };
?>

