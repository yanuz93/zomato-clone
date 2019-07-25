from django.contrib import admin
from .models import Restaurant, Review, Photo, Menu
# Register your models here.
@admin.register(Restaurant)
class AuthorResto(admin.ModelAdmin):
    list_display = ('nama', 'kota', 'alamat_lengkap', 'masakan', 'rerata_harga', 'kontak', 'buka_jam', 'tutup_jam')
    list_display_links = ('nama', 'kota')

class AuthorMenu(admin.ModelAdmin):
    list_display = ('nama', 'deskripsi', 'harga')
    list_display_links = ('nama', 'harga')

class AuthorFoto(admin.ModelAdmin):
    list_display = ('pict_url')
    list_display_links = ('pict_url')

class AuthorReview(admin.ModelAdmin):
    list_display = ('nama', 'judul', 'isi', 'nilai')
    list_display_links = ('nama', 'judul', 'nilai')
