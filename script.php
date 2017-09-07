<?php 

$name = $_GET['name'];
$cmd = escapeshellcmd("python C:/Users/rishi/Desktop/Search_Engine/test.py $name 2>&1");

echo "$cmd" . PHP_EOL;

exec($cmd, $output, $return_var);

echo "$return_var:" . PHP_EOL;
print_r($output);
?>