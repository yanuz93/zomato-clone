from django.contrib import admin
from .models import Restaurant, Review, Photo, Menu, Kategori
# Register your models here.
@admin.register(Restaurant)
class AuthorResto(admin.ModelAdmin):
    list_display = ('id', 'nama', 'kota', 'alamat_lengkap', 'masakan', 'kontak', 'buka_jam', 'tutup_jam')
    list_display_links = ('id', 'nama', 'kota')

@admin.register(Menu)
class AuthorMenu(admin.ModelAdmin):
    list_display = ('id', 'nama', 'deskripsi', 'harga')
    list_display_links = ('id', 'nama', 'harga')

@admin.register(Photo)
class AuthorFoto(admin.ModelAdmin):
    list_display = ('id', 'pict_url')
    list_display_links = ('id', 'pict_url')

@admin.register(Review)
class AuthorReview(admin.ModelAdmin):
    list_display = ('id', 'nama', 'judul', 'isi', 'nilai')
    list_display_links = ('id', 'nama', 'judul', 'nilai')

@admin.register(Kategori)
class AuthorFoto(admin.ModelAdmin):
    list_display = ('id', 'description')
    list_display_links = ('id', 'description')
