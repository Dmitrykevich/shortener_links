from django.urls import path

from .views import IndexView, LinksListView, redirect_to_origin_url

app_name = 'shortener'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('links/', LinksListView.as_view(), name='links'),
    path('<str:url_hash>/', redirect_to_origin_url, name='redirect_origin'),
]
