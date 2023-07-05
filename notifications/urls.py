from django.urls import path 
from . import views


urlpatterns = [
    path('create-notification/', views.create_notification_view, name='create-notice'),
    path('received-notifications/', views.received_notifications_view, name='received_notifications'),
]