from django.shortcuts import render
from artworks.models import Artwork


def gallery(request):
    """ View to return the gallery page with a list of artworks """
    artworks = Artwork.objects.all()
    return render(request, 'gallery/gallery.html', {'artworks': artworks})
