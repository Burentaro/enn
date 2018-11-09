from django.urls import path

from . import views


urlpatterns = [
    path('', views.menu, name='menu'),
    path('detail/', views.menu_item_detail, name='detail'),
    path('create/', views.menu_item_create, name='create'),
]
