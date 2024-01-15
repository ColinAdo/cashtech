from django.urls import path

from . import views, transfer

urlpatterns = [
    path("", views.index, name="index"),
    
    # Transfers
    path("search/", transfer.search_account, name="search_account"),
]
