import django_filters
from .models import Menu

class MenuFilter(django_filters.FilterSet):
    meal_name = django_filters.CharFilter(lookup_expr='iexact')
    keyword = django_filters.filters.CharFilter(field_name="meal_name",lookup_expr="icontains")
    min_price = django_filters.filters.NumberFilter(field_name="price" or 0,lookup_expr="gte")
    max_price = django_filters.filters.NumberFilter(field_name="price" or 90000,lookup_expr="lte")

    class Meta:
        model = Menu
        fields = ('category','keyword','min_price','max_price')
