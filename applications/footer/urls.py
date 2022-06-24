from django.urls import path
from applications.footer.views import FooterView

urlpatterns = [
    path('info/', FooterView),
]