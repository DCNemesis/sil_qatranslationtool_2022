from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('upload/', views.upload, name='upload'),
    path('results/', views.results, name='results'),
    path('results/similarity/', views.similarity, name='similarity'),
    path('results/readability/', views.readability, name='readability'),
    path('results/comprehensibility/', views.comprehensibility, name='comprehensibility'),
]
