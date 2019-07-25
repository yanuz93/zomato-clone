from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='halaman_home'),
]