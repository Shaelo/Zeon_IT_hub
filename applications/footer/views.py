from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from applications.footer.models import FirstFooterTab, SecondFooterTab
from applications.footer.serializers import FirstFooterTabSerializer, SecondFooterTabSerializer


@api_view(['GET'])
def FooterView(request):
    first_obj = FirstFooterTab.objects.all()
    second_obj = SecondFooterTab.objects.all()
    first_serializer = FirstFooterTabSerializer(first_obj, many=True)
    second_serializer = SecondFooterTabSerializer(second_obj, many=True)
    result = first_serializer.data + second_serializer.data
    return Response(result)