from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('detail/',views.detail, name='halaman_detail'),
    path('search/',views.search, name='halaman_search'),
]
