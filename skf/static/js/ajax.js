
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


function delProject(projectID, csrf_token)
{
    $.ajax({
        url : 'project-del',
        data:{"projectID":projectID, "csrf_token":csrf_token},
        type: 'POST',

        success: function(data){
            $('#projectRow'+projectID).html(data);
        }
    });
}

function delFunction(id,paramID,csrf_token)
{
    $.ajax({
        url : '/project-function-del',
        data:{"projectID":id,"paramID":paramID,"csrf_token":csrf_token},
        type: 'POST',

        success: function(data){
            $('#projectRow'+id).html(data);
        }
    });
}

function delChecklist(time,csrf_token)
{
    $.ajax({
        url : '/results-checklists-del',
        data:{"entryDate":time,"csrf_token":csrf_token},
        type: 'POST',

        success: function(data){
            $('#projectRow'+id).html(data);
        }
    });
}


function delFunctionList(time,csrf_token)
{
    $.ajax({
        url : '/results-functions-del',
        data:{"entryDate":time,"csrf_token":csrf_token},
        type: 'POST',

        success: function(data){
            $('#projectRow'+id).html(data);
        }
    });
}


$(document).ready(function(){

    $('[data-toggle="tooltip"]').tooltip();   

});


