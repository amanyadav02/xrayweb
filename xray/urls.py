from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('checkcovid/',views.checkcovid,name='checkcovid'),

     path("login/", views.logindevta, name="login"),
    path("register/", views.registerdevta, name="register"),
    path("logout/", views.logoutdevta, name="logout"),

    # email authentication
    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name="xray/password_reset.html"),
        name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="xray/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="xray/password_reset_form.html"), 
        name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="xray/password_reset_done.html"), 
        name="password_reset_complete"),

]

