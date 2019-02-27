from django.shortcuts import render

# Function Based Views, will switch over to CLass Based Views in the fututre.

def home(request):
    """
    Homepage for gallery of pictures.
    """
    return render(request, 'landing.html')