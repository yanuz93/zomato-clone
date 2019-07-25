from django.shortcuts import render, redirect
from .models import Restaurant, Menu, Review, Photo 
from .forms import InputReview, InputResto, InputFoto

# Create your views here.
def home(request):
    home = Restaurant.objects.all()
    list_kota = []
    for homes in home:
        if homes.kota not in list_kota:
            list_kota += homes.kota

    return render(request, 'home.html', {'restos':home,'lokasi_cari':list_kota})


def input_resto(request):
    if request.method == "POST":
        form_resto = InputResto(request.POST)
        if form_resto.is_valid():
            post_resto = form_resto.save(commit=False)
            post_resto.save()
            return redirect('home')
    else:
        form_resto = InputResto()

def input_review(request):
    if request.method == "POST":
        form_review = InputReview(request.POST)
        if form_review.is_valid():
            post_review = form_review.save(commit=False)
            post_review.save()
            return redirect('home')
    else:
        form_review = InputReview()

def input_foto(request):
    if request.method == "POST":
        form_foto = InputFoto(request.POST)
        if form_foto.is_valid():
            post_foto = form_foto.save(commit=False)
            post_foto.save()
            return redirect('home')
    else:
        form_foto = InputFoto()


