from django.urls import path
from admin_panel.views import RegUserView, RemoveUserView

urlpatterns = [
    path("registered-users", RegUserView.as_view(), name="registered-users"),
    path("remove/<int:id>", RemoveUserView.as_view(), name="remove"),
]