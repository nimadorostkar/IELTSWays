from django.urls import path
from accounts.views import UserLogin,UserRegister, Logout,Refresh,RefreshAccess,UserValidationView,OverView

urlpatterns = [
    path("login", UserLogin.as_view(), name="login"),
    path("register", UserRegister.as_view(), name="register"),

    path("refresh", Refresh.as_view(), name="refresh"),
    path("refresh-access", RefreshAccess.as_view(), name="refresh-access"),
    path("logout", Logout.as_view(), name="logout"),
    path("overview", OverView.as_view(), name="overview"),
    path("user-is-valid", UserValidationView.as_view(), name="is-valid"),

]


