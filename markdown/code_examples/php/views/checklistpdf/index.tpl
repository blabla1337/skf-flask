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


foreach($func as $f):

$projectName   = $f['projectName'];
$date 		   = $f['entryDate'];

endforeach;

$tab = 'http://'.$_SERVER['HTTP_HOST'];


//============================================================+
// File name   : example_006.php
// Begin       : 2008-03-04
// Last Update : 2013-05-14
//
// Description : Example 006 for TCPDF class
//               WriteHTML and RTL support
//
// Author: Nicola Asuni
//
// (c) Copyright:
//               Nicola Asuni
//               Tecnick.com LTD
//               www.tecnick.com
//               info@tecnick.com
//============================================================+

/**
 * Creates an example PDF TEST document using TCPDF
 * @package com.tecnick.tcpdf
 * @abstract TCPDF - Example: WriteHTML and RTL support
 * @author Nicola Asuni
 * @since 2008-03-04
 */

// Include the main TCPDF library (search for installation path).
require_once('libs/tcpdf/tcpdf.php');


// create new PDF document
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

// set document information
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetAuthor('Riccardo ten Cate');
$pdf->SetTitle('Security knowledge framework');
$pdf->SetSubject('www.securityknowledgeframework.nl');
$pdf->SetKeywords('info@kingsafe.nl');

// set default header data
$pdf->SetHeaderData('tcpdf_logo.jpg', '15px;', ' security knowledge framework', '       Post-development');

// set header and footer fonts
$pdf->setHeaderFont(Array(PDF_FONT_NAME_MAIN, '', PDF_FONT_SIZE_MAIN));
$pdf->setFooterFont(Array(PDF_FONT_NAME_DATA, '', PDF_FONT_SIZE_DATA));

// set default monospaced font
$pdf->SetDefaultMonospacedFont(PDF_FONT_MONOSPACED);

// set margins
$pdf->SetMargins(PDF_MARGIN_LEFT, PDF_MARGIN_TOP, PDF_MARGIN_RIGHT);
$pdf->SetHeaderMargin(PDF_MARGIN_HEADER);
$pdf->SetFooterMargin(PDF_MARGIN_FOOTER);

// set auto page breaks
$pdf->SetAutoPageBreak(TRUE, PDF_MARGIN_BOTTOM);

// set image scale factor
$pdf->setImageScale(PDF_IMAGE_SCALE_RATIO);

// set some language-dependent strings (optional)
if (@file_exists(dirname(__FILE__).'/lang/eng.php')) {
	require_once(dirname(__FILE__).'/lang/eng.php');
	$pdf->setLanguageArray($l);
}

// ---------------------------------------------------------

// set font
$pdf->SetFont('dejavusans', '', 10);

// add a page
$pdf->AddPage();

// writeHTML($html, $ln=true, $fill=false, $reseth=false, $cell=false, $align='')
// writeHTMLCell($w, $h, $x, $y, $html='', $border=0, $ln=0, $fill=0, $reseth=true, $align='', $autopadding=true)

// create some HTML content



//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Intro page
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

$html = '
<br/><br/><br/><br/>
<table>
<tr>
<td align="center">
<img  align="center" src="html/img/kingsafe.png" width="525x" height="110px"/>

</td>
</tr>
</table>

';

// output the HTML content
$pdf->writeHTML($html, true, false, true, false, '');


// output some RTL HTML content
$html = '
<br/><br/><br/>
<p>
Owasp top 10 
<br/>Datum:'  .$date.'
<br/>Project: '.htmlspecialchars($projectName).'
 </p>

';
$pdf->writeHTML($html, true, false, true, false, '');

// test some inline CSS
$html = '
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
<table>
<tr>
<td align="center">

<p style="color:red; font-size:1.3em;">Confedential Document</p>
</td>
</tr>
</table>
';

$pdf->writeHTML($html, true, false, true, false, '');

// reset pointer to the last page
$pdf->lastPage();


///////////////////////////////////////////////////////////////////////////////////////////////
//END OF INTRO PAGE
///////////////////////////////////////////////////////////////////////////////////////////////
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
// Print a table

// add a page

///////////////////////////////////////////////////////////////////////////////////////////////
//Table of contents
///////////////////////////////////////////////////////////////////////////////////////////////

$pdf->AddPage();

$html = '
<br/>
<h2>Table of contents</h2>
<p>
Table of contents<br/>
Introduction<br/>
Management summary<br/>
checklist summary<br/>
';

$pdf->writeHTML($html, true, false, true, false, '');

foreach($func as $p):
// output the HTML content

$string = 
'
<p style="font-style:italic; font-size:0.8em;">'.$p["question"].'
';

$pdf->writeHTML($string, true, false, true, false, '');

endforeach;



// reset pointer to the last page
$pdf->lastPage();


///////////////////////////////////////////////////////////////////////////////////////////////
//END OF Table of contents
///////////////////////////////////////////////////////////////////////////////////////////////



///////////////////////////////////////////////////////////////////////////////////////////////
//INTRODUCTION PAGE
///////////////////////////////////////////////////////////////////////////////////////////////


// add a page
$pdf->AddPage();


$html = "

<br/>
<h2>Introduction</h2>
<p>In the post-development stage of the security knowledge framework the developer double-checks his application 
against a checklist which consists out of several questions asking the developer about <br/>
different stages of development and the methodology of implementing different types of <br/>
functionality the application contains.<br/>

After filling in this checklist the developer gains feedback on the failed checklist<br/>
items providing him with solutions about how to solve the additional vulnerability's <br/>
found in the application.<br/>

</p>
<br/>

";

// output the HTML content
$pdf->writeHTML($html, true, false, true, false, '');


// reset pointer to the last page
$pdf->lastPage();

///////////////////////////////////////////////////////////////////////////////////////////////
//END OF INTRODUCTION PAGE
///////////////////////////////////////////////////////////////////////////////////////////////




///////////////////////////////////////////////////////////////////////////////////////////////
//MANAGEMENT SUMMARY PAGE
///////////////////////////////////////////////////////////////////////////////////////////////

// add a page
$pdf->AddPage();


$html = "

<br/>
<h2>Management summary</h2>
<p>The security knowledge framework is composed by means of the highest security standards currently 
available and is designed to maintain the integrety of your application, so you and <br/>
your costumers sensitive data is protected against hackers.<br/><br/>

This document is provided with a checklist in which the programmers of your application<br/>
had to run through in order to provide a secure product. 

</p>
<br/>

";

// output the HTML content
$pdf->writeHTML($html, true, false, true, false, '');

// reset pointer to the last page
$pdf->lastPage();

///////////////////////////////////////////////////////////////////////////////////////////////
//END OF MANAGEMENT SUMMARY PAGE
///////////////////////////////////////////////////////////////////////////////////////////////




///////////////////////////////////////////////////////////////////////////////////////////////
//CHECKLIST ITEMS PAGE
///////////////////////////////////////////////////////////////////////////////////////////////

// add a page
$pdf->AddPage();
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

$html="
<br/>
<h2>Checklist items</h2>
<p>These are the results based on the filled in checklist by the programmer which <br/>
were vulnerable.
</p><br/>";

$pdf->writeHTML($html, true, false, true, false, '');

$i=0;
$string='';
foreach($func as $r):



if($r['question'] == 'null'): $item =  $r['head']; 	    endif;
if($r['question'] != 'null'): $item =  $r['question'];  endif;

$string .='
<tr>
<td width="20">'.$i++.'</td>
<td width="550">'.htmlspecialchars($item).'</td>
<td width="60"></td>

</tr>
';

endforeach;

$tbl = <<<EOD

<table border="1" cellpadding="2" cellspacing="2">
<thead>
<tr style="background-color:#FF0000; color:white;">
<td width="20" align="center">#</td>
<td width="550" align="center">Question</td>
<td width="60" align="center">Fixed</td>
</tr>
</thead>

echo $string

</table>

EOD;

$pdf->writeHTML($tbl, true, false, true, false, '');

// reset pointer to the last page
$pdf->lastPage();

///////////////////////////////////////////////////////////////////////////////////////////////
//END OF MANAGEMENT SUMMARY PAGE
///////////////////////////////////////////////////////////////////////////////////////////////




///////////////////////////////////////////////////////////////////////////////////////////////
//INDIVIDUAL ITEMS PAGE
///////////////////////////////////////////////////////////////////////////////////////////////

//$pdf->AddPage();
$ab=0;
foreach($func as $value):

if(!empty($value['vulnName'])):
$pdf->AddPage();
endif;

$html ='<h2>'.htmlspecialchars($value["vulnName"]).'</h2>
<br/>
<h4>Discription</h4>
<p>'.htmlspecialchars($value['vulnDesc']).'</p>
<br/>
<h4>Solution</h4>
<p>'.htmlspecialchars($value['vulnSol']).'</p>
<br/>

';


$pdf->writeHTML($html, true, false, true, false, '');

if(!empty($value['tech'])):

$html2='
<h4>Reference</h4>
<p>More information such as code examples and implementation guides about '.htmlspecialchars($value['vulnName']).' 
can be found in the "Code examples" section by searching for '.htmlspecialchars($value['tech']).'.</p>
';

$pdf->writeHTML($html2, true, false, true, false, '');

endif;


endforeach;






//Close and output PDF document

 $pdf->Output("results.pdf",'D');

//============================================================+
// END OF FILE
//============================================================+
