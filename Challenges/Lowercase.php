<?php
//Convert all text to lowercase.
$file_data = file_get_contents($argv[1]);
        // File Data "Sanitation"
        $file_data = str_replace("\r\n","\n",$file_data);
        $file_data = str_replace("\r","\n",$file_data);
        // Make each line in the file an array.
        $file_data = explode("\n",$file_data);
        
        foreach($file_data as $line)
            { // For Each Line
            $line = trim($line);
            if($line == "") continue; // Continue the loop if the line is blank
              $line = strtolower($line);
              print $line . "\n";
            }
        
?>

