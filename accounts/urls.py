from django.urls import path
from accounts.views import UserLogin,UserRegister,Logout,RefreshAccess,UserValidationView,OverView

urlpatterns = [
    path("login", UserLogin.as_view(), name="login"),
    path("register", UserRegister.as_view(), name="register"),
    path("logout", Logout.as_view(), name="logout"),
    path("refresh", RefreshAccess.as_view(), name="refresh"),
    path("overview", OverView.as_view(), name="overview"),
    path("is-valid", UserValidationView.as_view(), name="is-valid"),

]


