from django.shortcuts import render
from .models import Picture
# Function Based Views, will switch over to CLass Based Views in the fututre.

def home(request):
    """
    Homepage for gallery of pictures.
    """
    picture = Picture.objects.all()
    return render(request, 'landing.html', {'picture': picture})