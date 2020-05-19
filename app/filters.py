import django_filters
from .models import Film


class FilmFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    duration = django_filters.NumberFilter()
    price_gt = django_filters.NumberFilter(
        field_name='price', lookup_expr='gt')
    price_lt = django_filters.NumberFilter(
        field_name='price', lookup_expr='lt')
    ratings_gt = django_filters.NumberFilter(
        field_name='ratings', lookup_expr='gte')

    class Meta:
        model = Film
        fields = []
