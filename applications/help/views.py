from rest_framework.decorators import api_view
from applications.help.models import *
from applications.help.serializers import HelpSerializer, ImageSerializer
from rest_framework.response import Response


@api_view(['GET'])
def HelpView(request):
    image_obj = Image.objects.all()
    help_obj = Help.objects.all()
    image_serializer = ImageSerializer(image_obj, many=True)
    help_serializer = HelpSerializer(help_obj, many=True)
    result = image_serializer.data + help_serializer.data
    return Response(result)