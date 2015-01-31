<?php

# Copyright 2014 Riccardo ten Cate
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class Db{
	
	private static $db;
	
	public static function init(){
		
		if (!self::$db){
			try {
				$dsn = 'mysql:host='.DB_HOST.';dbname='.DB_NAME;
				self::$db = new PDO($dsn, DB_USER, DB_PASS);
				self::$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
				self::$db->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
			}catch (PDOException $e){
				die('Connection error: ' . $e->getMessage());
			}
		}
		return self::$db;
	}
}
