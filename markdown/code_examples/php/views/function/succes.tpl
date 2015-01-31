<?php  header("refresh:2;url=/function/results" );  ?>
<?php include HOME . DS . 'includes' . DS . 'header.inc.php'; ?>
<?php  foreach($option as $optie){$projectID = $optie['projectID'];}  ?>
 
<!-- **********************************************************************************************************************************************************
      MAIN CONTENT
      *********************************************************************************************************************************************************** -->
      <!--main content start-->
      <section id="main-content">
          <section class="wrapper">
          	<h3>-<i class="fa fa-angle-right"></i><a href='#'>Projects</a> -> <a href='#'> Getting started</a> -> Add functions  -> Succes</h3>
		  		<div class="row mt">
			  		<div class="col-lg-12">
						<div class="content-panel">
							<h4 class="mb"><i class="fa fa-angle-right"></i> New project is stored, You will be redirected to the results page!</h4>
					  							
							</div>	
               </div><!-- /col-lg-4 -->			
		  	</div><!-- /row -->
		</section><! --/wrapper -->
      </section><!-- /MAIN CONTENT -->
         
<?php include HOME . DS . 'includes' . DS . 'footer.inc.php'; ?>
