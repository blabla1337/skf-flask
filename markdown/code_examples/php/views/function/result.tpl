<?php include HOME . DS . 'includes' . DS . 'header.inc.php'; ?>

 
<!-- **********************************************************************************************************************************************************
      MAIN CONTENT
      *********************************************************************************************************************************************************** -->
      <!--main content start-->
      <section id="main-content">
          <section class="wrapper">

		  		<div class="row mt">
			  		<div class="col-lg-12">
						<div class="-panel">
          	<h3><i class="fa fa-angle-right"></i> Function results</h3>
						<?php
                            if(!$projectResults):
                           	echo' <div class="alert alert-danger">There were no function lists found. <br/>Create a list in order to create results.</div> ';
                            endif;
                        ?>
                        
                        <?php
						
                            if($projectResults):
                           	echo' <div class="alert alert-info">Summary of all checklist-results.</div> ';
                            endif;
                        ?>


<?php if($projectResults): ?>							

      				<div class="showback">


		  	<div class="row mt">
                  <div class="col-md-12">
                      <div style='margin-top:-25px;' class="content-panel">
                          <table class="table table-striped table-advance table-hover">
	                  	  	  <h4><i class="fa fa-angle-right"></i>Project</h4>
	                  	  	  <hr>
                              <thead>
                              <tr>
                                  <th><i class="fa fa-bulhorn"></i> <b>Functions list</b></th>
                                  <th class="hidden-phne"><i class="fa fa-qustion-circle"></i><b>Version</b></th>
                                  <th><b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Edit</b></th>
                              </tr>
                              </thead>
                              <tbody>
                              
                              <?php
                              	$i=0;
                               	foreach ($projectResults as $o):
                                $i++;
                                ?>
                             
                              <tr>
                                  <td><?php echo htmlspecialchars($o['projectName']); ?></td>
                                  <td class="hidden-phone">&nbsp;&nbsp;&nbsp;<?php echo htmlspecialchars($o['projectVersion']); ?></td>
                                  <td>
                                       &nbsp;&nbsp;&nbsp;&nbsp;<a href="/functionpdf/functions/<?php echo htmlspecialchars($o['projectID']); ?>" target='' ><button class="btn btn-success btn-xs"><i class="fa fa-download "></i></button></a>
                                             				           
      						      <!-- Button trigger modal -->
					         	  <button class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModal<?php echo $i; ?>">
						          <i class="fa fa-times "></i>                  
					              </button>
						
						          <!-- Modal -->
						          <div class="modal fade" id="myModal<?php echo $i; ?>" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
						          <div class="modal-dialog">
						          <div class="modal-content">
						          <div class="modal-header">
						          <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
						          <h4 class="modal-title" id="myModalLabel">Warning</h4>
						          </div>
						          <div   class="modal-body">
						          <table id='checklist' style="width:525px">
						          
						<p>When you press the "Remove functions" button, all the functions which this project contains will be deleted from the documentation<br/>
						Are you sure you want to continue.
						</p>


								  </table>
						          </div>
						          <div class="modal-footer">
						          <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
						         <a href='/function/deleteFunction/<?php echo htmlspecialchars($o['functionName']); ?>' <input type="submit" name="submitCertifiedsecure" class="btn btn-danger" value='Remove functions'/>Remove functions</a>
						          </form>
						          </div>
						          </div>
						  		  </div>
								  </div>      				
      							  </div><!-                  
      							  
      							  </td>
                              </tr>
                             							<?php
						    endforeach; ?>
						

                              </tbody>
                          </table>
                      </div><!-- /content-panel -->
                  </div><!-- /col-md-12 -->
              </div><!-- /row -->
<br/>




<?php endif; ?>
						<!-- Modal -->
						<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
						  <div class="modal-dialog">
						    <div class="modal-content">
						      <div class="modal-header">
						        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
						        <h4 class="modal-title" id="myModalLabel">Generate results</h4>
						      </div>
						      <div class="modal-body">
						      Select a project from which results should be generated<br/><br/>
						    <form method='post' action='/functionResults/search'>
						      <select name='projectSearch'>

						      <?php
						    if ($details):
						    foreach ($details as $d): ?>
                              
						      <option value='<?php echo htmlspecialchars($d['projectName']); ?>' ><?php echo htmlspecialchars($d['projectName']); ?></option>
						     
						     	<?php
						    endforeach; ?>
						<?php endif; ?>
                              
						      </select>
						      
						      </div>
						      <div class="modal-footer">
						        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
						        <input type="submit" value='Generate results' class="btn btn-primary"/>
						        </form>
						      </div>
						    </div>
						  </div>
						</div>      				
      				</div><!-- /showback -->
      				
      				
							</div>	
               </div><!-- /col-lg-4 -->			
		  	</div><!-- /row -->
		</section><! --/wrapper -->
      </section><!-- /MAIN CONTENT -->
         
<?php include HOME . DS . 'includes' . DS . 'footer.inc.php'; ?>
