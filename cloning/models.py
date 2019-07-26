from django.db import models

# Create your models here.
class Kategori(models.Model):
    description = models.CharField(max_length=30)

class Restaurant(models.Model):
    nama = models.CharField(max_length=100)
    kota = models.CharField(max_length=50)
    alamat_lengkap = models.TextField(max_length=500)
    masakan = models.CharField(max_length=30)
    kontak = models.CharField(max_length=20)
    buka_jam = models.TimeField()
    tutup_jam = models.TimeField()
    the_choices = models.ManyToManyField(Kategori)


class Menu(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField(max_length=500)
    harga = models.PositiveIntegerField()
    rm_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Review(models.Model):
    nama = models.CharField(max_length=100)
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    nilai = models.FloatField()
    rm_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Photo(models.Model):
    pict_url = models.URLField(max_length=200)
    rm_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


