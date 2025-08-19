from django.urls import path
from accounts import views  
 

urlpatterns = [
    
    path('brands/', views.brand_list, name="brand"),
    path('brand/create/', views.create, name="create"),
    path('brand/edit/<int:pk>/', views.edit, name="edit"),
    path('brand/delete/<int:pk>/', views.delete, name="delete"),
]