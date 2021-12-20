from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import resetpasswordform,setpasswordform
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('create-todo/',views.createtodo,name="create"),
    path('update-todo/<str:pk>/',views.updatetodo,name="update"),
    path('delete-todo/<str:pk>/',views.deletetodo,name="delete"),
    path('details-todo/<str:pk>/',views.detailstodo,name="details"),
    path('accounts/register/',views.registerpage,name="register"),
    path('accounts/login/',views.loginpage,name="login"),
    path('accounts/logout/',views.logoutpage,name="logout"),
    path('accounts/password_reset/',auth_views.PasswordResetView.as_view(template_name='base/password_reset.html',form_class=resetpasswordform),name="password_reset"),
    path('accounts/password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='base/password_reset_done.html'),name="password_reset_done"),
    path('accounts/reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='base/password_reset_confirm.html',form_class=setpasswordform),name="password_reset_confirm"),
    path('accounts/reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='base/password_reset_complete.html'),name="password_reset_complete"),
]
