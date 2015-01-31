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
          	<h3><i class="fa fa-angle-right"></i> Checklist results</h3>
          	<br/>
          				  		
						<?php
                            if(!$projectResults):
                           	echo' <div class="alert alert-danger">There were no checklists found. <br/>Create a project and use the checklist forms in order to create results.</div> ';
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
	                  	  	  <h4><i class="fa fa-angle-right"></i>Checklists</h4>
	                  	  	  <hr>
                              <thead>
                              <tr>
                                  <th><i class="fa fa-bulhorn"></i> <b>Project</b></th>
                                  <th class="hidden-phne"><i class="fa fa-qustion-circle"></i><b> Checklist</b></th>
                                  <th><b>Date</b></th>
                                  <th><b>Download</b></th>
                              </tr>
                              </thead>
                              <tbody>
<?php								
									$i=0;	    
									foreach ($projectResults as $o): 
									$i++;
?>
                              
                              <tr>
                                  <td><?php echo $o['projectName'].' '.$o['projectVersion'] ?></td>
                                  <td class="hidden-phone"><?php echo $o['listName']; ?></td>
                              	 <td><span class="label label-info label-mini"><?php echo htmlspecialchars($o['entryDate']); ?></span></td>
                                  <td>
                                  <?php
                                  echo "<a href='/checklistpdf/checklists/".$o['entryDate']." ' target='_self' >  
                                  <button class='btn btn-success btn-xs'><centeR><i class='fa fa-download'></i></center></button></a>";?>
                              	  <!-- Button trigger modal -->
					         	  <button class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModal<?php echo $i ?>"">
						          <i class="fa fa-times "></i>                  
					              </button>
						
						          <!-- Modal -->
						          <div class="modal fade" id="myModal<?php echo $i ?>" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
						          <div class="modal-dialog">
						          <div class="modal-content">
						          <div class="modal-header">
						          <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
						          <h4 class="modal-title" id="myModalLabel">Warning</h4>
						          </div>
						          <div   class="modal-body">
						          <table id='checklist' style="width:525px">
						          
									<p>When you press the "Remove checklist" button, the checklist which this project contains will be deleted from the documentation
									Are you sure you want to continue.
									</p>


								  </table>
						          </div>
						          <div class="modal-footer">
						          <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
							   	<a href='/checklist/deleteList/<?php echo $o['entryDate']; ?>' <input type="submit" name="submitCertifiedsecure" class="btn btn-danger" value='Remove functions'/>Remove Checklist</a>
						          </form>
						          </div>
						          </div>
						  		  </div>
								  </div>      				
      							  </div><!-  
                              	
                                  </td>
                              </tr>
                              
                     
                              
                                 
                             							<?php
						    endforeach; 
						    
						    ?>
						

                              </tbody>
                          </table>
                          <?php endif; ?>
                      </div><!-- /content-panel -->
                  </div><!-- /col-md-12 -->
              </div><!-- /row -->



	
		  	</div><!-- /row -->
		</section><! --/wrapper -->
      </section><!-- /MAIN CONTENT -->
         
<?php include HOME . DS . 'includes' . DS . 'footer.inc.php'; ?>
