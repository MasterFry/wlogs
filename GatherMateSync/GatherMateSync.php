<?php

function error($msg)
{
  echo "ERROR\n" . $msg . "\n";
  exit();
}

function success($data = null)
{
  echo "SUCCESS\n";
  if(data != null)
    echo $data;
  echo "\n";
  exit();
}

$FILENAME = "GatherMateData.json";

$type = $_SERVER["REQUEST_METHOD"];
if($type == "GET")
{
  $file = fopen($FILENAME, "r") or error("Failed to open file!");
  $data = fread($file, filesize($FILENAME));
  fclose($file);
  success($data);
} 
elseif ($type == "POST")
{
  $data = file_get_contents("php://input");
  if(!$data)
      error("No Data received!");
  
  $file = fopen($FILENAME, "w") or error("Failed to open file!");
  fwrite($file, $data);
  fclose($file);
  success();
} 
else
{
  error("Invalid type: " . $type);
}
