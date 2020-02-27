from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def social(request):
    return render(request, 'social.html')