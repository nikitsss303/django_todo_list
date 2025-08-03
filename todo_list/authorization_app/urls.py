from django.urls import path
from . import views


app_name = 'authorization_app'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('test/', views.test_view, name='test')
]