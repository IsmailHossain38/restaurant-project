from django.urls import path
from .  import views

urlpatterns = [
    path('show_item/<int:id>/', views.show_item , name='show_item'),
    
]