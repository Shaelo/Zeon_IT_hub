from django.urls import path
from applications.info.views import *
from applications.product.views import *

urlpatterns = [
    path('collections/', CollectionView.as_view()),
]