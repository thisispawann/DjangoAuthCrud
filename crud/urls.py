from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# Creating URLs

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'), # class based view
    path('home/', views.home, name="home"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create', views.Create, name='create'),
    path('delete/<int:pk>/', views.Delete, name='delete'),
    path('update/<int:pk>/', views.Update, name='update'),
    path('detail/<int:pk>/', views.Detail, name='detail')
]
