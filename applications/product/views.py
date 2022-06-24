from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from applications.product.models import Collection, Product
from applications.product.serializers import CollectionSerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 8
    page_query_param = 'page_size'
    max_page_size = 9999


class CollectionView(ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = LargeResultsSetPagination