from django.shortcuts import render

# Create your views here.

def account(request):
    """ Display the user's account. """

    template = 'accounts/account.html'
    context = {}

    return render(request, template, context)