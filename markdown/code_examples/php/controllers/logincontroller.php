<?php

# Copyright 2014 Riccardo ten Cate


class LoginController extends Controller{
	
	public function __construct($model, $action){
		parent::__construct($model, $action);
		$this->_setModel($model);
	}
	
	public function index(){
		
		try {
			
			if(!isset($_SESSION['access']) || (trim($_SESSION['access']) == '')) {
				session_start();
	        }
	        
			return $this->_view->output();
		}catch (Exception $e){
			echo '<h1>Application error:</h1>' . $e->getMessage();
		}
	}
	
	public function check(){
		
		$errors = array();
		$check = true;
			
		$username = isset($_POST['username']) ? trim($_POST['username']) : NULL;
		$password = isset($_POST['password']) ? trim($_POST['password']) : NULL;
		//$yubi = isset($_POST['yubi']) ? trim($_POST['yubi']) : NULL;
					
		if (empty($username) || empty($username) /* || empty($yubi)*/ ){
			$check = false;
			array_push($errors, "Niet alle velden zijn ingevuld.");
		}

			// data was not complete render standard page
	        if (!$check){
            	$this->_setView('index');
				$this->_view->set('errors', $errors);
				$this->_view->set('formData', $_POST);
				return $this->_view->output();
			}
			
			try {
		
				$userData = $this->_model->loginUser($username,$password);
				
				if(!empty($userData)){
					$this->_setView('success');	
					$this->_view->set('username', $userData['username']);	
				}else{
					$this->_setView('index');	
					array_push($errors, "Verkeerde gebruikersnaam/wachtwoord");
					$this->_view->set('errors', $errors);
				}
									
		} catch (Exception $e){
            $this->_setView('index');
            $this->_view->set('title', 'Zorgburo de liemers:: Error wrong username/password');
            $this->_view->set('formData', $_POST);
			$this->_view->set('saveError', $e->getMessage());
		}
	return $this->_view->output();
	}
	
	public function delete(){
	
		try {
			
			session_start();
			session_destroy();
			$this->_setView('index');
				
			return $this->_view->output();
			
		}catch (Exception $e){
			echo '<h1>Application error:</h1>' . $e->getMessage();
		}
	}
}
