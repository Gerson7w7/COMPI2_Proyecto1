from django.shortcuts import render
import requests

# Create your views here.
def editor(request):
    return render(request, 'editor.html')