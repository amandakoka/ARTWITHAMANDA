from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Artwork, Category
from .forms import ArtworkForm


# Create your views here.
def all_artworks(request):
    """ A view to show all artworks, including filtering by category """
    artworks = Artwork.objects.all()
    categories = Category.objects.all()
    selected_categories = request.GET.getlist('category')

    if selected_categories:
        artworks = artworks.filter(category__name__in=selected_categories)

    context = {
        'artworks': artworks,
        'categories': categories,
        'selected_categories': selected_categories,
    }

    return render(request, 'artworks/artworks.html', context)


def artwork_detail(request, artwork_id):
    """ View to show one artwork """

    artwork = get_object_or_404(Artwork, pk=artwork_id)

    context = {
        'artwork': artwork
    }

    return render(request, 'artworks/artwork_detail.html', context)


def add_artwork(request):
    """ Add an artwork to the store """
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save()
            messages.success(request, 'Successfully added artwork!')
            return redirect(reverse('artwork_detail', args=[artwork.id]))
        else:
            messages.error(request, 'Failed to add artwork. Please ensure the form is valid.')
    else:
        form = ArtworkForm()

    template = 'artworks/add_artwork.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
def edit_artwork(request, artwork_id):
    """ Edit an artwork in the store """
    artwork = get_object_or_404(Artwork, pk=artwork_id)
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated artwork!')
            return redirect(reverse('artwork_detail', args=[artwork.id]))
        else:
            messages.error(request, 'Failed to update artwork. Please ensure the form is valid.')
    else:
        form = ArtworkForm(instance=artwork)
        messages.info(request, f'You are editing {artwork.name}')

    template = 'artworks/edit_artwork.html'
    context = {
        'form': form,
        'artwork': artwork,
    }

    return render(request, template, context)


def delete_artwork(request, artwork_id):
    """ Delete an artwork from the store """
    artwork = get_object_or_404(Artwork, pk=artwork_id)
    artwork.delete()
    messages.success(request, 'Artwork deleted!')
    return redirect(reverse('artworks'))
