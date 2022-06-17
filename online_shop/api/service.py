# from django_filters import filters
import django_filters
from rest_framework.pagination import PageNumberPagination

from .models import Product

class CharFilter(django_filters.BaseInFilter, django_filters.CharFilter):
    pass

class DoubleFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
    pass

class ProductFilter(django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr="in")
    articule = CharFilter(field_name="articule", lookup_expr="in")
    category = CharFilter(field_name="category__catalog", lookup_expr="in")
    category2 = CharFilter(field_name="category__type", lookup_expr="in")
    # price = DoubleFilter(field_name="price", lookup_expr="in")
    price = django_filters.RangeFilter()

    # order_by = django_filters.OrderingFilter(
    #     fields= (
    #         ('title', 'title')
    #     )
    # )

    class Meta:
        model = Product
        fields = ['title', 'articule', 'category', 'price', 'category2']


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 2
