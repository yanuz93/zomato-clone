from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('detail/',views.detail, name='halaman_detail'),
    path('search/page<int:page>/',views.search, name='halaman_search'),
    path('kota/',views.kota, name='cari_kota'),
    path('filter/',views.filter, name='filter_by_place'),
    path('filter/',views., name='filter_by_category'),
    path('tambah/',views.input_resto, name'tambah_foto'),
    path('tambah/',views.input_resto, name'tambah_foto'),
    path('tambah/',views.input_resto, name'tambah_foto'),

]
