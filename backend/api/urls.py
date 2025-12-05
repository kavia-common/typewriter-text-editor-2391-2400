from django.urls import path
from .views import health
from texts.views import texts_collection, texts_detail

urlpatterns = [
    path('health/', health, name='Health'),
    path('texts/', texts_collection, name='texts-collection'),
    path('texts/<str:text_id>/', texts_detail, name='texts-detail'),
]
