from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
from artworks.models import Artwork

def gallery(request):
    """ View to return the gallery page with a list of artworks """
    artworks = Artwork.objects.all()
    return render(request, 'gallery/gallery.html', {'artworks': artworks})

def review_form(request):
    """ View to display and handle the review form """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = ReviewForm()

    return render(request, 'gallery/review_form.html', {'form': form})
