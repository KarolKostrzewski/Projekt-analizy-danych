from django.shortcuts import render

# Create your views here.

def snooker(request):
    return render(request, 'snooker.html')