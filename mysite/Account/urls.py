from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('login', views.login_page, name='login'),
    # path('logout', views.logout, name='logout'),
    path('register', views.register_page, name='register'),
]