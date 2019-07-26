from .models import Restaurant, Review, Photo, Menu
import django_filters

class RestoFilter(django_filters.FilterSet):
    class Meta:
        model = Restaurant
        fields = {
            'nama' = 'icontains',
            'alamat_lengkap' = 'icontains',
            'masakan' = 'icontains',
            'kota' = 'iexact',} 
