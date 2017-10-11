# Privilege based authentication
-------

## Example:


    """
    For privilege based authentication we will use the table permissions.

    TABLE permissions
    ------------------------------------------------------------
    |       *Name*      |       *Type*      |    *Extra*       |
    ------------------------------------------------------------
    |         ID        |       Int(11)     |   AUTO_INCREMENT |
    ------------------------------------------------------------
    |  content_type_id  |       Int(11)     |                  |
    ------------------------------------------------------------
    |      codename     |    Varchar(255)   |                  |
    ------------------------------------------------------------
    |        name       |    varchar(30)    |                  |
    ------------------------------------------------------------

    Permissions are associated with models, and define the operations that can be performed on a model instance by a user who has the permission . Django automatically gives add, change, and delete permissions to all models by default.
    """

    //Adding certain privileges to user
    //Selecting particular User and adding permission
    user = User.objects.filter(username='user1').first()
    user.user_permissions = [Permission.objects.get(codename='change_choice')]

    """
    Permissions can be checked in both templates and views.
    In templates, Current user's permission are checked in template variable {{ perms }}
    In Views, Permissions can be tested in function view using the permission_required decorator or in class based view we can use PermissionRequiredMixin
    """
    
    //In templates
    {% if perms.polls.change_choice %}
      <!-- Add appropriate code. -->
    {% endif %}

    //In Views 
    @permission_required('polls.change_choice')
    @permission_required('polls.can_edit')
    def my_view(request):
      ...

    //Permission-required for class based views
    from django.contrib.auth.mixins import PermissionRequiredMixin

    class MyView(PermissionRequiredMixin, View):
        permission_required = 'catalog.can_mark_returned'
        ...