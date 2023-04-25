from django.urls import path
from . import views

urlpatterns = [
    path('', views.highlight_sentence, name='highlight_sentence'),
]
