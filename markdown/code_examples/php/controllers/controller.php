<?php

# Copyright 2014 Riccardo ten Cate


class Controller{
	
	protected $_model;
	protected $_controller;
	protected $_action;
	protected $_view;
	protected $_modelBaseName;
	
	public function __construct($model, $action){
		
		$this->_controller = ucwords(__CLASS__);
		$this->_action = $action;
		$this->_modelBaseName = $model;
		$this->_view = new View(HOME . DS . 'views' . DS . strtolower($this->_modelBaseName) . DS . $action . '.tpl');
	}
	
	protected function _setModel($modelName){
		$modelName .= 'Model';
		$this->_model = new $modelName();
	}
	
	protected function _setView($viewName){
		$this->_view = new View(HOME . DS . 'views' . DS . strtolower($this->_modelBaseName) . DS . $viewName . '.tpl');
	}
	
	protected function _checkSession(){
			session_start();
			if($_SESSION['access'] != "active"){
			if($_SESSION['access'] ==''){
				
				header("Location: /login");
				die();
			}
				}
	}



	protected function _checkCsrf($token){
		session_start();	
		if($_SESSION['csrf'] != $token){
			session_destroy();
			header("Location: /login");
			die();
		}
	}
	
}
