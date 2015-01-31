<?php
foreach($func as $f):

$projectName   = $f['projectName'];
$date_ 		   = $f['entryDate'];

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
$pdf->SetAuthor('');
$pdf->SetTitle('The security knowledge framework');
$pdf->SetSubject('Function resukts');
$pdf->SetKeywords('info@kingsafe.nl');

// set default header data
$pdf->SetHeaderData('', '15px;', ' Security knowledge framework', '       Pre-development');

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
<img  src="html/img/kingsafe.png" width="525x" height="110px"/>

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
Pre-development 
<br/>Datum:' .$date_.'
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
Management Summary<br/>
Checklist items
';

$pdf->writeHTML($html, true, false, true, false, '');

foreach($func as $p):
// output the HTML content

$string = 
'
'.htmlspecialchars($p["vulnName"]).'
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
<p>In this part of security knowledge framework, al the paramaters and variables are audited by <br/> 
means of the information given
by the programmer in the kingsafe application such as the processing techniques and globaltypes.
<br/> <br/>

Ech of these techniques and globaltypes contain different types of func's when <br/>
implemented in a inproper fashion<br/>
This document will rais awareness about these func's, as well as presenting <br/>
solutions for the right implementation

<br/> <br/>  
Througout the document you will find your application functions devided into different<br/>
chapters and provided with a checklist which indicates the types of func's <br/>
the function could possibly be vulnerable to.<br/>
After the func's are solved the 'fixed' tab can be checked by the programmer


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
<p>security knowledge framework is composed by means of the highest security standards currently <br/>
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
foreach($func as $r):

$string .='
<tr>
<td width="20">'.$i++.'</td>
<td width="100">'.htmlspecialchars($r["functionName"]).'</td>
<td width="150">'.htmlspecialchars($r["techName"]).'</td>
<td width="350">'.htmlspecialchars($r["vulnName"]).'</td>
</tr>
';

endforeach;

$tbl = <<<EOD

<table border="1" cellpadding="2" cellspacing="2">
<thead>
<tr style="background-color:#FF0000; color:white;">
<td width="20" align="center">#</td>
<td width="100" align="center">Listname</td>
<td width="150" align="center">Technique</td>
<td width="350" align="center">func</td>

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

header('Content-type: application/pdf');
header('Content-Disposition: attachment; filename="file.pdf"');


//Close and output PDF document
$pdf->Output('FunctionResults.pdf', 'D');

//============================================================+
// END OF FILE
//============================================================+
