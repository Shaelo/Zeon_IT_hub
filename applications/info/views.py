from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from applications.info.serializers import *
from applications.info.models import *
from rest_framework.generics import *


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 8
    page_query_param = 'page_size'
    max_page_size = 9999

@api_view(['GET'])
def AboutUsView(request):
    image_obj = Image.objects.all()
    about_us_obj = AboutUs.objects.all()
    image_serializer = AboutUsImageSerializer(image_obj, many=True)
    help_serializer = AboutUsSerializer(about_us_obj, many=True)
    result = image_serializer.data + help_serializer.data
    return Response(result)


class OfferView(ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class NewsView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = LargeResultsSetPagination

