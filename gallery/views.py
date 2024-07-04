from django.shortcuts import render


# Create your views here.
def gallery(request):
    """ View to return the index page """

    return render(request, 'gallery/gallery.html')
