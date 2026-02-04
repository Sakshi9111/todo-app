from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Django-provided login view
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="login",
    ),

    # Django-provided logout view
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),

    # Custom signup view
    path(
        "signup/",
        views.signup_view,
        name="signup",
    ),
]

