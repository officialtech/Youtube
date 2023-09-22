from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_data, name="create"),
    path('success/', views.success, name="success_page"),
]
