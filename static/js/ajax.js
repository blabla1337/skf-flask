
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

function delProject(id)
{
    $.ajax({
        url : 'project-del',
        data:{"projectID":id},
        type: 'POST',

        success: function(data){
            $('#projectRow'+id).html(data);
        }
    });
}

