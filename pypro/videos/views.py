from django.shortcuts import render


# Create your views here.
def video(request, slug):
    return render(request, 'videos/video.html')
