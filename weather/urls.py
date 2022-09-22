from django.urls import path
from . import views

# name='city_detail_view' means identifier from models.py reverse name
urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('city/<int:id>/', views.city_id_view, name='city_detail_view'),
]
