from django.urls import path
from applications.info.views import *

urlpatterns = [
    path('about-us/', AboutUsView),
    path('offer/', OfferView.as_view()),
    path('news/', NewsView.as_view()),
]