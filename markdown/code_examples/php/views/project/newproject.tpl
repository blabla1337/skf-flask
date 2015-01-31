<?php include HOME . DS . 'includes' . DS . 'header.inc.php'; ?>
 
<!-- **********************************************************************************************************************************************************
      MAIN CONTENT
      *********************************************************************************************************************************************************** -->
      <!--main content start-->
      <section id="main-content">
          <section class="wrapper">          
          	<h3><i class="fa fa-angle-right"></i> Create new project</h3>
   

		  		<div class="row mt">
			  		<div class="col-lg-12">
						<div class="content-panel">
							<h4 class="mb"><i class="fa fa-angle-right"></i> Project</h4>

							<form class="form-horizontal" role="form" style="padding-left:20px;padding-right:20px;" method="post" action="/project/step1">
							<div class="form-group">
							    <label for="inputName" class="col-sm-2 control-label">Project Name</label>
							    <div class="col-sm-10">
							      <input type="text" class="form-control" name="inputName" id="inputName" value="<?php if(isset($formData)) echo htmlspecialchars($formData['inputName']); ?>" placeholder="Project Name">
							    </div>
							  </div>
							  <div class="form-group">
							    <label for="inputVersion" class="col-sm-2 control-label">Project Version</label>
							    <div class="col-sm-10">
							      <input type="text" class="form-control" id="inputVersion" name="inputVersion" value="<?php if(isset($formData)) echo htmlspecialchars($formData['inputVersion']); ?>" placeholder="Project version">
							    </div>
							  </div>
							  

							  <div class="form-group">
							    <label for="inputDesc" class="col-sm-2 control-label">Project Description</label>
							    <div class="col-sm-10">
									<textarea class="form-control" name="inputDesc" value="<?php if(isset($formData)) echo htmlspecialchars($formData['inputDesc']); ?>" id="inputDesc" rows="3" placeholder="Project Description"></textarea>
							    </div>
							  </div>
							  <div class="form-group">
							    <div class="col-sm-offset-2 col-sm-10">
							    							      <input type="hidden" name="token" value="<?php echo htmlspecialchars($_SESSION['csrf']); ?>" id="token">
							      <input type="submit" id="projectFormSubmit" name="projectFormSubmit" value="Create Project" class="btn btn-default">
							    </div>
							  </div>
							  
							<?php 


								
								if (isset($saveError)){
									echo "<h2>Error please try again.</h2>" . htmlspecialchars($saveError);
								}
								?>
							</form>
							
							</div>	
               </div><!-- /col-lg-4 -->			
		  	</div><!-- /row -->
		</section><! --/wrapper -->
      </section><!-- /MAIN CONTENT -->
         
<?php include HOME . DS . 'includes' . DS . 'footer.inc.php'; ?>
