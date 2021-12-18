from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('create-todo/',views.createtodo,name="create"),
    path('update-todo/<str:pk>/',views.updatetodo,name="update"),
    path('delete-todo/<str:pk>/',views.deletetodo,name="delete"),
    path('details-todo/<str:pk>/',views.detailstodo,name="details"),
    path('register/',views.registerpage,name="register"),
    path('login/',views.loginpage,name="login"),
    path('logout/',views.logoutpage,name="logout"),
]
