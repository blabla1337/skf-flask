
function getItem(id)
{
    $.ajax({
        url : 'kb-item',
        data:{"id":id},
        type: 'POST',

        success: function(data){
            $('#'+id).html(data);
            $(document).ready(function() {

            });
        }
    });
}


function getCode(id)
{
    $.ajax({
        url : 'code-item',
        data:{"id":id},
        type: 'POST',

        success: function(data){
            $('#'+id).html(data);
            $(document).ready(function() {
                $('pre code').each(function(i, block) {
                    hljs.highlightBlock(block);
                });
            });
        }
    });
}



$(document).ready(function(){

    $('[data-toggle="tooltip"]').tooltip();   

});


