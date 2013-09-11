<?php
//Fibonacci Series

$file_data = file_get_contents($argv[1]);
        // File Data "Sanitation"
        $file_data = str_replace("\r\n","\n",$file_data);
        $file_data = str_replace("\r","\n",$file_data);
        // Make each line in the file an array.
        $file_data = explode("\n",$file_data);
	
	foreach($file_data as $line){
                $line = trim($line);
                if($line == "") continue;
		
		$fibSeries = array(0,1);

		for($n=2; $n<=$line; $n++){
			$fibSeries[$n] = $fibSeries[$n-1] + $fibSeries[$n-2];
			array_push($fibSeries,$fibSeries[$n]);	

		};
			print $fibSeries[$line] . "\n";
	};
?>
