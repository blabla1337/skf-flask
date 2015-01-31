<?php 
header("Cache-Control: no-store, no-cache, must-revalidate"); // HTTP/1.1
header("Cache-Control: post-check=0, pre-check=0", false);
header("Pragma: no-cache"); // HTTP/1.0 
header('X-Frame-Options: SAMEORIGIN');
header("X-XSS-Protection:1; mode=block");
header('X-Content-Type-Options: nosniff'); 

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

// Turn off all error reporting
//error_reporting(0);
?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $title; ?></title>

    <!-- Bootstrap core CSS -->
    <link href="/html/css/bootstrap.css" rel="stylesheet">
    <!--external css-->
    <link href="/html/font-awesome/css/font-awesome.css" rel="stylesheet" />
    <?php //echo $wizardCss; ?>
    
    <!-- Custom styles for this template -->
    <link href="/html/css/style.css" rel="stylesheet">
    <link href="/html/css/style-responsive.css" rel="stylesheet">

    <link href="/html/css/table-responsive.css" rel="stylesheet">
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="/html/js/html5shiv.js"></script>
      <script src="/html/js/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

  <section id="container" >
      <!-- **********************************************************************************************************************************************************
      TOP BAR CONTENT & NOTIFICATIONS
      *********************************************************************************************************************************************************** -->
      <!--header start-->
      
      
      <header class="header black-bg">
      
      
      
              <div class="sidebar-toggle-box">
                  <div class="fa fa-bars tooltips" data-placement="right" data-original-title="Toggle Navigation"></div>
              </div>
            <!--logo start-->
            <a href="/dashboard" class="logo"><img style='margin-top:-10px;' width='105px;' height='50px;' src='/html/img/ricco.png'/></a>
            <!--logo end-->
            <div class="top-menu">
            	<ul class="nav pull-right top-menu">
                    <li><a class="logout" href="/login/delete">Logout</a></li>
            	</ul>
            </div>
            
                        <div style='margin-top:14px; margin-right:55px;' class="btn-group pull-right theme-container animated tada">
                <button class="btn btn-default dropdown-toggle" data-toggle="dropdown">
                    <i class="fa fa-code"></i><span
                        class="hidden-sm hidden-xs"> Code Language </span>
                    <span class="caret"></span>
                </button>
                <ul class="dropdown-menu" id="themes">
                    <li><a href="/code/lang/php">PHP</a></li>
                  <li><a href="/code/lang/java">Java</a></li>
                </ul>
            </div>
        </header>
      <!--header end-->
      
      <!-- **********************************************************************************************************************************************************
      MAIN SIDEBAR MENU
      *********************************************************************************************************************************************************** -->
      <!--sidebar start-->
      <aside>
          <div id="sidebar"  class="nav-collapse ">
              <!-- sidebar menu start-->
              <ul class="sidebar-menu" id="nav-accordion">
              	  <!-- 
              	  <p class="centered"><a href="profile.html"><img src="../html/img/logo.png" class="" width="60"></a></p>
              	  <h5 class="centered">Kingsafe</h5>
             -->
                  <li class="mt">
                      <a  <?php if(!empty($menuActiveKnowledge)){ echo $menuActiveKnowledge; }; ?> href="/knowledge">
                          <i class="fa fa-book"></i>
                          <span>Knowledge Base</span>
                      </a>
                  </li>

                  <li class="sub-menu">
                      <a <?php if(!empty($menuActiveProject)){ echo $menuActiveProject; }; ?> href="/project">
                          <i class="fa fa-th"></i>
                          <span>Projects</span>
                      </a>
                      <ul class="sub">
                          <li <?php if(!empty($menuActiveProjectNew)){ echo $menuActiveProjectNew; }; ?>><a href="/project/newproject">New Project</a></li>

                          <li <?php if(!empty($menuActiveProjectList)){ echo $menuActiveProjectList; }; ?>><a href="/project">List Projects</a></li>
	                                            </ul>
                  </li>


                 
                  </li>
                  <li <?php if(!empty($menuActiveProjectList)){ echo $menuActiveProjectList; }; ?> class="sub-menu">
                      <a href="javascript:;" >
                          <i class="fa fa-bar-chart-o"></i>
                          <span>Results</span>
                      </a>
                      <ul class="sub">
                          <li><a  href="/checklist/results">Checklists</a></li>
                          <li><a  href="/function/results">Functions</a></li>
                                               </ul>
                  </li>
                  

                  <li class="">
                      <a  <?php if(!empty($menuActive)){ echo $menuActive; }; ?> href="/code/examples">
                          <i class="fa fa-code"></i>
                          <span>Code examples</span>
                      </a>
                  </li>
           
              </ul>
              <!-- sidebar menu end-->
          </div>
      </aside>
      <!--sidebar end-->
    
