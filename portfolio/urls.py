# portfoilio/urls.py

from django.urls import path
from .views import ProjectView, PortfolioView, home

urlpatterns = [
    path('', home, name='welcome'),
    path('home<int:pk>/', PortfolioView.as_view(), name='home'),
]
