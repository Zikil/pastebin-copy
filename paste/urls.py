from django.urls import path

from .views import *

urlpatterns = [
    path('', PasteCreate.as_view(), name='paste_create_url'),
    path('all/', paste_list, name='paste_list_url'),
    path('<str:slug>/', PasteDetail.as_view(), name='paste_detail_url'),
    path('<str:slug>/delete', PasteDelete.as_view(), name='paste_delete_url'),
]
