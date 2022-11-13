from django.shortcuts import render

def fist(request):
    return render(request, 'main/index.html')

