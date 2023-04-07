"""
URL mappings for the user API.
The 'name' here, is what is reversed engineered with the
reverse function in the unittests.
"""
from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]
