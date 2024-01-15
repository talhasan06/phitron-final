
from django.urls import path
from .views import UserRegistrationFormView,UserLoginView,UserLogoutView
urlpatterns = [
    path('register/',UserRegistrationFormView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
]
