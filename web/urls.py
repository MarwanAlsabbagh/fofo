from django.urls import path
from . import views

urlpatterns = [
    path('search/<str:q>',views.search,name='search'),
    path('get_all',views.get_all_docs,name='get_all_docs'),
    path('open/<str:file_name>',views.open_file,name='open_file'),
]