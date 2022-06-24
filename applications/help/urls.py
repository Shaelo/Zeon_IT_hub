from django.urls import path
from applications.help.views import HelpView

urlpatterns = [
    path('info/', HelpView),
]