from django.urls import path
from . import views


app_name = 'list_app'

urlpatterns = [
    path('list/', views.list_view, name='list'),
    path('create/', views.create_view, name='create')
]