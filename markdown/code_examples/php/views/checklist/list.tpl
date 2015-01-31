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
          	<h3>-<i class="fa fa-angle-right"></i><a href='/project'>Projects</a> -> <a href='/dashboard/results/<?php echo htmlspecialchars($identifier); ?>'> Getting started</a> -> <a href='/checklist/summary/<?php echo htmlspecialchars($identifier); ?>'> Cheklist summary</a> -> Security checklists</h3>
		  		<div class="row mt">
			  		<div class="col-lg-12">
                        <div class="alert alert-info">
<b>Note:</b>
Whenever you upload a new checklist and this one already exists for this project, the old version will be overwritten.
</div>
          
						<div class="content-panel">
               <table class="table table-striped table-advance table-hover"> 
                              <thead>
                              <tr>
                                  <th><i class="fa fa-bullhorn"></i> Checklist</th>
                              </tr>
                              </thead>
                              <tbody>
						       

              
                                                     
<form method="post" action="/checklist/checklistInsert/<?php echo htmlspecialchars($identifier); ?>">						
<?php
$i=0;
 foreach($checklist as $c):
 
 ?>
 
<tr>

<?php if($c['question'] != 'null'): $i++; ?>

  <td style='font-size:0.8em; border-style:solid; border-color:black; border-width:1px;'> <?php echo htmlspecialchars($c['question']); ?></td>
  <td></td>
    <td style='font-size:0.8em; border-style:solid; border-color:black; border-width:1px; text-align:center;'>
    <select name='answer<?php echo htmlspecialchars($i); ?>' >
    <option value='yes' >Done</option>
    <option value='no' >Not done</option>
    <option value='yes' >N.A.</option>
    </select>
    </td>
    <input type='hidden' name='vulnID<?php echo htmlspecialchars($i); ?>' value='<?php echo htmlspecialchars($c['vulnID']); ?>'/>
    <input type='hidden' name='questionID<?php echo htmlspecialchars($i); ?>' value='<?php echo htmlspecialchars($c['questionID']); ?>'/>
    <input type='hidden' name='listNameAnswer<?php echo htmlspecialchars($i); ?>' value='<?php echo htmlspecialchars($c['listName']); ?>'/>
    <input type='hidden' name='token' value='<?php echo $_SESSION['csrf']; ?>'/>
 
    </td>
</tr>




<?php endif; ?>

<?php if($c['question'] == 'null'): ?>
  <td style='padding-top:20px;' > <?php echo '<b>'.htmlspecialchars($c['head']).'</b>'?></td>
  <td></td>
    <td></td>
</tr>


<?php endif; ?>
<?php endforeach; ?>



                              </tbody>
                          </table>


                      </div><br/>
 <input style="float:right;" type="submit" class="btn btn-success" name="submitList" value="Add checklist"/>
 </form>	
               </div><!-- /col-lg-4 -->			
		  	</div><!-- /row -->
		</section><! --/wrapper -->
      </section><!-- /MAIN CONTENT -->
         
<?php include HOME . DS . 'includes' . DS . 'footer.inc.php'; ?>
