"""Users URL's."""

# Django
from django.urls import path

# Views
from spotify.users import views


urlpatterns = [
    # Management

    path(
        route='',
        view=views.feed,
        name='feed'
    ),
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),
    path(
        route="user/<str:username>/",
        view=views.UpdateProfileView.as_view(),
        name="update"
    ),
]
