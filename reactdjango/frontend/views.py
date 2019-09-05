from django.shortcuts import render

# Create your views here.
def index(request):
    """
        Look at the index.html which then looks at the id App
        which points to the index.js which imports the App.js
    """
    return render(request, 'frontend/index.html') 