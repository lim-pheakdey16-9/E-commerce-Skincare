from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
    path('logout/', views.logout, name='logout'),   
    path('dashboard/', views.dashboard, name="dashboard"),
    path('card/', views.card, name="card"),
    path('shop/', views.shop, name="shop"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),



 
]