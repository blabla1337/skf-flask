//Array is as follows [diamond name, price, place to write value ]

var diamond = [];

diamond[0] = ["#powermail_fieldwrap_9 .powermail_input"		,"123"  , "#powermail_fieldwrap_9  .price"]; 
diamond[1] = ["#powermail_fieldwrap_10 .powermail_input"	,"122"  , "#powermail_fieldwrap_10 .price"]; 
diamond[2] = ["#powermail_fieldwrap_11 .powermail_input" 	,"233"  , "#powermail_fieldwrap_11 .price"]; 
diamond[3] = ["#powermail_fieldwrap_12 .powermail_input"	,"333"  , "#powermail_fieldwrap_12 .price"]; 
diamond[4] = ["#powermail_fieldwrap_13 .powermail_input"	,"334"  , "#powermail_fieldwrap_13 .price"]; 



//Foreach loop for the diamond array
diamond.forEach(function (item) 
{
	$(document).ready(function() {
		$(item[0]).keyup(function() {
			
			//Here we do the math
			var amount = $(item[0]).val();
			var price =  item[1]
				
			var total = amount * price ;
			
			//We call on currency format for...... currency formatting :D
			var formatted = currencyFormat(total);
			
			$(item[2]).text('EUR '+ formatted);
		    totalCount();
	    });//end onkeyup
	});//end document.ready  
})//endforeach

function totalCount(){		

	var total = 0 ;	
    for(var i = 0 ; i < diamond.length ; i++){
        
        var inputValue = diamond[i][0];
        var currency   = diamond[i][1];
                
        var values = $(inputValue).val();
        
        var totalSum = values * currency;
        total += totalSum;
        var final = currencyFormat(total);
    }
    $('#powermail_field_totalprice').val(final);
    $('#total1.prices').text(final);
    
    }


//Here is where we change the currency format.
function currencyFormat (num) 
{
    return num.toFixed(2).replace(/([^\d.,]+)\s*([\d.,]+)\s*([^\d.,]+)/g, "$1,")
}
