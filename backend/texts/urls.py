from django.urls import path
from . import views

urlpatterns = [
    path('', views.texts_collection, name='texts-collection'),  # /api/texts/
    path('<str:text_id>/', views.texts_detail, name='texts-detail'),  # /api/texts/{id}/
]
