from django.urls import path
from .views import update_profile

app_name = 'user_management'

urlpatterns = [
    path('profile/', update_profile, name='update_profile'),
]
