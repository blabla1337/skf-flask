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
<?php  foreach($option as $optie){$projectID = $optie['projectID'];}  ?>
 
<!-- **********************************************************************************************************************************************************
      MAIN CONTENT
      *********************************************************************************************************************************************************** -->
      <!--main content start-->
      <section id="main-content">
          <section class="wrapper">
                    	<h3>-<i class="fa fa-angle-right"></i>  Checklist results -> Deleted</h3>
		  		<div class="row mt">
			  		<div class="col-lg-12">
						<div class="content-panel">
							<h4 class="mb"><i class="fa fa-angle-right"></i>Checklist was deleted</h4>
					  							
							</div>	
               </div><!-- /col-lg-4 -->			
		  	</div><!-- /row -->
		</section><! --/wrapper -->
      </section><!-- /MAIN CONTENT -->
         
<?php include HOME . DS . 'includes' . DS . 'footer.inc.php'; ?>
