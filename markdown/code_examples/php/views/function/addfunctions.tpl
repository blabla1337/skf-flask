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


include HOME . DS . 'includes' . DS . 'header.inc.php'; ?>
<?php  foreach($projectID as $optie){$projectID = $optie['projectID'];}  ?>
 <style>
 .tbl_container{ overflow:auto; width: 500px;height: 200px; }
 </style>
 


 
<!-- **********************************************************************************************************************************************************
      MAIN CONTENT
      *********************************************************************************************************************************************************** -->
      <!--main content start-->
      <section id="main-content">
          <section class="wrapper">
          	<h3>-<i class="fa fa-angle-right"></i><a href='/project'>Projects</a> -> <a href='/show/results/<?php echo htmlspecialchars($projectID); ?>'> Getting started</a> -> Add functions</h3>
          							<?php
if (isset($errors)) {

	foreach ($errors as $e){
	
	echo '<div class="alert alert-danger">'.htmlspecialchars($e).'</div> ';
	}
} 

?> 

		  		<div class="row mt">
						
			  		<div class="col-lg-12">
			  		<div class="alert alert-info"><b>Note:</b> Here we enter the processing techniques the application contains. For example, File upload, HTML ouput, SQL queries etc.<br/>
			  		All lists will be collected into a single document per project.
			  		</div>
						<div class="">
              
                 <div class="">
<div class="col-lg-4 col-md-4 col-sm-4 mb">

<div style='float:left; margin-left:-12px;' class="">
<h4>
<button class="btn btn-success btn-lg" data-target="#myModal" data-toggle="modal">Add list</button>
<div id="myModal" class="modal fade" aria-hidden="true" aria-labelledby="myModalLabel" role="dialog" tabindex="-1" style="display: none;">
<div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
<button class="close" aria-hidden="true" data-dismiss="modal" type="button">×</button>
<h4 id="myModalLabel" class="modal-title">Add a new function</h4>
</div>
<div class="modal-body">Please enter the number of processing techniques the application contains.<br/><br/>
<form method='post'>
<input type="number" placeholder='0' name='numbers' min="0" max="100" step="1" id="test" />
</div>
<div class="modal-footer">
<button class="btn btn-default" data-dismiss="modal" type="button">Close</button>
<input type='submit' class="btn btn-primary" value='Add values' name='submit' type="button">
</form>
</div>
</div>
</div>
</div>
</div>
</div>
</div><!-- /col-lg-4 -->			
</div><!-- /row -->


<?php if(isset($_POST['submit'])):?>

		  		<div class="row mt">
			  		<div class="col-lg-12">
						<div class="">
              
                 <div class="">
<div class="col-lg-4 col-md-4 col-sm-4 mb">

<div style='float:left;  margin-left:-12px;'' class="">
<h4>
<button style='margin-top:-60px;' class="btn btn-warning btn-lg" data-target="#myModal1" style='visibility:none' data-toggle="modal">Result</button>
<div id="myModal1" class="modal fade" aria-hidden="true" aria-labelledby="myModalLabel" role="dialog" tabindex="-1" style="display: none;">
<div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
<button class="close" aria-hidden="true" data-dismiss="modal" type="button">×</button>
<h4 id="myModalLabel" class="modal-title">Add a new function</h4>
</div>
<div class="modal-body">Please select the processing techniques which your application contains<br/><br/>
<div class="tbl_container">
<form method='post' action='/function/insertFunctions/<?php echo htmlspecialchars($projectID); ?>'>
<input type='text' name='functionName' placeholder='List name'/><br/><br/>
<textarea name='functionDesc' placeholder='List description'></textarea><br/><br/>
<?php for($int = 0; $int < htmlspecialchars($_POST['numbers']); $int++): ?>
 
<select name='tech<?php echo htmlspecialchars($int); ?>'>
	<?php
	if ($dropdown):
	$i = 0;
	foreach ($dropdown as $d): ?>
							
     <option value="<?php echo htmlspecialchars($d['techID']); ?>"> <?php echo htmlspecialchars($d['techName']);?> </option>
  
   <?php endforeach; ?>
</select> 	
<input type="hidden" name="token" value="<?php echo htmlspecialchars($_SESSION['csrf']); ?>" id="token">
<br/>
<?php
	 endif;//if dropwdown
	 endfor;
?>
</div>
<div class="modal-footer">
<button class="btn btn-default" data-dismiss="modal" type="button">Close</button>
<input type='submit' class="btn btn-primary" value='Add values' name='submit' type="button">
</form>
</div>
</div>
</div>
</div>
</div>
</div>
</div><!-- /col-lg-4 -->			
</div><!-- /row -->

<?php endif;//if post submit 
 if($projects):// if there are projects than show the summary
 
?>
	
		  	<div class="row mt">
                  <div class="col-md-12">
                      <div style='margin-top:-25px;' class="content-panel">
                          <table class="table table-striped table-advance table-hover">
	                  	  	  <h4><i class="fa fa-angle-right"></i>Function summary</h4>
	                  	  	  <hr>
                              <thead>
                              <tr>
                                  <th><i class="fa fa-bulhorn"></i> <b>Function</b></th>
                                  <th class="hidden-phne"><i class="fa fa-qustion-circle"></i><b> List name</b></th>
                                  <th><i class=" fa fa-edit"></i> Date/Time</th>
                                  <th><b>Remove</b></th>
                              </tr>
                              </thead>
                              <tbody>
                              <?php
                               
						    foreach ($projects as $o): ?>
                              
                              <tr>
                                  <td><?php echo htmlspecialchars($o['techName']); ?></td>
                                  <td class="hidden-phone">&nbsp;&nbsp;&nbsp;<?php echo htmlspecialchars($o['functionName']); ?></td>
                                           <td><span class="label label-info label-mini"><?php echo htmlspecialchars($o['entryDate']); ?></span></td>
                         
                                  <td>
                                    
                                         <!-- Button trigger modal -->
					         	 &nbsp;&nbsp; <button class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModal<?php echo $o['paramID']; ?>">
						          <i class="fa fa-times "></i>                  
					              </button>
						
						          <!-- Modal -->
						          <div class="modal fade" id="myModal<?php echo $o['paramID'];?>" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
						          <div class="modal-dialog">
						          <div class="modal-content">
						          <div class="modal-header">
						          <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
						          <h4 class="modal-title" id="myModalLabel">Warning</h4>
						          </div>
						          <div   class="modal-body">
						          <table id='checklist' style="width:525px">
						          
						<p>When you press the "Remove function" button, the function which this project contains will be deleted from the documentation<br/>
						Are you sure you want to continue.
						</p>


								  </table>
						          </div>
						          <div class="modal-footer">
						          <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
						       <a href='/function/deleteFunction/<?php echo htmlspecialchars($o['functionName']); ?>'<button class="btn btn-danger "></button>Remove function </a>   </form>
						          </div>
						          </div>
						  		  </div>
								  </div>      				
      							  </div><!-                
                                  </td>
                              </tr>
                             							<?php
						    endforeach; ?>
						<?php endif; ?>

                              </tbody>
                          </table>
                      </div><!-- /content-panel -->
                  </div><!-- /col-md-12 -->
              </div><!-- /row -->
              
              
		</section><! --/wrapper -->
      </section><!-- /MAIN CONTENT -->
         
         
         <!-- js placed at the end of the document so the pages load faster -->
    <script src="assets/js/jquery.js"></script>
    <script src="assets/js/bootstrap.min.js"></script>
    <script class="include" type="text/javascript" src="assets/js/jquery.dcjqaccordion.2.7.js"></script>
    <script src="assets/js/jquery.scrollTo.min.js"></script>
    <script src="assets/js/jquery.nicescroll.js" type="text/javascript"></script>
    <script type="text/javascript" src="assets/js/gritter/js/jquery.gritter.js"></script>
    <script type="text/javascript" src="assets/js/gritter-conf.js"></script>
    


    <!--common script for all pages-->
    <script src="assets/js/common-scripts.js"></script>
         
<?php include HOME . DS . 'includes' . DS . 'footer.inc.php'; ?>
