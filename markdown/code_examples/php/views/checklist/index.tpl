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


include HOME . DS . 'includes' . DS . 'header.inc.php'; 

foreach($projectID as $proj):  $identifier = $proj['projectID']; endforeach;
?>

<!-- **********************************************************************************************************************************************************
      MAIN CONTENT
      *********************************************************************************************************************************************************** -->
      <!--main content start-->
      <section id="main-content">
          <section class="wrapper">
          	<h3>-<i class="fa fa-angle-right"></i><a href='/project'>Projects</a> -> <a href='/dashboard/results/<?php echo htmlspecialchars($identifier); ?>'> Getting started</a> -> Security checklists</h3>
		  		<div class="row mt">
			  		<div class="col-lg-12">
                        <div class="alert alert-info">
<b>Note:</b>
This is the post-development stage, here we double check our implementation of functionality.
</div>
          
						<div class="content-panel">
               <table class="table table-striped table-advance table-hover"> 
                              <thead>
                              <tr>
                                  <th><i class="fa fa-bullhorn"></i> Checklist</th>
                                  <th class="hidden-phone"><i class="fa fa-question-circle"></i> Description</th>
                                  <th><i class="fa fa-bookmark"></i> Level</th>
                                  <th></th>
                                  <th><i class=" fa fa-edit"></i> Take list</th>
                              </tr>
                              </thead>
                              <tbody>
						       
                             <?php
$count = 0;
 foreach($checkSum as $c):
 
 ?>
                                                          <tr>
                                  <td><a href="basic_table.html#"></a><?php echo $c['listName']; ?></td>
                                  <td class="hidden-phone">.</td>
                                  <td class="hidden-phone">Recommended</td>
                                  <td></td>
                                  <td>

      				              <div class="showbak">
      						      <!-- Button trigger modal -->
					         <form method="post" action="/checklist/takelist/<?php echo htmlspecialchars($identifier);?>">
					         <input type="submit" class="btn btn-success btn-xs" value="start"/>
					         <input type="hidden" value="<?php echo $c['listName']; ?> " name="list"/>
					         <input type="hidden" value="<?php echo $_SESSION['csrf']; ?> " name="token"/>
					         
					         </form>

						         

<?php endforeach; ?>                                      
                                      
                        
						





                              </tbody>
                          </table>

                      </div>
	
               </div><!-- /col-lg-4 -->			
		  	</div><!-- /row -->
		</section><! --/wrapper -->
      </section><!-- /MAIN CONTENT -->
         
<?php include HOME . DS . 'includes' . DS . 'footer.inc.php'; ?>
