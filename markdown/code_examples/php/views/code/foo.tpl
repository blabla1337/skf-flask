<?php  include HOME . DS . 'includes' . DS . 'header.inc.php'; e ?>
 
<!-- **********************************************************************************************************************************************************
      MAIN CONTENT
      *********************************************************************************************************************************************************** -->
      <!--main content start-->
 <?php
						    foreach ($exam as $a): 
							
			
						$test  = preg_replace('/\s+/', '_', $a['codeName']);
						$v     = preg_quote($v, '/');
						$test1 = preg_replace("/\//", '_', $test);
						
						echo $test1;
						
						$fp = fopen($a['codeID'].'-code_example--'.$test1.'--.md', 'w');
						
						$writeString=
"
".$a['codeName']."
-------

**Example:**



		".$a['codeExample']."


	";
						
						fwrite($fp, $writeString);
						fclose($fp);
						
						    endforeach; 
						
						?>

         
<?php include HOME . DS . 'includes' . DS . 'footer.inc.php'; ?>


