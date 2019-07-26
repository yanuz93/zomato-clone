from django.shortcuts import render, redirect, Http404
from .models import Restaurant, Menu, Review, Photo 
from .forms import InputReview, InputResto, InputFoto, InputMenu
from django.db.models import Q

# Create your views here.
def home(request):
    home = Restaurant.objects.all()
    list_kota = Restaurant.objects.values('kota').distinct()
#    list_kota = []
#    for homes in home:
#        if homes.kota not in list_kota:
#            list_kota += [homes.kota]
    return render(request, 'home.html', {'restos':home,'list_kota':list_kota})

def kota(request):
    return render (request, 'filter_by_place.html',{})

def detail(request):
    try:
        resto_id=Restaurant.objects.get(pk=restoid)
        menus = Menu.objects.all().filter(rm_id_id=resto_id.id)
        fotos = Photo.objects.all().filter(rm_id_id=resto_id.id)
        reviews = Review.objects.all().filter(rm_id_id=resto_id.id)
    except Restaurant.DoesNotExist:
        raise Http404(f"Restaurant dengan entry nomor {restoid} tidak tersedia.")
    return render(request, 'detail.html', {'resto_id':resto_id,'menus':menus,'fotos':fotos,'reviews':reviews}) 

def search(request):
    if request.method=='GET':
        loc = request.GET.get('src_loc')
        qry = request.GET.get('src_qry')
        if loc is not None:
            if qry is not None:
                src_rslt = Restaurant.objects.filter(kota__iexact=loc).filter(Q(nama__icontains=qry) | Q(alamat_lengkap__icontains=qry) | Q(masakan__icontains=qry))
                return render (request, 'search_result.html',{'search_result':src_rslt})
            src_rslt = Restaurant.objects.filter(kota__iexact=loc)
            return render (request, 'search_result.html',{'search_result':src_rslt})
    return render (request, 'search_result.html')

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

def input_menu(request):
    if request.method == "GET":
        form_menu = InputMenu(request.POST)
        if form_menu.is_valid():
            post_menu = form_menu.save(commit=False)
            post_menu.save()
            return redirect('detail')
    else:
        form_menu = InputMenu()
