from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='halaman_home'),
    path('detail/',views.detail, name='halaman_detail'),
    path('search/',views.search, name='halaman_search'),
]