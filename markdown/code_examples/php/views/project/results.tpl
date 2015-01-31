<?php include HOME . DS . 'includes' . DS . 'header.inc.php'; ?>

<?php  foreach($option as $optie){$projectID = $optie['projectID'];}  ?>

<!-- **********************************************************************************************************************************************************
      MAIN CONTENT
      *********************************************************************************************************************************************************** -->
      <!--main content start-->
      <section id="main-content">
          <section class="wrapper">
          	<h3>-<i class="fa fa-angle-right"></i><a href='/project'>Projects</a> -> Getting started</h3>
		  		<div class="row mt">
			  		<div class="col-lg-12">
						<div class="content-panel">
                 
                 <div class="row">
<div class="col-lg-4 col-md-4 col-sm-4 mb">
<div style='margin-left:10px; margin-right:10px;' class="product-panel-2 pn">



<br/>
<h4 class="mt">Add processing functions</h4>
<br/>
<a class='fa fa-file-code-o fa-4x' href='/show/addfunctions/<?php echo htmlspecialchars($projectID); ?>/'></a>
<br/><br/><br/>
<a href='/show/addfunctions/<?php echo htmlspecialchars($projectID); ?>/'><button class="btn btn-small btn-theme04">Start project</button></a>
</div>
</div>


<div class="col-lg-4 col-md-4 col-sm-4 mb">
<div style='margin-left:10px; margin-right:10px;' class="product-panel-2 pn">

<br/>
<h4 class="mt">Add new checklists</h4>
<br/>
<a class='fa fa-file-text-o fa-4x' href='/checklistSummary/summary/<?php echo htmlspecialchars($projectID); ?>/'></a>
<br/><br/><br/>
<a href='/checklistsummary/summary/<?php echo htmlspecialchars($projectID); ?>/'><button class="btn btn-small btn-theme04">Start project</button></a>
</div>
</div>

<div class="col-lg-4 col-md-4 col-sm-4 mb">
<div style='margin-left:10px; margin-right:10px;' class="product-panel-2 pn">

<br/>
<h4 class="mt">Security knowledge base</h4>
<br/>
<a class='fa fa-university fa-4x' href='/project/newproject'></a>
<br/><br/><br/>
<a href='/knowledge/'><button class="btn btn-small btn-theme04">View item</button></a>
</div>
</div>



  
                      </div>
	
               </div><!-- /col-lg-4 -->			
		  	</div><!-- /row -->
		</section><! --/wrapper -->
      </section><!-- /MAIN CONTENT -->
         
<?php include HOME . DS . 'includes' . DS . 'footer.inc.php'; ?>
