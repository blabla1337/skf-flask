<?php


# Copyright 2014 Riccardo ten Cate


//controller that will be loaded first.

$controller = "login";
$action = "index";
$query = null;

if (isset($_GET['load'])){
	
	$params = array();
	$params = explode("/", $_GET['load']);

	$controller = ucwords($params[0]);
	
	if (isset($params[1]) && !empty($params[1])){
		$action = $params[1];
	}
	
	if (isset($params[2]) && !empty($params[2])){
		$query = $params[2];
	}
	
	if (isset($params[3]) && !empty($params[3])){
		$query = $params[3];
	}
}

	$modelName = $controller;
	$controller .= 'Controller';
	$load = new $controller($modelName, $action);	

	if (method_exists($load, $action)){
	    $load->{$action}($query);
	}else{
		die('Invalid method. Please check the URL.');
	}
?>