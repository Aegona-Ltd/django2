from django.urls import path
from src.views.cms import dashboard, account, admin, groupPermission,contact

app_name = "cms"
urlpatterns = [
    path("auth/login", account.login, name="login"),
    path("logout", account.logout, name="logout"),
    path("", dashboard.index, name="dashboard"),
    # admin
    path("admin", admin.index, name="admin.index"),
    path("admin/create", admin.create, name="admin.create"),
    path("admin/update/<id>", admin.update, name="admin.update"),
    path("admin/delete", admin.delete, name="admin.delete"),
    # group permission
    path("group-permission", groupPermission.index, name="groupPermission.index"),
    path(
        "group-permission/create", groupPermission.create, name="groupPermission.create"
    ),
    path(
        "group-permission/update/<id>",
        groupPermission.update,
        name="groupPermission.update",
    ),
    path(
        "group-permission/delete", groupPermission.delete, name="groupPermission.delete"
    ),
    path("contact", contact.index, name="contact.index"),
]
