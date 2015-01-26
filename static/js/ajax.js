
function getItem(id)
{
    $.ajax({
        url : 'kb-item',
        data:{"id":id},
        type: 'POST',

        success: function(data){
            $('#'+id).html(data);
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
        }
    });
}

function delProject(projectID)
{
    $.ajax({
        url : 'project-del',
        data:{"projectID":projectID},
        type: 'POST',

        success: function(data){
            $('#projectRow'+projectID).html(data);
        }
    });
}

function delFunction(id,paramID)
{
    $.ajax({
        url : '/project-function-del',
        data:{"projectID":id,"paramID":paramID},
        type: 'POST',

        success: function(data){
            $('#projectRow'+id).html(data);
        }
    });
}

