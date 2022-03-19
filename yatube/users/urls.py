from django.contrib.auth.views import *
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUp.as_view(template_name='users/signup.html'), name='signup'),
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path(
        'auth/password_change/',
        PasswordChangeView.as_view(template_name='users/password_change_form.html'),
        name='pass_ch_v'
    ),
    path(
        'auth/password_change/done/',
        PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
        name='pass_ch_d'
    ),
    path(
        'auth/password_reset/',
        PasswordResetView.as_view(template_name='users/password_reset_form.html'),
        name='pass_res'
    ),
    path(
        'auth/password_reset/done/',
        PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='pass_res_d'
    ),
    path(
        'auth/reset/<uidb64>/<token>',
        PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='pass_res_conf'
    ),
    path(
        'auth/reset/done',
        PasswordResetView.as_view(template_name='users/password_reset_complete.html'),
        name='pass_res_compl'
    ),

]
