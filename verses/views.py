from django.views.generic import ListView 
from .models import Verse

# Create your views here.
class VerseListView(ListView):
    model = Verse 
    template_name = 'home.html'