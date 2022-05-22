from django.urls import path
from core import views
urlpatterns = [
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logout/', views.user_logout, name="logout"),
    path('', views.user_login, name="login"),
    path('signup/', views.user_signup, name="signup"),
    path('addpost/', views.add_post, name="addpost"),
    path('updatepost/<int:id>/', views.update_post, name="updatepost"),
    path('deletepost/<int:id>/', views.delete_post, name="deletepost"),
    path('detailpost/<int:id>/', views.detailsPost, name="detailpost"),
    path('make-prediction',views.makePrediction, name="makePrediction"),
]
