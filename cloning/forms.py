from .models import Restaurant, Menu, Review, Photo 
from django import forms

class InputResto(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('nama', 'kota', 'alamat_lengkap', 'masakan', 'kontak', 'buka_jam', 'tutup_jam', 'the_choices')

class InputMenu(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('nama', 'deskripsi', 'harga')

class InputFoto(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('pict_url',)

class InputReview(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('nama', 'judul', 'isi', 'nilai')
