<?php include HOME . DS . 'includes' . DS . 'header.inc.php'; ?>
 
<!-- **********************************************************************************************************************************************************
      MAIN CONTENT
      *********************************************************************************************************************************************************** -->
      <!--main content start-->
      <section id="main-content">
          <section class="wrapper">
          	<h3><i class="fa fa-angle-right"></i> history of your projects</h3>
		  		<div class="row mt">
			  		<div class="col-lg-12">
						<div class="content-panel">
                         <table class="table table-striped table-advance table-hover"> 
                              <thead>
                              <tr>
                                  <th><i class="fa fa-bullhorn"></i> Project Name</th>
                                  <th class="hidden-phone"><i class="fa fa-question-circle"></i> Description</th>
                                  <th><i class="fa fa-bookmark"></i> Project version</th>
                                  <th><i class=" fa fa-edit"></i> Date/Time</th>
                                  <th><i class=" fa fa-times"></i> Delete</th>
                                  <th></th>
                              </tr>
                              </thead>
                              <tbody>
						<?php
						    if ($projects):
						    $i=0;
						    foreach ($projects as $project): ?>
                              <?php $i++;?>
                              <tr>
                                  <td><a href="/dashboard/results/<?php echo $project['projectID']; ?>/"><?php echo htmlspecialchars($project['projectName']); ?></a></td>
                                  <td style='max-width:250px;' class="hidden-phone">
                                  <?php echo htmlspecialchars(substr($project['projectDesc'],0, 50)); 
                                  if(strlen($project['projectDesc']) > 49):
                                  echo "...";
                                  endif;
                                  
                                  ?>
                                  
                                  </td>
                                  <td><?php echo htmlspecialchars($project['projectVersion']); ?></td>
                                  <td><span class="label label-info label-mini"><?php echo htmlspecialchars($project['timestamp']); ?></span></td>
                                  <td>  <!-- Button trigger modal -->
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
						          
						<p>When you press the "Remove project" button, This project will be deleted<br/>
						Are you sure you want to continue.
						</p>


								  </table>
						          </div>
						          <div class="modal-footer">
						          <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
						         <a href='/project/projectDelete/<?php echo $project['projectID']; ?>' <input type="submit" name="" class="btn btn-danger" value='Remove functions'/>Remove Project</a>
						          </form>
						          </div>
						          </div>
						  		  </div>
								  </div>      				
      							  </div><!-                </td>
                                  <td>

                                  </td>
                              </tr>
							<?php
						    endforeach; ?>
						<?php endif; ?>
                              
                     
                              </tbody>
                          </table>
                      </div>
	
               </div><!-- /col-lg-4 -->			
		  	</div><!-- /row -->
		</section><! --/wrapper -->
      </section><!-- /MAIN CONTENT -->
         
<?php include HOME . DS . 'includes' . DS . 'footer.inc.php'; ?>
