from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
]
