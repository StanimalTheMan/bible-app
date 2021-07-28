from django.urls import path 
from .views import VerseListView

urlpatterns = [
    path('', VerseListView.as_view(), name='home')
]