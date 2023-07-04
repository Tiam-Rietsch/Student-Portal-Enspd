from django.urls import path 
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/edit_profile_photos/', views.edit_profile_photos, name='edit-profile-photos'),

    path('dashboard/admin/', views.admin_dashboard_view, name='dashboard'),

    path('profile/', views.profile_page_view, name='profile'),
    path('profile/get-slot-data/', views.get_slot_data, name='get-slot-data'),
    path('profile/get-calendar/', views.get_calendar, name='get-calendar'),
]