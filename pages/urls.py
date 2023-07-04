from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('ENSPD/', views.enspd_home_page_view, name='enspd_home'),
]