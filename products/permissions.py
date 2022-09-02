from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    # def has_permission(self, request, view):
        # if not request.user.username == 'Raiden': # to spacify by name
        #     return False
        # if request.user.is_staff:
            # return False
        # return super().has_permission(request, view)


    # def has_permission(self, request, view):
    #     # return super().has_permission(request, view)
    #     user = request.user
    #     print(user.get_all_permissions())
    #     if user.is_staff:
    #         # products is the name of the app
    #         # product is the name of the models in lowercase
    #         if user.has_perm("products.add_product"):  # app_name.action_model_name
    #             return True
    #         if user.has_perm("products.delete_product"):
    #             return True
    #         if user.has_perm("products.change_product"):
    #             return True
    #         if user.has_perm("products.view_product"):
    #             return True
    #     return False


    # def has_object_permission(self, request, view, obj):
    #     owner should be in model.py as owener = models.ForeginKey(User)
    #     return obj.owner == request.user
