from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('detail/',views.detail, name='halaman_detail'),
    path('search/',views.search, name='halaman_search'),
    path('tambah/resto',views.input_resto, name='tambah_resto'),
    path('tambah/foto',views.input_foto, name='tambah_foto'),
    path('tambah/review',views.input_review, name='tambah_review'),
    path('tambah/menu',views.input_menu, name='tambah_menu'),
]
