from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registerpage/', views.registerPage, name='registerPage'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutPage, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_product/', views.add_product, name='add_product'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('edit-product/', views.edit_product, name='edit_product'),

]
