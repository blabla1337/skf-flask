<?php  include HOME . DS . 'includes' . DS . 'header.inc.php'; e ?>
 
<!-- **********************************************************************************************************************************************************
      MAIN CONTENT
      *********************************************************************************************************************************************************** -->
      <!--main content start-->
      <section id="main-content">
          <section class="wrapper">
          	<h3><i class="fa fa-angle-right"></i> Knowledge Base code examples <?php echo $_SESSION['ref']; ?></h3>
          	         <?php if($exam): ?>
          	          	<form  method="post" action="/code/search"><br/>
          	<input type="text" name="search" placeholder="Search vulnerability"/>
          	</form>
		  		<div class="row mt">
			  		<div class="col-lg-12">
			  		
                       <div class="panel-group" id="accordion">
						<?php 
						    foreach ($exam as $ss):  
							 ?>
						  <div class="panel panel-default">
						    <div class="panel-heading" style='background-color:white;'>
						      <h4 class="panel-title">
						        <a data-toggle="collapse" data-parent="#accordion" href="#collapse<?php echo $ss['codeID']; ?>">
						          <?php echo htmlspecialchars($ss['codeName']); ?>
						        </a>
						      </h4>
						    </div>
						    <div id="collapse<?php echo $ss['codeID']; ?>" class="panel-collapse collapse">
						      <div class="panel-body" style='background-color:#f5f5f5;'>
						
							<b>Code:</b><br>					        
							<p><?php echo highlight_string($ss['codeExample']); ?></p>
						      </div>
						    </div>
						  </div>
						<?php
						    endforeach; 
						    endif;
						    
						    if(!$exam):
						    	echo'<br/>';
						    	echo'<br/>';
								echo'<div class="alert alert-info">';
								echo'<center>';
								echo'<b>Note:</b>';
								echo'No search results were found, please select your preferred code language in the "code language" tab located in the top right corner.';
								echo'</center>';
								echo'</div>   ';	
						 
						    endif;
						    ?>
						
					</div>                           
               </div><!-- /col-lg-4 -->			
		  	</div><!-- /row -->
		</section><! --/wrapper -->
      </section><!-- /MAIN CONTENT -->
         
<?php include HOME . DS . 'includes' . DS . 'footer.inc.php'; ?>


