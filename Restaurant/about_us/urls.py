from django.urls import path
from .  import views

urlpatterns = [
    path('about/<int:ide>/', views.aboutUs , name='about'),
    

]
